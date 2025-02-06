from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnnouncementViewSet, CourseViewSet, BatchViewSet

router = DefaultRouter()
router.register(r'announcements', AnnouncementViewSet, basename='announcement')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'batches', BatchViewSet, basename='batch')

urlpatterns = [
    path('', include(router.urls)),
]
