from django.shortcuts import render,redirect,HttpResponse
from accounts.forms import Profileform,DriverForm,AdminFrom
from django.contrib import messages
from django.contrib.auth.models import User,auth
from accounts.models import Profiles,Driver,Journey
from rest_framework.parsers import JSONParser ,FormParser , MultiPartParser
import json
import requests
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.contrib.auth import logout
from rest_framework import generics
from .serializers import UserSerializer,DriverSerializer,JourneySerializer,DriverSerializer,ProfileSerializer,OtpSerializer,DriverMobileSerializer,DriverOtpSerializer

from django.contrib.auth.forms import UserCreationForm
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,parser_classes
from rest_framework.response import Response
from rest_framework import permissions





'''CUSTOMER LOGIN BY OTP WITHOUT API VIEWS'''
def customer_login(request):
    if request.method=='POST':
        mobile_no=request.POST['mobile_no']
        user=Profiles.objects.filter(mobile=mobile_no).exists()
        if user:
           response=requests.get('https://2factor.in/API/V1/e2620bdd-53bb-11ea-9fa5-0200cd936042/SMS/'+mobile_no+'/AUTOGEN')
           data = response.json()
           request.session['otp_session_data']=data['Details']
           return redirect('otp')
        else:
            return HttpResponse('No such mobile no exist:-'+mobile_no+'sorry')
    else:   
        return render(request,'registration/login.html')
    return render(request,'registration/login.html')


''' OTP AUTHENTICATION AND MATCH NORMAL VIEWS'''
def otp(request):
   
    if request.method=='POST':
        password=request.POST['otp']
        request.session['otp_session_data']
        response = requests.get('https://2factor.in/API/V1/e2620bdd-53bb-11ea-9fa5-0200cd936042/SMS/VERIFY/'+ request.session['otp_session_data'] +'/'+ password +'')	
        data = response.json()
        if data['Status'] == "Success":
            return redirect('home')
        else:
            return redirect('login')
    return render(request,'registration/otp-module.html')



#======================================customer login with otp =========================================
'''GET ONE PASSENGER DETAIL''' 
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def profiles_detail(request,id):
    if request.method == 'GET':
        snippets = Profiles.objects.filter(id=id)
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)


'''ADD PASSENGER '''
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def profiles_post(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




'''PASSENGER LOGIN OTP'''
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def passenger_login(request):
    if request.method=='POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            mobile_no=request.data
            result=json.dumps(mobile_no)
            number=result[12:22]
            response=requests.get('https://2factor.in/API/V1/e2620bdd-53bb-11ea-9fa5-0200cd936042/SMS/'+number+'/AUTOGEN')
            data = response.json()
            print(data)
            request.session['otp_session_data']=data['Details']
            return Response(serializer.data, status=status.HTTP_201_CREATED)
     
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''ENTER OTP FOR AUTHENTICATION BY PASSENGER'''   
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def customer_otp(request):
    if request.method=='POST':
        serializer = OtpSerializer(data=request.data)
        if serializer.is_valid():
            request.session['otp_session_data']
            otp=request.data
            result=json.dumps(otp)
            number=result[9:15]
            print(number)
            response = requests.get('https://2factor.in/API/V1/e2620bdd-53bb-11ea-9fa5-0200cd936042/SMS/VERIFY/'+ request.session['otp_session_data'] +'/'+ number +'')
            data = response.json()
            print(data)
            if data['Status'] == "Success":
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          

#=====================================FOR ADD DRIVER WITHOUT API VIEWS =============================================
''' ADD NEW DRIVER WITHOUT API VIEWS'''

def driver(request):
    if request.method=='POST':
        dform=DriverForm(request.POST,request.FILES)

        if dform.is_valid():
            dform.save()
            return HttpResponse('submit')
    else:
        dform=DriverForm()
    return render(request,'templates/accounts/driver.html',{'dform':dform})

#===========================FOR DRIVER API VIEW============================================
''' GET PARTICULAR DRIVER DETAIL'''
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def driver_list(request,id):
    if request.method == 'GET':
        snippets = Driver.objects.filter(id=id)
        serializer =  DriverSerializer(snippets, many=True)
        return Response(serializer.data)



'''ADD NEW DRIVER THROUGH THE API'''
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
@parser_classes((JSONParser,FormParser , MultiPartParser))
def driver_signup(request):
    if request.method == 'POST':
        serializer =  DriverSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''GET OTP ON MOBILE FOR DRIVER '''
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def driver_login(request):
    if request.method=='POST':
        serializer = DriverMobileSerializer(data=request.data)
        if serializer.is_valid():
            mobile_no=request.data
            result=json.dumps(mobile_no)
            number=result[12:22]
            response=requests.get('https://2factor.in/API/V1/e2620bdd-53bb-11ea-9fa5-0200cd936042/SMS/'+number+'/AUTOGEN')
            data = response.json()
            print(data)
            request.session['otp_session_data']=data['Details']
            return Response(serializer.data, status=status.HTTP_201_CREATED)
     
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''ENTER OTP BY THE DRIVER'''
api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def driver_otp(request):
    if request.method=='POST':
        serializer = DriverOtpSerializer(data=request.data)
        if serializer.is_valid():
            request.session['otp_session_data']
            otp=request.data
            result=json.dumps(otp)
            number=result[9:15]
            print(number)
            response = requests.get('https://2factor.in/API/V1/e2620bdd-53bb-11ea-9fa5-0200cd936042/SMS/VERIFY/'+ request.session['otp_session_data'] +'/'+ number +'')
            data = response.json()
            print(data)
            if data['Status'] == "Success":
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






# ==================JOURNEY DETAIL=================================================
'''GET DETAIL ABOUT JOURNEY'''
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def journey_get(request,id):
    if request.method == 'GET':
        snippets = Journey.objects.filter(id=id)
        serializer = JourneySerializer(snippets, many=True)
        return Response(serializer.data)


'''ADD NEW JOURNEY'''
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def journey_post(request):
    if request.method == 'POST':
        serializer = JourneySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




''' for admin part only code'''

#=====================SIGNUP FOR ADMIN AUTHENTICATION===================

def signupAdmin(request):
    if request.method=='POST':
        form=AdminFrom(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
    else:
          form=AdminFrom()
    return render(request,'templates/accounts/register.html',{'form':form})

#=====================LOGOUT FOR ADMIN======================================
def logout_view(request):
    auth.logout(request)
    return redirect('admin')

# ===========================LOGOUT FOR ADMIN=============================
def login_admin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['is_lgoin']=True
            return redirect('home')
            
        else:
            return redirect('admin')
    else:
        return render(request,'templates/dashboard/login.html')
    return render(request,'templates/dashboard/login.html')