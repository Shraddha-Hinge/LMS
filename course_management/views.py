from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *

# Course Complete Details View
class CourseDetailCompleteView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Instructor Views
class InstructorListCreate(generics.ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

# Course Views
class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Course Extra Details 
class CourseDetailListCreateView(generics.ListCreateAPIView):
    serializer_class = CourseDetailSerializer

    def get_queryset(self):
        course_id = self.kwargs.get("course_id")
        if course_id:
            return CourseDetail.objects.filter(course_id=course_id)
        return CourseDetail.objects.none()

class CourseDetailRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseDetail.objects.all()
    serializer_class = CourseDetailSerializer

# Learning Point Views
class LearningPointListCreate(generics.ListCreateAPIView):
    serializer_class = LearningPointSerializer

    def get_queryset(self):
        course_id = self.kwargs.get("course_id")
        if course_id:
            return LearningPoint.objects.filter(course_id=course_id)
        return LearningPoint.objects.none()

    def perform_create(self, serializer):
        course = get_object_or_404(Course, pk=self.kwargs["course_id"])
        serializer.save(course=course)

class LearningPointDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LearningPoint.objects.all()
    serializer_class = LearningPointSerializer

# Course Material Views
class CourseMaterialListCreate(generics.ListCreateAPIView):
    serializer_class = CourseMaterialSerializer

    def get_queryset(self):
        course_id = self.kwargs.get("course_id")
        if course_id:
            return CourseMaterial.objects.filter(course_id=course_id)
        return CourseMaterial.objects.none()
        
    def perform_create(self, serializer):
        course = get_object_or_404(Course, pk=self.kwargs["course_id"])
        serializer.save(course=course)

class CourseMaterialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseMaterial.objects.all()
    serializer_class = CourseMaterialSerializer

# Review Views 
class ReviewListCreate(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        course_id = self.kwargs.get("course_id")
        if course_id:
            return Review.objects.filter(course_id=course_id)
        return Review.objects.none()

    def perform_create(self, serializer):
        course = get_object_or_404(Course, pk=self.kwargs["course_id"])
        serializer.save(course=course, user=self.request.user)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# About Author Views
class AboutAuthorListCreate(generics.ListCreateAPIView):
    queryset = AboutAuthor.objects.all()
    serializer_class = AboutAuthorSerializer

class AboutAuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutAuthor.objects.all()
    serializer_class = AboutAuthorSerializer

