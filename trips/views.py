from django.shortcuts import render
from .models import Trip
from rest_framework import viewsets
from .serializers import TripSerializer
from .utils import generate_log_sheet
from django.http import JsonResponse

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def perform_create(self, serializer):
        trip = serializer.save()
        log_path = generate_log_sheet(trip.id)
        trip.log_sheet = log_path
        trip.save()


def get_route_details(request, route_id):
    try:
        route = Route.objects.get(id=route_id)
        data = {
            'pickup': route.pickup,
            'dropoff': route.dropoff,
            'cycle': route.cycle,
            # Add other fields as necessary
        }
        return JsonResponse(data)
    except Route.DoesNotExist:
        return JsonResponse({'error': 'Route not found'}, status=404)