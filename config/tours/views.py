from django.shortcuts import render, get_object_or_404, redirect
from .forms import TourForm
from .models import Tour 

def tour_detail(request, id):
    tour = get_object_or_404(Tour, id=id)

    return render(request, 'tours/tour_detail.html', {
        'tour': tour
    })


def tour_update(request, id):
    tour = get_object_or_404(Tour, id=id)

    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            form.save()
            return redirect('tour_detail', id=tour.id)

    else:
        form = TourForm(instance=tour)

    return render(request, 'tours/tour_form.html', {
        'form': form,
        'tour': tour
    })
