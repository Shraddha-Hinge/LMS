from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, BatchViewSet, EnrolledStudentViewSet

router = DefaultRouter()

router.register(r'courses', CourseViewSet, basename='course')
router.register(r'batches', BatchViewSet, basename='batch')
router.register(r'enrolledstudents', EnrolledStudentViewSet, basename='enrolledstudent')

urlpatterns = [
    path('', include(router.urls)),  
]
