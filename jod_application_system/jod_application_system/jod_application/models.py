from django.db import models

# Create your models here.
class JodApplication(models.Model):
    STATUS_CHOICES = [
        ('standard', 'ต้องการบริกร 1-2 คน'),
        ('premium', 'ต้องการบริกร 3-4 คน'),
        ('super premium', 'ต้องการบริกร 5-6 คน'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    room_type = models.CharField(max_length=100)
    room_size = models.CharField(max_length=100)
    set_food = models.CharField(max_length=100)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    application_status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='waiting') 

    def __str__(self):
        return f'{self.first_name} {self.phone_number} - {self.set_food} {self.booking_date} {self.booking_time} {self.application_status}'