from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, BatchViewSet, ResourceViewSet, TaskViewSet, TestViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'batches', BatchViewSet)
router.register(r'resources', ResourceViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'tests', TestViewSet) 
urlpatterns = [
    path('', include(router.urls)),
]
