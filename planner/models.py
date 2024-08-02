from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#create a model for the recipe

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    day = models.CharField(max_length=100, default='something')
    name = models.CharField(max_length=100, default ='something')
    descrtiption = models.TextField(default='something')

