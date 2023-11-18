from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    