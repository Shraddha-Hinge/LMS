from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from django.contrib.auth.models import User  
from .models import Course, Batch, EnrolledStudent
from .serializers import EnrolledStudentSerializer, CourseSerializer, BatchSerializer
from rest_framework.permissions import IsAuthenticated

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]  

    # Custom action to archive courses
    @action(detail=True, methods=['post'])
    def archive(self, request, pk=None):
        course = self.get_object()
        
        if not Batch.objects.filter(course=course).exists() and not EnrolledStudent.objects.filter(course=course).exists():
            course.archived = True
            course.save()
            return Response({'status': 'Course archived successfully'})
        return Response({'error': 'Cannot archive a course with active batches or enrolled students'}, status=400)

    # Custom action to delete a course
    @action(detail=True, methods=['delete'])
    def delete_course(self, request, pk=None):
        course = self.get_object()
        
        if not Batch.objects.filter(course=course).exists() and not EnrolledStudent.objects.filter(course=course).exists():
            course.delete()
            return Response({'status': 'Course deleted successfully'})
        return Response({'error': 'Cannot delete a course with active batches or enrolled students'}, status=400)

class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    permission_classes = [IsAuthenticated]

class EnrolledStudentViewSet(viewsets.ModelViewSet):
    queryset = EnrolledStudent.objects.all()
    serializer_class = EnrolledStudentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        course = serializer.validated_data.get('course')

        if course.archived:
            raise ValidationError({'error': 'Cannot enroll in an archived course.'})

        serializer.save()

    @action(detail=True, methods=['post'])
    def enroll(self, request, pk=None):
        course = Course.objects.get(id=pk)
        
        if course.archived:
            return Response({'error': 'You cannot enroll in an archived course.'}, status=status.HTTP_400_BAD_REQUEST)
        
        user_id = request.data.get('user_id')
        
        try:
            student = User.objects.get(id=user_id)  
        except User.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Enroll the student in the course
        batch_id = request.data.get('batch_id', None)
        if batch_id:
            try:
                batch = Batch.objects.get(id=batch_id, course=course)
            except Batch.DoesNotExist:
                return Response({'error': 'Invalid batch for this course'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            batch = None
        
        EnrolledStudent.objects.create(course=course, student=student, batch=batch)
        
        return Response({'status': 'Student enrolled successfully.'}, status=status.HTTP_201_CREATED)
