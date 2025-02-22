from django.urls import path
from .views import *

urlpatterns = [

    # About Authors
    path('about-authors/', AboutAuthorListCreate.as_view(), name='about-author-list-create'),
    path('about-authors/<int:pk>/', AboutAuthorDetailView.as_view(), name='about-author-detail'),

    # Instructor Details
    path('instructors/', InstructorListCreate.as_view(), name='instructor-list-create'),
    path('instructors/<int:pk>/', InstructorDetailView.as_view(), name='instructor-detail'),

    # Course Details
    path('courses/', CourseListCreate.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),  

    # Course Complete Details
    path('courses/<int:pk>/details/', CourseDetailCompleteView.as_view(), name='course-detail-complete'),

    # Creating Learning Points (What you'll learn) 
    path('courses/<int:course_id>/learning-points/', LearningPointListCreate.as_view(), name='learning-points-list-create'),
    path('learning-points/<int:pk>/', LearningPointDetailView.as_view(), name='learning-points-detail'),

    # Course Extra Details (This Course Includes)
    path('courses/<int:course_id>/extra-details/', CourseDetailListCreateView.as_view(), name='course-extra-details'),
    path('courses/<int:course_id>/extra-details/<int:pk>/', CourseDetailRetrieveUpdateView.as_view(), name='course-extra-detail'),

    # Course Materials
    path('courses/<int:course_id>/materials/', CourseMaterialListCreate.as_view(), name='course-materials-list-create'),
    path('materials/<int:pk>/', CourseMaterialDetailView.as_view(), name='course-materials-detail'),

    # Reviews
    path('courses/<int:course_id>/reviews/', ReviewListCreate.as_view(), name='reviews-list-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='reviews-detail'),

]

