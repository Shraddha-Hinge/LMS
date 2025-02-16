from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()
    time_left = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_discounted_price(self, obj):
        return obj.discounted_price()  

    def get_time_left(self, obj):
        return obj.time_left() 

    def get_average_rating(self, obj):
        return obj.average_rating() 

class LearningPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningPoint
        fields = '__all__'

class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDetail
        fields = '__all__'

class CourseMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseMaterial
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  
    course_title = serializers.ReadOnlyField(source='course.title')  

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user  
        return super().create(validated_data)

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.name')  

    class Meta:
        model = Education
        fields = '__all__'
