from django import forms
from .models import Gig, ShowcaseImage,Comment

class GigCreationForm(forms.ModelForm):
    """
    Form for add Gig 
    """
    class Meta:
        model = Gig
        fields = ['title','category', 'description', 'experience']
        exclude = ['user']

class ShowcaseForm(forms.ModelForm):
    """
    Form for add Gig 
    """
    class Meta:
        model = ShowcaseImage
        fields = ['image_meta', 'image']
        exclude = ['gig']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['title', 'body']
        exclude = ['gig','user', 'is_aproved']
                