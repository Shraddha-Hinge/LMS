from django.contrib import admin
from .models import Student, Course, Enrollment, Attendance, Grade

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'dob', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'instructor', 'credits', 'semester')
    search_fields = ('name', 'instructor')

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date')
    search_fields = ('student__first_name', 'student__last_name', 'course__name')

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date', 'status')
    list_filter = ('status', 'course')
    search_fields = ('student__first_name', 'student__last_name', 'course__name')

class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'grade', 'date_assigned')
    search_fields = ('student__first_name', 'student__last_name', 'course__name')
    list_filter = ('grade', 'course')

admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Grade, GradeAdmin)
