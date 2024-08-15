from django.shortcuts import render
from .forms import StuForm
from .models import StuModel
from django.contrib import messages

# Create your views here.
def Info(request):
    if request.method=='POST':
        fm=StuForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'DATA SAVED')
            messages.info(request,'NOW YOU CAN LOGIN')
            messages.warning(request,'warning')
            messages.error(request,'it is an error')
            print(messages.get_level(request))
            messages.debug(request,' your 1st debug ')
            messages.set_level(request,messages.DEBUG)
            messages.debug(request,' your 1st debug ')
            print(messages.get_level(request))
            
    else:
        fm=StuForm()
    return render(request,'user.html',{'form':fm})
