from django.urls import path 
from .views import tour_detail, tour_update, tour_delete

app_name = 'tours'


urlpatterns = [
    path('<int:id>/', tour_detail, name='tour_detail'),
    path('<int:id>/edit/', tour_update, name='tour_update'),
    path('<int:id>/delete/', tour_delete, name='tour_delete'),
]