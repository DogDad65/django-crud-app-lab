from django.urls import path
from .views import BikeListView, BikeDetailView, BikeCreateView, BikeUpdateView, BikeDeleteView, add_maintenance, add_category

urlpatterns = [
    path('', BikeListView.as_view(), name='bike_index'),
    path('create/', BikeCreateView.as_view(), name='create_bike'),
    path('<int:pk>/', BikeDetailView.as_view(), name='bike_detail'),
    path('<int:pk>/update/', BikeUpdateView.as_view(), name='bike_update'),
    path('<int:pk>/delete/', BikeDeleteView.as_view(), name='bike_delete'),
    path('<int:bike_id>/add-maintenance/', add_maintenance, name='add_maintenance'),
    path('add-category/', add_category, name='add_category'),  # Add this line
]
