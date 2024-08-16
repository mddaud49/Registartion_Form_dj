from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


class SignForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}

class EditProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','last_login','date_joined']
        labels={'email':'Email'}

class EditAdminForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields='__all__'
        labels={'email':'Email'}