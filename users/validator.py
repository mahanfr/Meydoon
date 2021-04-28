from django.core.validators import validate_email, ValidationError
from django.utils.translation import gettext, gettext_lazy as _
import re

error_messages = {
    'phone_number_invalid':_('Phone number is invalid'),
    'user_name_invalid':_('Username invalid'),
}

def validate_phone_number(phone_number):
    phone_number_pattern = re.compile(r"^09\d{9}$") # 09([0-9]*9)
    # check for validation
    if not re.search(phone_number_pattern, phone_number):
        raise ValidationError(error_messages['phone_number_invalid'],code='phone_number_invalid')

def validate_username(user_name):
    # init a username pattern
    ## Only starts and ends with char or number
    ## Has 8-20 characters
    ## Only _ and __ are allowed
    user_name_pattern = re.compile(r"^(?=[a-zA-Z0-9_]{5,20}$)(?!.*_{3})[^_].*[^_]$")
    if not re.search(user_name_pattern,user_name):
        raise ValidationError(error_messages['user_name_invalid'],code='user_name_invalid')