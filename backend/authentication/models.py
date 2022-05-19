from datetime import date
from django.db import models
from email.policy import default
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_employee = models.BooleanField('employee status', default=False)
    is_customer = models.BooleanField('customer status', default=False)
    pass

    '''
    This is a custom version of the built in User class
    It contains all of the built in fields and functionality of the standard User
    You can add fields here for any additional properties you want a User to have
    This is useful for adding roles (Customer and Employee, for example)
    For just a few roles, adding boolean fields is advised
    '''
    # Example (note import of models above that is commented out)
    # this will add a column to the user table
    # is_student = models.BooleanField('student status', default=False)

class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    user_since = models.DateField(date)

