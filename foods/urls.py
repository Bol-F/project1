from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.FoodListView.as_view(), name='food_list'),
    path('create/', views.FoodCreateView.as_view(), name='food_create'),
    path('food/<int:pk>/', views.FoodDetailView.as_view(), name='food_detail'),
    path('del/<int:pk>/', views.FoodDeleteView.as_view(), name='food_delete'),
    path('update/<int:pk>/', views.FoodUpdateView.as_view(), name='food_update'),
    path('search/', views.FoodSearchView.as_view(), name='food_search')

    # path('', views.food_list, name='food_list'),
    # path('food/<int:pk>/', views.food_detail, name='food_detail'),
    # path('new/', views.food_create, name='food_create'),
    # path('del/<int:pk>/', views.food_delete, name='food_delete'),
    # path('update/<int:pk>/', views.food_update, name='food_update'),
    # path('serch/', views.search, name='search')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
