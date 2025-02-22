from django.contrib import admin
from .models import *

@admin.register(AboutAuthor)
class AboutAuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution', 'total_reviews', 'profile_image', 'rating')
    search_fields = ('name', 'institution')
    list_filter = ('institution',)

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'education')
    search_fields = ('name', 'education')
    list_filter = ('rating',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'about_author', 'original_price', 'discounted_price', 'rating', 'category', 'image', 'start_date')
    search_fields = ('title', 'about_author__name', 'category')
    list_filter = ('category', 'is_discount_active', 'start_date')
    
    def discounted_price(self, obj):
        return obj.discounted_price()
    discounted_price.short_description = "Discounted Price"

@admin.register(LearningPoint)
class LearningPointAdmin(admin.ModelAdmin):
    list_display = ('course', 'title')
    search_fields = ('title', 'course__title')

@admin.register(CourseDetail)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display = ('course', 'batch_start_date', 'batch_code', 'meeting_id', 'quiz_topic', 'mini_project')
    search_fields = ('batch_code', 'quiz_topic')

@admin.register(CourseMaterial)
class CourseMaterialAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'category')
    search_fields = ('title', 'category', 'course__title')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'rating', 'date_posted')
    search_fields = ('user__username', 'course__title')
    list_filter = ('rating', 'date_posted')
