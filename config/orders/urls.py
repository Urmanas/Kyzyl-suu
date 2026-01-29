from django.urls import path
from .views import create_order

app_name = 'orders'

urlpatterns = [
    path("create/<int:tour_id>/", create_order, name="create_order"),
]
