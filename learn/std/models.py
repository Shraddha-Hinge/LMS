from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Batch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Resource(models.Model):
    RESOURCE_TYPES = [
        ('article', 'Article'),
        ('video', 'Video'),
        ('document', 'Document'),
        ('link', 'Link'),
    ]
    
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='resources/')
    resource_type = models.CharField(max_length=50, choices=RESOURCE_TYPES)
    visibility = models.CharField(max_length=50, choices=[('public', 'Public'), ('private', 'Private')])
    created_at = models.DateTimeField(auto_now_add=True)
    folder = models.CharField(max_length=255, blank=True, null=True)  
    
class Task(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    task_type = models.CharField(max_length=50, choices=[
        ('quiz', 'Quiz'),
        ('document', 'Document'),
        ('qa', 'Q/A'),
        ('link', 'Link'),
        ('combined', 'Combined'),
    ])
    # Additional fields can be added as necessary

class Test(models.Model):  
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    test_type = models.CharField(max_length=50, choices=[
        ('quiz', 'Quiz'),
        ('document', 'Document'),
        ('qa', 'Q/A'),
        ('link', 'Link'),
        ('combined', 'Combined'),
    ])
    # Additional fields can be added as necessary
