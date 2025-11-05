from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "home.html")

def menu(request):
    return render(request, "menu.html")

def our_restaurants(request):
    return render(request, "our_restaurants.html")

def booking_form(request):
    return render(request, "booking_form.html")