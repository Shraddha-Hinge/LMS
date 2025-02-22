from rest_framework import serializers
from .models import *

class AboutAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutAuthor
        fields = '__all__'

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

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
    user = serializers.StringRelatedField()  
    date_posted = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'
    
    def get_date_posted(self, obj):
        return obj.date_posted.strftime('%d %b %Y')

class CourseSerializer(serializers.ModelSerializer):
    last_updated = serializers.SerializerMethodField()
    time_left = serializers.SerializerMethodField()
    discounted_price = serializers.SerializerMethodField()
    about_author = AboutAuthorSerializer(read_only=True) 
    instructor = InstructorSerializer(read_only=True) 
    learning_points = LearningPointSerializer(many=True, read_only=True)
    course_detail = CourseDetailSerializer(read_only=True)
    materials = CourseMaterialSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_last_updated(self, obj):
        return obj.last_updated.strftime('%d %b %Y')

    def get_time_left(self, obj):
        return obj.time_left()

    def get_discounted_price(self, obj):
        return format(obj.discounted_price(), '.2f')
