from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.db import models


# Create your models here.
class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bought_cars = models.ManyToManyField('cars.Car', blank=True)