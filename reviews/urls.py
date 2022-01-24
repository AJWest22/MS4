from django.urls import path
from . import views


urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('reviews/add/', views.add_review),
    path('reviews/add/<str:search_term>/', views.add_review),
]
