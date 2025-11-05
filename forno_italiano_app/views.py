from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("this is the index page")

def menu(request):
    return HttpResponse("this is the menu page")

def our_restaurants(request):
    return HttpResponse("this is the our restaurants page")

def booking_form(request):
    return HttpResponse("this is the booking page")