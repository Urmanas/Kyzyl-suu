from django.urls import path 

from .views import home, tour_list, about, contact, signup

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('tours/', tour_list, name='tour_list'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('signup/', signup, name='signup'),
]