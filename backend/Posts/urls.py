from django.urls import path;
from . import views

urlpatterns = [
    path('all/',views.get_all_posts_list),
    path('get_post_by_id/<int:pk>/', views.get_post_by_id),
    path('create/', views.create_post),
    path('delete/<int:pk>/', views.post_delete),
    path('patch/<int:pk>/', views.post_patch)

]