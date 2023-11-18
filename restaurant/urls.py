from django.urls import path
from .views import *

urlpatterns = [
    path('menu/all/', MenuApiView.as_view(), name='menu'),
    path('menuitem/<int:pk>/', MenuItemApiView.as_view(), name='menuitem'),
    # path('group/all/', GroupApiView.as_view(), name = 'group' )
]
