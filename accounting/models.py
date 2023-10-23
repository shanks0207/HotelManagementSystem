from django.db import models
from frontdesk.models import *

# Create your models here.

class Bill(models.Model):
    guest = models.ForeignKey(GuestInfo, on_delete=models.CASCADE)
    total_amount = models.FloatField()

class payment(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    paild_amount = models.FloatField()
