from django import forms
from django.contrib.auth.models import User
from django.core import validators
from captcha.fields import CaptchaField

def validate_password(value):

    if len(value) < 4:

        raise forms.ValidationError('Password too short!! Please enter again!')

    if value.isalnum():

        raise forms.ValidationError('Password must be alphanumeric! Please Try again!')


class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput, validators = [validate_password])

    captcha = CaptchaField()

    class Meta:

        model = User

        fields = ('first_name','last_name','username','captcha','password')
