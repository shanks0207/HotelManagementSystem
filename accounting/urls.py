from django.urls import path
from .views import *

urlpatterns = [
    path('accounting/all/', AccountingApiView.as_view(), name='accounting'),
    path('billing/<int:pk>/', BillingApiView.as_view(), name='billing'),
    # path('group/all/', GroupApiView.as_view(), name = 'group' )
]