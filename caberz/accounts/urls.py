from django.urls import path,include
from accounts import views


urlpatterns=[

 #=====================ADMIN SIGNUP ,LOGIN,LOGOUT -==========================
    
    path('signup-admin/',views.signupAdmin,name='sign'),
    path('login/admin/',views.login_admin,name='admin'),
    path('logout/',views.logout_view,name="logout"),
   
#=============================PASSENGER ========================================
    path('otp/',views.otp,name='otp'),
    path('login/',views.customer_login,name='login'),# ENTER MOBILE NUMBER FORM 

#========================ADD DRIVER FORM==========================================

   path('driver/',views.driver),#DRIVER SIGNUP FORM
    
#=============================PASSENGER API VIEWS FOR SIGNUP,LOGIN===================================
    path('api/profile/get/<int:id>',views.profiles_detail,name='profile-get'),
    path('api/profile/post/',views.profiles_post,name="list"),
    path('api/passenger/login/',views.passenger_login,name='customer_login_otp'),
    path('api/passenger/login/otp/',views.customer_otp,name='otp_login'),

#=======================DRIVER API VIEWS FOR LOGIN ,SIGNUP,DETAIL==============================================
    path('api/driver/get/<int:id>',views.driver_list,name='driver list'),
    path('api/driver/signup/',views.driver_signup,name="driver-signup"),
    path('api/driver/login/',views.driver_login,name='driver_login'),
    path('api/driver/otp/',views.driver_otp,name='driver_otp'),

#=================================JOURNEY DETAIL=================================
    path('api/journey/get/<int:id>',views.journey_get,name='journey-get'),
    path('api/journey/post/',views.journey_post,name='journey-post'),
   

    
    

]
