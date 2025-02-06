from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True}
    )

    def __str__(self):
        return self.name


class Batch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='batches')
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})

    def __str__(self):
        return f"{self.name} ({self.course.name})"


class Announcement(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='announcements')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.teacher.username}"
