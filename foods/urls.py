from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('food/<int:pk>/', views.food_detail, name='food_detail'),
    path('new/', views.food_create, name='food_create'),
    path('del/<int:pk>/', views.food_delete, name='food_delete'),
    path('update/<int:pk>/', views.food_update, name='food_update'),
    path('serch/', views.search, name='search')
]
