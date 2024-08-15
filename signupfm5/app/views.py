from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import SignForm
from django.contrib import messages

# Create your views here.
def Signup(request):
    if request.method=='POST':
        fm=SignForm(request.POST)
        if fm.is_valid():
            messages.success(request,'FORM SUCCESSFULLY COMPLETED')
            fm.save()
            fm=SignForm()
    else:
     fm=SignForm()
    return render(request,'signup.html',{'form':fm})
