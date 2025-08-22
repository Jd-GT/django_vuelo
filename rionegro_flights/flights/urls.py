from django.urls import path
from . import views

urlpatterns = [
    path('flights/register/', views.register_flight, name='register_flight'),
    path('flights/', views.flight_list, name='flight_list'),
    path('flights/stats/', views.flight_stats, name='flight_stats'),
]