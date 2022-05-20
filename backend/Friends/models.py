from django.db import models;
from authentication.models import User;


# Create your models here.
   
   
#make a friends class and tie it into serializaers

class Friends(models.Model):
    friends = models.ManyToManyField(User)
