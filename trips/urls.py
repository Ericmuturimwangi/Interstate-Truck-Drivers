from django.urls import path, include
from .views import TripViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'trips', TripViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
