from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent_folder = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, related_name='folders', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.module.name}'


class Resource(models.Model):
    RESOURCE_TYPES = [
        ('blog', 'Blog'),
        ('pdf', 'PDF'),
        ('article', 'Article'),
        ('video', 'Video'),
    ]
    title = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES)
    content = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='resources/', blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    folder = models.ForeignKey(Folder, related_name='resources', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
