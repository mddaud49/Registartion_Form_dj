from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignForm,EditProfileForm,EditAdminForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

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
            messages.success(request,'Login successfully')
            return HttpResponseRedirect('/profile/')
   else:
      fm=AuthenticationForm()
   return render(request,'login.html',{'form':fm})
 else:
    return HttpResponseRedirect('/profile/')

def UserProfile(request):
   if request.user.is_authenticated:
    if request.method=='POST':
       if request.user.is_superuser=='TRUE':
          fm=EditAdminForm(request.POST,instance=request.user)
       else:
        fm=EditProfileForm(request.POST,instance=request.user)
       if fm.is_valid:
          messages.success(request,'Profile updated')
          fm.save()
    else:
     if request.user.is_superuser==True:
        fm=EditAdminForm(instance=request.user)
     else:
      fm=EditProfileForm(instance=request.user)
    return render(request,'profile.html',{'name':request.user.username,'form':fm})
   else:
      return HttpResponseRedirect('/login/')

def UserLogout(request):
   logout(request)
   return HttpResponseRedirect('/login/')

def Changepass(request):
 if request.user.is_authenticated:
   if request.method=='POST':
      fm=PasswordChangeForm(user=request.user,data=request.POST)
      if fm.is_valid():
         fm.save()
         update_session_auth_hash(request,fm.user)
         return HttpResponseRedirect('/profile/')
   else:
    fm=PasswordChangeForm(user=request.user)
   return render(request,'change.html',{'form':fm})
 else:
    return HttpResponseRedirect('/login/')
 
def Changepass1(request):
 if request.user.is_authenticated:
   if request.method=='POST':
      fm=SetPasswordForm(user=request.user,data=request.POST)
      if fm.is_valid():
         fm.save()
         update_session_auth_hash(request,fm.user)
         return HttpResponseRedirect('/profile/')
   else:
      fm=SetPasswordForm(user=request.user)
   return render(request,'change1.html',{'form':fm})
 else:
    return HttpResponseRedirect('/login/')

   
    


   
