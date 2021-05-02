from django.contrib import admin
from .models import Gig, Category, SubCategory, Plan, Comment, ShowcaseImage, UserRate

admin.site.register(Gig)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Plan)
admin.site.register(Comment)
admin.site.register(ShowcaseImage)
admin.site.register(UserRate)
