from django.shortcuts import render, redirect, get_object_or_404
from tours.models import Tour
from .forms import OrderForm

def create_order(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.tour = tour
            order.save()
            return redirect("order_success")
    else:
        form = OrderForm()

    return render(request, "orders/create_order.html", {
        "tour": tour,
        "form": form
    })
