from django.urls import path;
from . import views

urlpatterns = [
    path('all/',views.get_all_posts_list),
    path('details/', views.post_detail),
    path('create/', views.create_post),
]