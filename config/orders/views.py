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
            existing_people = sum(
    o.people for o in tour.orders.all()
)

            if existing_people + order.people > tour.max_people:
                form.add_error("people", "Not enough available spots for this tour.")
            else:
                order.save()

            return redirect("orders:order_success")
    else:
        form = OrderForm()

    return render(request, "orders/create_order.html", {
        "tour": tour,
        "form": form
    })

def order_success(request):
    return render(request, 'orders/order_success.html')
