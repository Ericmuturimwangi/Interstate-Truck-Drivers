from django.urls import path, include
from .views import TripViewSet, RouteCreateView, RouteDetailView, ELDLogCreateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'trips', TripViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/routes/', TripViewSet.as_view({'post':'create'}), name='create-route'),
    path('api/routes/<int:pk>/', RouteDetailView.as_view(), name='route-detail'),
    path('api/eld-logs/', ELDLogCreateView.as_view(), name='create-eld-log'),
]
