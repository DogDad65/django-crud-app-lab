from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bikes/', views.bike_index, name='bike_index'),
    path('add-category/', views.add_category, name='add_category'),
    path('bikes/<int:bike_id>/', views.bike_detail, name='bike_detail'),
    path('bikes/create/', views.create_bike, name='create_bike'),
    path('bikes/<int:bike_id>/update/', views.update_bike, name='update_bike'),
    path('bikes/<int:bike_id>/delete/', views.delete_bike, name='delete_bike'),
]
