from os import remove
from sqlite3 import Timestamp
from django.db import models;
from drf_jwt_backend import settings
from django.dispatch import receiver
from django.utils import timezone
from authentication.models import User
from authentication.serializers import serializers


# Create your models here.
   
   
#make a friends class and tie it into serializaers

# class User(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=250)
#     last_name = models.CharField(max_length=250)
#     country = models.CharField(max_length=250)

class FriendList(models.Model):  
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="friends")

    def __str__(self):
        return self.user.username

    def add_friend(self, account):
        """Add a new Travel Buddy"""
        if not account in self.friends.all():
            self.friends.add(account)
            self.save()
    
    def remove_friend(self, account):
        """Remove a Travel Buddy"""
        if account in self.friends.all():
            self.friends.remove(account)
            self.save

    def unfriend(self, removee):
        """Initiation of Actually unfriending someone"""
        remover_friends_list = self
        remover_friends_list.remove_friend(remove)
        friends_list = FriendList.objects.get(user=removee)
        friends_list.remove_friend(self.user)

    def is_mutual_friend(self, friend):
        """Is this already a friend"""
        if friend in self.friends.all():
            return True
        else:
            return False


class FriendRequest(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reciever")
    is_active = models.BooleanField(blank=True, null=False, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.sender.username
    def accept(self):
        receiver_friends_list = FriendList.objects.get(user=self.receiver)
        if receiver_friends_list:
           receiver_friends_list.add_friend(self.sender)
           sender_friends_list = FriendList.objects.get(user=self.sender)
        if sender_friends_list:
            sender_friends_list.add_friend(self.receiver)
            self.is_active = False
            self.save()

    def decline_friend_request(self):
        self.is_active = False
        self.save()

    def cancel_my_friend_request(self):
        self.is_active = False
        self.save



    


