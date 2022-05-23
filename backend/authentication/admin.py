from django.contrib import admin
from Posts.models import Posts
from .models import User
from Friends.models import FriendList, FriendRequest

# Register your models here.
admin.site.register(User)

class FriendListAdmin(admin.ModelAdmin):
    list_filter = ['user']
    list_display = ['user']
    search_fields = ['user']
    readonly_fields = ['user']

    class Meta:
        model = FriendList

admin.site.register(FriendList, FriendListAdmin)
admin.site.register(Posts)

# class FriendRequestAdmin(admin.ModelAdmin):
#     list_filter = ['sender', 'reciever']
#     list_display = ['sender', 'reciever']
#     search_fields = ['sender__username', 'sender__email', 'reciever__username', 'reciever__email']
    
    # class Meta:
    #     model = FriendRequest

