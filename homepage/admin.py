from django.contrib import admin
from .models import *

# Register models in Django Admin
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'education', 'rating')
    search_fields = ('name', 'education')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount', 'is_discount_active', 'start_date', 'lifetime_access')
    search_fields = ('title',)
    list_filter = ('is_discount_active', 'lifetime_access', 'start_date')

@admin.register(LearningPoint)
class LearningPointAdmin(admin.ModelAdmin):
    list_display = ('course', 'title')
    search_fields = ('title',)

@admin.register(CourseDetail)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display = ('course', 'batch_code', 'batch_start_date', 'quiz_topic')
    search_fields = ('batch_code', 'quiz_topic')

@admin.register(CourseMaterial)
class CourseMaterialAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'category')
    search_fields = ('title', 'category')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'rating', 'date_posted')
    search_fields = ('user__username', 'course__title')
    list_filter = ('rating', 'date_posted')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution', 'total_reviews', 'rating')
    search_fields = ('name', 'institution')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('author', 'degree', 'institution', 'year_start', 'year_end')
    search_fields = ('degree', 'institution')
