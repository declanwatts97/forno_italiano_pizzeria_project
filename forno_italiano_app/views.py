from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from .models import Booking
from django.shortcuts import render, redirect, get_object_or_404

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
            
                booking = form.save(commit=False)
                
                if request.user.is_authenticated:
                    booking.user = request.user  
                
                booking.save()
                
                messages.success(request, 'Your table has been booked successfully!')
                return redirect('booking_success')
            except Exception as e:
                
                messages.error(request, f"There was an error processing your booking: {e}")
        else:
            
            messages.error(request, 'Please correct the errors below.')
    else:
        
        form = BookingForm()
        
    context = {
        'form': form
    }
    return render(request, 'booking_form.html', context)

def booking_success(request):
    return render(request, 'booking_success.html')

def login (request):
    return render(request, 'account/login.html')

@login_required
def my_bookings(request):
    user_bookings = Booking.objects.filter(user=request.user).order_by('-date', '-time')
    context = {
        'bookings': user_bookings 
    }
    return render(request, "my_bookings.html", context)

@login_required
def booking_details(request, pk):
    
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    
    context = {
        'booking': booking
    }
    return render(request, 'booking_details.html', context)

@login_required
def cancel_booking(request, pk):
   
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    
    booking.delete()
    
    messages.success(request, f"Your reservation for {booking.date} at {booking.time} has been successfully cancelled.")
    
    return redirect('my_bookings') 

@login_required
def edit_booking(request, pk):
    
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    
    if request.method == 'POST':
    
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Your booking has been successfully updated!')
                return redirect('my_bookings')
            except Exception as e:
                messages.error(request, f"There was an error updating your booking: {e}")
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
    
        form = BookingForm(instance=booking)
        
    context = {
        'form': form,
        'editing': True,
        'booking_pk': pk
    }
    return render(request, 'booking_form.html', context)