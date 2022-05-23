from django.db import models
from rest_framework.decorators import api_view, permission_classes
from authentication.models import User 

# Create your models here.

class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=5000)

