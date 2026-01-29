from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("full_name", "tour", "people", "created_at")
    list_filter = ("tour",)
