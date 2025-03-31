from rest_framework import serializers
from .models import Trip, Route, ELDLog

class TripSerializer( serializers. ModelSerializer):
    class Meta:
        model =Trip
        fields = "__all__"

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"

class ELDLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ELDLog
        fields = "__all__"