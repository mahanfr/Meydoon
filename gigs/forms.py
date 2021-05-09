from django import forms
from .models import Gig, Plan, ShowcaseImage,Comment

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
    image = forms.ImageField(required=False)
    class Meta:
        model = ShowcaseImage
        fields = ['image']
        exclude = ['gig']

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea, max_length=400, required=False)
    class Meta:
        model = Comment
        fields = ['title', 'body']
        exclude = ['gig','user', 'is_aproved']
                
class PlanForm(forms.ModelForm):
    """
    Form for add Plans 
    """
    class Meta:
        model = Plan
        fields = ['title', 'price', 'feature_list']
        exclude = ['gig']                
    