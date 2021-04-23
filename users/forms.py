from django.db.models import fields
from users.models import Profile
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import (
    authenticate, 
    get_user_model, 
    password_validation,
)
from django.contrib.auth.forms import UsernameField
from django.core.validators import validate_email, ValidationError
from django.utils.translation import gettext, gettext_lazy as _
import re

User = get_user_model()

class UserRegisterForm(forms.ModelForm):

    """ Prams """
    # List of error messages
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
        'email_in_use': _('Email is already in use'),
        'phone_number_in_use':_('Phone number is already in use'),
        'phone_number_invalid':_('Phone number is invalid'),
        'user_name_in_use':_('Username is already in use'),
        'user_name_invalid':_('Username invalid'),
    }

    class Meta:
        model = User
        fields = ('email','user_name','phone_number','first_name','last_name')

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    """ Prams """

    # Validate passwords and check for mismatch
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    # Validate email and check for availability
    def clean_email(self):
        # extract email from form data
        email = self.cleaned_data['email']
        validate_email(email)
        if User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError(self.error_messages['email_in_use'],code='email_in_use')
        return email.lower()

    # Validate username and check for availability
    def clean_user_name(self):
        user_name = self.cleaned_data['user_name']
        # init a username pattern
        ## Only starts and ends with char or number
        ## Has 8-20 characters
        ## Only _ and __ are allowed
        user_name_pattern = re.compile(r"^(?=[a-zA-Z0-9_]{5,20}$)(?!.*_{3})[^_].*[^_]$")
        if not re.search(user_name_pattern,user_name):
            raise forms.ValidationError(self.error_messages['user_name_invalid'],code='user_name_invalid')
        if User.objects.filter(user_name=user_name).count() > 0:
            raise forms.ValidationError(self.error_messages['user_name_in_use'],code='user_name_in_use')
        return user_name

    # Validate phonenumber and check for availability
    def clean_phone_number(self):
        # extract phonenumber from form data
        phone_number = self.cleaned_data['phone_number']
        # init a phone number pattern
        phone_number_pattern = re.compile(r"^09\d{9}$") # 09([0-9]*9)
        # check for validation
        if not re.search(phone_number_pattern, phone_number):
            raise forms.ValidationError(self.error_messages['phone_number_invalid'],code='phone_number_invalid')
        if User.objects.filter(phone_number=phone_number).count() > 0:
            raise forms.ValidationError(self.error_messages['phone_number_in_use'],code='phone_number_in_use')
        return phone_number

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
class UserEditForm(forms.ModelForm):
    #we need to add input validation 
    class Meta:
        model = User
        fields = ('user_name','phone_number','first_name','last_name')

 #we need to add input validation 
class ProfileEditForm(forms.ModelForm):
    profile_pic = forms.ImageField()
    class Meta:
        model = Profile
        fields = ('profile_pic', 'id_number', 'degree', 'address')
        