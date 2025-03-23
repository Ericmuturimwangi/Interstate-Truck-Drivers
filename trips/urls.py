from django.urls import path, include
from .views import TripViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'trips', TripViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/routes/', RouteCreateView.as_view(), name='create-route'),
    path('api/routes/<int:pk>/', RouteDetailView.as_view(), name='route-detail'),
    path('api/eld-logs/', ELDLogCreateView.as_view(), name='create-eld-log'),
]
