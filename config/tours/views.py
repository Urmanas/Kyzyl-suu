from django.shortcuts import render, get_object_or_404

from .models import Tour 

def tour_detail(request, id):
    tour = get_object_or_404(Tour, id=id)

    return render(request, 'tours/tour_detail.html', {
        'tour': tour
    })