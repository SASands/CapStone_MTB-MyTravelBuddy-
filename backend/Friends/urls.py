from django.urls import path
from . import views


urlpatterns = [
    path('get_users/',views.get_all_users),
    path('get_user_by_id/<int:pk>/',views.get_user_by_id),
    path('view_friends/',views.get_friends_list),
    path('send_friend_request/<int:pk>/' ,views.send_friend_request),    
    path('approve_friend_request/<int:pk>/',views.approve_friend_request),
]