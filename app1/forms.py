from django import forms

from app1.models import *


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password','last_name','first_name']

        widgets={'password':forms.PasswordInput}


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','Profile_pic']