from orders.models import Order
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
from users.validator import validate_phone_number, validate_username
from django.utils.translation import gettext, gettext_lazy as _
from datetime import datetime

User = get_user_model()


class UserRegisterForm(forms.ModelForm):

    """Prams"""

    # List of error messages
    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
        "email_in_use": _("Email is already in use"),
    }

    class Meta:
        model = User
        fields = ("email", "user_name", "phone_number", "first_name", "last_name")

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
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
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2

    # Validate email and check for availability
    def clean_email(self):
        # extract email from form data
        email = self.cleaned_data["email"].lower()
        validate_email(email)
        if User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError(self.error_messages["email_in_use"], code="email_in_use")
        return email

    # Validate username and check for availability
    def clean_user_name(self):
        user_name = self.cleaned_data["user_name"]
        validate_username(user_name)
        if User.objects.filter(user_name=user_name).count() > 0:
            raise forms.ValidationError(self.error_messages["user_name_in_use"], code="user_name_in_use")
        return user_name

    # Validate phonenumber and check for availability
    def clean_phone_number(self):
        # extract phonenumber from form data
        phone_number = self.cleaned_data["phone_number"]
        validate_phone_number(phone_number)
        if User.objects.filter(phone_number=phone_number).count() > 0:
            raise forms.ValidationError(self.error_messages["phone_number_in_use"], code="phone_number_in_use")
        return phone_number

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserEditForm(forms.ModelForm):

    error_messages = {
        "user_name_in_use": _("Username is already in use"),
        "phone_number_in_use": _("Phonenumber is already in use"),
    }

    class Meta:
        model = User
        fields = ("user_name", "phone_number", "first_name", "last_name")

    def clean_user_name(self):
        user_name = self.cleaned_data["user_name"]
        validate_username(user_name)
        user_name_exists = User.objects.filter(user_name=user_name).exclude(id=self.instance.id)
        if self.instance and self.instance.id and user_name_exists:
            raise forms.ValidationError(self.error_messages["user_name_in_use"], code="user_name_in_use")
        return user_name

    # Validate phonenumber and check for availability
    def clean_phone_number(self):
        # extract phonenumber from form data
        phone_number = self.cleaned_data["phone_number"]
        validate_phone_number(phone_number)
        phone_number_exists = User.objects.filter(phone_number=phone_number).exclude(id=self.instance.id)
        if self.instance and self.instance.id and phone_number_exists:
            raise forms.ValidationError(self.error_messages["phone_number_in_use"], code="phone_number_in_use")
        return phone_number


# we need to add input validation
class ProfileEditForm(forms.ModelForm):
    profile_pic = forms.ImageField(required=False)
    birthday = forms.DateField(
        required=False, widget=forms.SelectDateWidget(years=[x for x in range(1970, datetime.now().year + 1)])
    )

    class Meta:
        model = Profile
        fields = ("profile_pic", "national_id", "bank_number", "address", "bio")
