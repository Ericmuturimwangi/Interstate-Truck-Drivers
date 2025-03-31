from django.db import models

# Create your models here.
class Trip(models.Model):
    current_location = models.CharField(max_length=255)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    current_cycle_hours = models.FloatField()

    created_at =models.DateTimeField(auto_now_add=True)
    log_sheet = models.ImageField(upload_to="logs/", blank=True, null=True)
    

    def __str__ (self):
        return f"Trip from {self.pickup_location} to {self.dropoff_location}"
    
class Route(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    route = models.TextField()
    distance = models.FloatField()
    duration = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f"Route for {self.trip}"
class ELDLog(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    cycle_hours = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"ELD Log for {self.trip}"
    