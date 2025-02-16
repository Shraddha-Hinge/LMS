from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *

# Instructor APIs
class InstructorListCreate(generics.ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

# Course APIs
class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Learning Point APIs
class LearningPointListCreate(generics.ListCreateAPIView):
    serializer_class = LearningPointSerializer

    def get_queryset(self):
        return LearningPoint.objects.filter(course_id=self.kwargs['course_id'])

    def perform_create(self, serializer):
        course = get_object_or_404(Course, id=self.kwargs['course_id'])
        serializer.save(course=course)

class LearningPointDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LearningPoint.objects.all()
    serializer_class = LearningPointSerializer

# Course Detail APIs
class CourseExtraDetailListCreate(generics.ListCreateAPIView):
    queryset = CourseDetail.objects.all()
    serializer_class = CourseDetailSerializer

class CourseExtraDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseDetail.objects.all()
    serializer_class = CourseDetailSerializer

# Course Material APIs
class CourseMaterialListCreate(generics.ListCreateAPIView):
    serializer_class = CourseMaterialSerializer

    def get_queryset(self):
        return CourseMaterial.objects.filter(course_id=self.kwargs['course_id'])

    def perform_create(self, serializer):
        course = get_object_or_404(Course, id=self.kwargs['course_id'])
        serializer.save(course=course)

class CourseMaterialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseMaterial.objects.all()
    serializer_class = CourseMaterialSerializer

# Review APIs (Requires Authentication)
class ReviewListCreate(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):
        return Review.objects.filter(course_id=self.kwargs['course_id'])

    def perform_create(self, serializer):
        course = get_object_or_404(Course, id=self.kwargs['course_id'])
        serializer.save(course=course, user=self.request.user)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Author APIs
class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Education APIs
class EducationListCreate(generics.ListCreateAPIView):
    serializer_class = EducationSerializer

    def get_queryset(self):
        return Education.objects.filter(author_id=self.kwargs['author_id'])

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.kwargs['author_id'])
        serializer.save(author=author)

class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
