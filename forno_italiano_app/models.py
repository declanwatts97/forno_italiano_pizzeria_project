from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('date', 'time')  

    def clean(self):
        
        if Booking.objects.exclude(pk=self.pk).filter(date=self.date, time=self.time).exists():
            raise ValidationError("Please note we are a small family business so will only be accepting staggered bookings at this time.")

    def __str__(self):
        return f"{self.full_name} - {self.date} {self.time}"