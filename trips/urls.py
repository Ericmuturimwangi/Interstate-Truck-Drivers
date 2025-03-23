from django.urls import path, include
from .views import TripViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'trips', TripViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/routes/<int:route_id>/', views.get_route_details, name='get_route_details'),
]
