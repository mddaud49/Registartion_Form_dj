from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

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

def UserLogin(request):
 if not request.user.is_authenticated:
   if request.method=="POST":
      fm=AuthenticationForm(request=request,data=request.POST)
      if fm.is_valid():
         uname=fm.cleaned_data['username']
         upass=fm.cleaned_data['password']
         user=authenticate(username=uname,password=upass)
         if user is not None:
            login(request,user)
            messages.success(request,'Login Successfully')
            return HttpResponseRedirect('/profile/')
   else:
      fm=AuthenticationForm()
   return render(request,'login.html',{'form':fm})
 else:
    return HttpResponseRedirect('/profile/')

def UserProfile(request):
   if request.user.is_authenticated:
    return render(request,'profile.html',{'name':request.user})
   else:
      return HttpResponseRedirect('/login/')

def UserLogout(request):
   logout(request)
   return HttpResponseRedirect('/login/')
    


   fm=AuthenticationForm()
   return render(request,'login.html',{'form':fm})
