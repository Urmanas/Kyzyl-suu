from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from tours.models import Tour 


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {
        'form': form
        })


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
