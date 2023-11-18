from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name = 'login'),
    path('register/', register, name = 'login'),
    path('user/all/', UserApi.as_view(), name = 'user')
]