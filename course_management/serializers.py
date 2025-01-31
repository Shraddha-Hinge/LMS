from rest_framework import serializers
from .models import Course, Batch, EnrolledStudent

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'

class EnrolledStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrolledStudent
        fields = '__all__'
