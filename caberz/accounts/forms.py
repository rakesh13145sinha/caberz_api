from django import forms
from accounts.models import Profiles,Driver
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class Profileform(forms.ModelForm):
    class Meta:
        model=Profiles
        fields='__all__'
class DriverForm(forms.ModelForm):
    class Meta:
        model=Driver
        fields=('first_name','last_name','mobile','car','license_no','ownership_no')

class AdminFrom(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1", "password2"]