from rest_framework import serializers
from .models import Course, Batch, Resource, Task, Test

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'batch', 'title', 'file', 'resource_type', 'visibility', 'created_at', 'folder']  # Include new folder field

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'batch', 'title', 'description', 'due_date', 'task_type']  # Include new fields if necessary

class TestSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Test
        fields = ['id', 'batch', 'title', 'description', 'due_date', 'test_type'] 