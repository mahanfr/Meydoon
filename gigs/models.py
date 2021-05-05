from django.db import models
from django.contrib.auth import get_user_model

# Best Practice for getting the user model
User = get_user_model()


# This a model that hanndels advertisment for intrested user
# to be shown to other users
class Gig(models.Model):
    title = models.CharField(max_length=50,null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey('gigs.Category',on_delete=models.SET_NULL,null=True,blank=True)
    sub_category = models.ForeignKey('gigs.SubCategory', on_delete=models.SET_NULL,null=True,blank=True)
    description = models.TextField()
    experience = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.user.user_name} {self.title} gig'
    
    def get_showcase(self):
        showcase = ShowcaseImage.objects.all().filter(gig=self)
        return showcase[0].image


# Every gig has a category and you can choose one 
# from database of this model
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


# Every gig has a category and you can choose one 
# from database of this model
class SubCategory(models.Model):
    category = models.ForeignKey('gigs.Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.category} - {self.name}'


# every gig have one or more plans that can be
# used to advertise different tier of services
class Plan(models.Model):
    gig = models.ForeignKey('gigs.Gig',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=5000)
    feature_list = models.TextField()

    def __str__(self):
        return f'gig #{self.gig.id} plan'


# a gig can have some comments
class Comment(models.Model):
    gig = models.ForeignKey('gigs.Gig',on_delete=models.CASCADE)
    user = models.ForeignKey('users.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=255)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.user_name} on gig #{self.gig.id}'


# every gig can have multiple images that showcase the user work
class ShowcaseImage(models.Model):
    gig = models.ForeignKey('gigs.Gig',on_delete=models.CASCADE)
    image_meta = models.CharField(max_length=50)
    image = models.ImageField(upload_to='scimages',default='default.jpg')

    def __str__(self):
        return f'#{self.id}'


# This model class handels ratings for a gig
class UserRate(models.Model):
    gig = models.ForeignKey('gigs.Gig',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'#{self.id}'
