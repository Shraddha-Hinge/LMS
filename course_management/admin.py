from django.contrib import admin
from .models import Course, Batch, EnrolledStudent
from django.db.models import Count

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'archived')
    list_filter = ('archived', 'created_by')
    search_fields = ('name', 'description')

    # Archive courses if no active batches or enrolled students
    def archive_courses(self, request, queryset):
        for course in queryset:
            if not course.batch_set.exists() and not course.enrolledstudent_set.exists():
                course.archived = True
                course.save()
        self.message_user(request, "Selected courses archived.")
    archive_courses.short_description = "Archive selected courses"

    # Delete courses if no active batches or enrolled students
    def delete_courses(self, request, queryset):
        for course in queryset:
            if not course.batch_set.exists() and not course.enrolledstudent_set.exists():
                course.delete()
        self.message_user(request, "Selected courses deleted.")
    delete_courses.short_description = "Delete selected courses"

    actions = ['archive_courses', 'delete_courses']

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'start_date', 'end_date')
    list_filter = ('course',)

@admin.register(EnrolledStudent)
class EnrolledStudentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'batch', 'enrollment_date')
    list_filter = ('course', 'batch')

