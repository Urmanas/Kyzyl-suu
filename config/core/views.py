from django.shortcuts import render
from tours.models import Tour 


def home(request):
    tours = Tour.objects.all()
    return render(request, 'core/home.html', {
        'tours': tours
    })

def tour_list(request):
    tours = Tour.objects.all()
    return render(request, 'core/tour_list.html', {
        'tours': tours
    })

def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')
