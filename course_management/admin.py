from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'price', 'discounted_price', 'rating', 'category')
    search_fields = ('title', 'instructor', 'category')
    list_filter = ('category', 'rating')
