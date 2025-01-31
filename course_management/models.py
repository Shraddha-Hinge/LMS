from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    learning_outcomes = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_created')
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Batch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='batches')
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.course.name}"


class EnrolledStudent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrolled_students')
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='students', null=True, blank=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.course.name}"

