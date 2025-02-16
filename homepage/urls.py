from django.urls import path
from .views import *

urlpatterns = [
    # Instructor
    path('instructors/', InstructorListCreate.as_view(), name='instructor-list-create'),
    path('instructors/<int:pk>/', InstructorDetailView.as_view(), name='instructor-detail'),

    # Course
    path('courses/', CourseListCreate.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),

    # Course Detail
    path('course-details/', CourseExtraDetailListCreate.as_view(), name='course-detail-list-create'),
    path('course-details/<int:pk>/', CourseExtraDetailView.as_view(), name='course-detail-view'),

    # Learning Points
    path('courses/<int:course_id>/learning-points/', LearningPointListCreate.as_view(), name='learning-points-list-create'),
    path('learning-points/<int:pk>/', LearningPointDetailView.as_view(), name='learning-points-detail'),

    # Course Materials
    path('courses/<int:course_id>/materials/', CourseMaterialListCreate.as_view(), name='course-materials-list-create'),
    path('materials/<int:pk>/', CourseMaterialDetailView.as_view(), name='course-materials-detail'),

    # Reviews
    path('courses/<int:course_id>/reviews/', ReviewListCreate.as_view(), name='reviews-list-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='reviews-detail'),

    # Author
    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

    # Education
    path('authors/<int:author_id>/education/', EducationListCreate.as_view(), name='education-list-create'),
    path('education/<int:pk>/', EducationDetailView.as_view(), name='education-detail'),
]
