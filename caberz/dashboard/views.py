from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
import requests
from django.urls import reverse,reverse_lazy
from  accounts.models import Driver,Profiles,Journey

from django.contrib.auth.decorators import login_required




# def index(request):
#     if request.session.has_key('is_login'):
#         request.session.set_expiry(300)
#         return render(request,'templates/dashboard/index.html')
#     
#     return redirect('login')

@login_required
def index(request):
    Number_of_driver=Driver.objects.all()
    driver_count=Number_of_driver.count()
    destination=Journey.objects.all()
    return render(request,'templates/dashboard/index.html',{'driver_count':driver_count,'destination':destination})
@login_required
def remove_from_list(request,id):
    try:
        destination=Journey.objects.get(id=id)
        destination.delete()
    except:
        HttpResponse(redirect('<h1>there is no driver record</h1>'))
    return HttpResponseRedirect(reverse('home'))
    



@login_required
def chart_view(request):
    return render(request,'templates/dashboard/charts.html')
@login_required
def driver_tracking_view(request):
    return render(request,'templates/dashboard/driver-tacking.html')
@login_required   
def inbox_view(request):
    return render(request,'templates/dashboard/inbox.html')
@login_required
def layout_static_view(request):
    return render(request,'templates/dashboard/layout-static.html')

@login_required
def offers_view(request):
    return render(request,'templates/dashboard/layout-static.html')





def map(request):
    return render (request,'templates/social/home')





