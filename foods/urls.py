from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('food/<int:pk>/', views.food_detail, name='food_detail'),
    path('new/', views.food_create, name='food_create'),
]
