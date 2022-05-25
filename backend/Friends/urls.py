from django.urls import path
from . import views


urlpatterns = [
    path('view_friends/',views.friends_list),
    path('get_users/',views.get_all_users),
    path('get_user_by_id/<int:pk>/',views.get_user_by_id),    
]