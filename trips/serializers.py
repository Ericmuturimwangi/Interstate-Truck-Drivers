from rest_framework import serializers
from .models import Trip, Route, ELDLog
class RouteSerializer(serializers.ModelSerializer):
    trip_id = serializers.PrimaryKeyRelatedField(queryset=Trip.objects.all(), source='trip', write_only=True)
    class Meta:
        model = Route
        fields = ['id', 'route', 'distance', 'duration', 'created_at', 'trip_id']

class TripSerializer( serializers. ModelSerializer):

    class Meta:
        model =Trip
        fields = ['id', 'current_location', 'pickup_location', 'dropoff_location', 'current_cycle_hours', 'created_at', 'log_sheet']





class ELDLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ELDLog
        fields = "__all__"