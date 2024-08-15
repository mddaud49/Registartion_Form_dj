from django.contrib import admin
from .models import StuModel

# Register your models here.
@admin.register(StuModel)
class StuAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')
