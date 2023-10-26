from django.urls import path
from .views import *

urlpatterns = [
    path('guestinfo/all/', GuestInfoApiView.as_view(), name='guestinfo'),
    path('guestinfo/<int:pk>/', GuestInfoIdApiView.as_view(), name='guestinfoid')
]