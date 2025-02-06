from rest_framework import serializers
from .models import Announcement, Course, Batch


class AnnouncementSerializer(serializers.ModelSerializer):
    teacher_name = serializers.ReadOnlyField(source='teacher.username')

    class Meta:
        model = Announcement
        fields = ['id', 'course', 'batch', 'teacher', 'teacher_name', 'title', 'content', 'created_at']

    def validate(self, data):
        """Ensure teacher can only post announcements for their own courses."""
        teacher = self.context['request'].user
        course = data.get('course')
        
        # Check if the teacher is responsible for the selected course
        if course and course.teacher != teacher:
            raise serializers.ValidationError("You are not authorized to post announcements for this course.")
        return data

#
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'teacher']


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ['id', 'course', 'name']
