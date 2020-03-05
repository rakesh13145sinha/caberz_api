from django.urls import path
from dashboard import views
urlpatterns=[
    #path('social/',views.map,name='map'),
    path('home/',views.index,name='home'),
    path('charts/', views.chart_view, name="charts"),
    path('tracking/', views.driver_tracking_view, name="driver_tracking"),
    path('inbox/', views.inbox_view, name="inbox"),
    path('layout/', views.layout_static_view, name="layout"),
    path('offer/',views.offers_view,name="offers"),
    path('remove/<int:id>/',views.remove_from_list,name="remove")


    


]   