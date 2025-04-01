from django.shortcuts import render
from .models import Trip
from rest_framework import viewsets
from .serializers import TripSerializer
from .utils import generate_log_sheet
from django.http import JsonResponse
from rest_framework import generics
from .models import Route, ELDLog
from .serializers import RouteSerializer,   ELDLogSerializer, RouteSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def perform_create(self, serializer):
        trip = serializer.save()
        log_path = generate_log_sheet(trip.id)
        trip.log_sheet = log_path
        trip.save()

@method_decorator(csrf_exempt, name='dispatch')
class RouteCreateView(generics.CreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

@method_decorator(csrf_exempt, name='dispatch')
class RouteDetailView(generics.RetrieveAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
@method_decorator(csrf_exempt, name='dispatch')
class ELDLogCreateView(generics.CreateAPIView):
    queryset = ELDLog.objects.all()
    serializer_class = ELDLogSerializer