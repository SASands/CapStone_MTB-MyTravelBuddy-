from django.urls import path
from . import views


urlpatterns = [
    path('',views.friends_list),
    path('all/',views.get_all_users),
    path('',views.get_user_by_id),    
]