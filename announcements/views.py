from rest_framework import viewsets, permissions
from .models import Announcement, Course, Batch
from .serializers import AnnouncementSerializer, CourseSerializer, BatchSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()  # Add this line to avoid DRF error
    serializer_class = AnnouncementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Filter announcements by teacher's assigned courses."""
        user = self.request.user
        return Announcement.objects.filter(teacher=user)

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()  # Add this line
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Restrict courses to those assigned to the teacher."""
        return Course.objects.filter(teacher=self.request.user)


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()  # Add this line
    serializer_class = BatchSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Restrict batches based on teacher's courses."""
        user_courses = Course.objects.filter(teacher=self.request.user)
        return Batch.objects.filter(course__in=user_courses)
