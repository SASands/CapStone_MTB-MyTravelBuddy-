from django.db import models
from authentication.models import User



class FriendList(models.Model):  
    request_receiver = models.ForeignKey(User, related_name="request_receiver", on_delete=models.CASCADE)
    request_sender = models.ForeignKey(User, related_name="request_sender", on_delete=models.CASCADE)
    



class FriendRequest(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="reciever", on_delete=models.CASCADE)
    is_active = models.BooleanField(blank=True, null=False, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)



    


