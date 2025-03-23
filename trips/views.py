from django.shortcuts import render
from .models import Trip
from rest_framework import viewsets
from .serializers import TripSerializer
from .utils import generate_log_sheet

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def perform_create(self, serializer):
        trip = serializer.save()
        log_path = generate_log_sheet(trip.id)
        trip.log_sheet = log_path
        trip.save()
