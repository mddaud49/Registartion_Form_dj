from django import forms
from .models import StuModel

class StuForm(forms.ModelForm):
    class Meta:
        model=StuModel
        fields=['name','email','password']
        widgets={'password':forms.PasswordInput}