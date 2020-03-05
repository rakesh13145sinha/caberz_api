from django.contrib import admin
from django.contrib.auth.models import User
from accounts.models import Profiles,Driver,Journey
# Register your models here.
class ProfilesAdmin(admin.ModelAdmin):
    
    list_display=['user','first_name','last_name','mobile']
admin.site.register(Profiles,ProfilesAdmin)


class DriverAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','car','license_no']


admin.site.register(Driver,DriverAdmin)
admin.site.register(Journey)
