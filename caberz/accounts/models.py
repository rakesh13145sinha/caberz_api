from django.db import models
from django.contrib.auth.models import User
from datetime import date,datetime
from django.urls import reverse




class Profiles(models.Model):
    user            =models.CharField(max_length=50,blank=False,default="username")
    first_name      =models.CharField(max_length=50,blank=False,default="")
    last_name       =models.CharField(max_length=50,blank=False,default="last_name")
    email           =models.EmailField(max_length=50,blank=False,default="email")
    password1       =models.CharField(max_length=20,blank=False,default="")
    password2       =models.CharField(max_length=20,blank=False,default="")
    mobile          =models.IntegerField(blank=False,default=+91)
    otp             =models.IntegerField(blank=False,default=123456)
    s_latitude      =models.FloatField()
    s_logitude      =models.FloatField()
    total_ride      =models.IntegerField(default=0)
    def __str__(self):
        return self.first_name
    

    
class Driver(models.Model):
    first_name         =models.CharField(max_length=100,blank=False,default="driver")
    last_name          =models.CharField(max_length=50,blank=False,default="driver_last")
    mobile             =models.IntegerField(default=+91)
    car                =models.CharField(max_length=50,)
    license_no         =models.ImageField(upload_to='media/license',blank=False)
    ownership_no       =models.ImageField(upload_to='media/ownership',blank=False)
    timestamp          =models.DateTimeField(auto_now=False ,auto_now_add=True)
    update             =models.DateTimeField(auto_now=True,auto_now_add=False)
    active             =models.BooleanField(default=True)
    otp                =models.IntegerField(blank=False,default=123456)

    s_latitude         =models.FloatField(max_length=50, blank=True,null=True)
    s_logitude         =models.FloatField(max_length=50, blank=True,null=True)
    rate               =models.FloatField(max_length=50, blank=True,null=True)
    price              =models.FloatField(max_length=50, blank=True,null=True)

    def __str__(self):
        return self.first_name

class Vehicle(models.Model):
    ECONOMY = 'EC'
    PRIME = 'PR'
    EXTRA_LARGE= 'XL'
    VEHECLES_CHOICES = [
        (ECONOMY, 'Economy'),
        (PRIME, 'Prime'),
        (EXTRA_LARGE, 'Extra_large'),
    ]
    driver              =models.ForeignKey(Driver,on_delete=models.CASCADE)
    vehicle_name        =models.CharField(max_length=50, blank=False)
    vehicle_type        =models.CharField(max_length=50,choices=VEHECLES_CHOICES, blank=False)
    vehecle_number      =models.CharField(max_length=50, blank=False)
    vehicle_dimension   =models.CharField(max_length=50, blank=False)
    timestamp           =models.DateTimeField(auto_now=False ,auto_now_add=True)
    update              =models.DateTimeField(auto_now=True,auto_now_add=False)
    active              =models.BooleanField(default=True)


class Driver_vehicle(models.Model):
    vehicle_type        =models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    driver_name         =models.ForeignKey(Driver,on_delete=models.CASCADE)
    timestamp           =models.DateTimeField(auto_now=False ,auto_now_add=True)
    update              =models.DateTimeField(auto_now=True,auto_now_add=False)
    active              =models.BooleanField(default=True)


class Journey(models.Model):
    ECONOMY = 'EC'
    PRIME = 'PR'
    EXTRA_LARGE= 'EL'
    CAR_CHOICES = [
        (ECONOMY, 'Economy'),
        (PRIME, 'Prime'),
        (EXTRA_LARGE, 'Extra_large'),
     
        
    ]
    CASH='CASH'
    UPI='UPI'
    NETBANKING='NETBANING'
    PAYMENT=[
        (CASH,'Cash'),
        (UPI,'Upi'),
        (NETBANKING,'Netbanking')
    ]



    driver           =models.ForeignKey(Driver,on_delete=models.CASCADE)
    customer         =models.ForeignKey(Profiles,on_delete=models.CASCADE)
    source           =models.CharField(max_length=50, blank=False)
    s_latitude       =models.IntegerField()
    s_logitude       =models.IntegerField()

    destination      =models.CharField(max_length=50, blank=False )
    d_logitude       =models.IntegerField()
    d_latitude       =models.IntegerField()

    luxury           =models.CharField(max_length=2,choices=CAR_CHOICES,default=PRIME)    
    payment_mode     =models.CharField(max_length=50,choices=PAYMENT)
    rating           =models.IntegerField()
    timestamp        =models.DateTimeField(auto_now=False ,auto_now_add=True)
    update           =models.DateTimeField(auto_now=True,auto_now_add=False)
    active           =models.BooleanField(default=True)
    def get_absolute__url(self):
        return reverse('home',kwargs={'id':self.id})
    