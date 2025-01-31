from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BatchViewSet, LiveSessionViewSet

router = DefaultRouter()
router.register(r'batches', BatchViewSet, basename='batch')
router.register(r'live-sessions', LiveSessionViewSet, basename='live-session')

urlpatterns = [
    path('', include(router.urls)),  
]
