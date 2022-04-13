from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:post_id>/',
         views.edit_post, name='edit_post'),
]
