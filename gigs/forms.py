from django import forms
from django.db.models.fields.related import ForeignKey
from .models import Gig, ShowcaseImage

class GigCreationForm(forms.ModelForm):
    """
    Form for add Gig 
    """
    class Meta:
        model = Gig
        fields = ['title','category', 'description', 'experience', 'user']
        exclude = ['user']

class ShowcaseForm(forms.ModelForm):
    """
    Form for add Gig 
    """
    class Meta:
        model = ShowcaseImage
        fields = ['image_meta', 'image', 'gig']
        exclude = ['gig']
        