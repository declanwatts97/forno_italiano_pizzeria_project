from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm
# Create your views here.

def home(request):
    return render(request, "home.html")

def menu(request):
    return render(request, "menu.html")

def our_restaurants(request):
    return render(request, "our_restaurants.html")

def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Your table has been booked successfully!')
                return redirect('booking_success')
            except Exception as e:
                messages.error(request, str(e))
    else:
        form = BookingForm()

    return render(request, 'booking_form.html', {'form': form})

def booking_success(request):
    return render(request, 'booking_success.html')