from django.urls import path
from .views import (
    home,
    BikeListView, BikeDetailView, BikeCreateView, BikeUpdateView, BikeDeleteView, 
    add_maintenance, add_category,
    UpgradeListView, UpgradeDetailView, UpgradeCreateView, UpgradeUpdateView, UpgradeDeleteView
)

urlpatterns = [
    path('', home, name='home'),
    path('bikes/', BikeListView.as_view(), name='bike_index'),
    path('bikes/create/', BikeCreateView.as_view(), name='create_bike'),  # Use the class-based view here
    path('bikes/<int:pk>/', BikeDetailView.as_view(), name='bike_detail'),
    path('bikes/<int:pk>/update/', BikeUpdateView.as_view(), name='bike_update'),
    path('bikes/<int:pk>/delete/', BikeDeleteView.as_view(), name='bike_delete'),
    path('bikes/<int:bike_id>/add-maintenance/', add_maintenance, name='add_maintenance'),
    path('add-category/', add_category, name='add_category'),

    # Routes for managing upgrades
    path('upgrades/', UpgradeListView.as_view(), name='upgrade_list'),
    path('upgrades/create/', UpgradeCreateView.as_view(), name='upgrade_create'),
    path('upgrades/<int:pk>/', UpgradeDetailView.as_view(), name='upgrade_detail'),
    path('upgrades/<int:pk>/update/', UpgradeUpdateView.as_view(), name='upgrade_update'),
    path('upgrades/<int:pk>/delete/', UpgradeDeleteView.as_view(), name='upgrade_delete'),
]

