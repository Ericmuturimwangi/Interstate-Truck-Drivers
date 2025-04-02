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
from rest_framework.response import Response
@method_decorator(csrf_exempt, name='dispatch')
class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def perform_create(self, serializer):
        trip = serializer.save()
        log_path = generate_log_sheet(trip.id)
        trip.log_sheet = log_path
        trip.save()

        route, created = Route.objects.get_or_create(
            trip=trip,  # Directly link the Trip instance
            route="Default route",
            distance=0.0,
            duration=0.0
        )

        if not created:
            print(f"Route already exists for Trip {trip.id}")

    def retrieve(self, request, *args, **kwargs):
        trip = self.get_object()  
        routes = Route.objects.filter(trip=trip)  


        trip_serializer = self.get_serializer(trip)
        route_serializer = RouteSerializer(routes, many=True)  

   
        return Response({
            **trip_serializer.data,
            'routes': route_serializer.data  
        })

@method_decorator(csrf_exempt, name='dispatch')
class RouteCreateView(generics.CreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

@method_decorator(csrf_exempt, name='dispatch')
class RouteDetailView(generics.RetrieveAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    lookup_field = 'id'
     

@method_decorator(csrf_exempt, name='dispatch')
class ELDLogCreateView(generics.CreateAPIView):
    queryset = ELDLog.objects.all()
    serializer_class = ELDLogSerializer

