from django.urls import path
from .views import restapiview

urlpatterns=[
   path('restapiviews/<int:id>/', restapiview.as_view(), name='home')
]