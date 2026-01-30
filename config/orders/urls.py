from django.urls import path
from .views import create_order, order_success

app_name = 'orders'

urlpatterns = [
    path("create/<int:tour_id>/", create_order, name="create_order"),
    path('success/', order_success, name='order_success'),
]
