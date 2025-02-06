from rest_framework import serializers
from .models import Add_Student , Add_Staff

class AddStudentSerializer(serializers.ModelSerializer):
	first_name = serializers.CharField(max_length=100)
	last_name = serializers.CharField(max_length=100)
	email_id = serializers.EmailField(max_length=200)
	phone_number = serializers.CharField(max_length=13)
	dob = serializers.DateField()

	class Meta:
		model = Add_Student
		fields = "__all__"

class AddStaffSerializer(serializers.ModelSerializer):
	staff_first_name = serializers.CharField(max_length=100)
	staff_last_name = serializers.CharField(max_length=100)
	staff_email_id = serializers.EmailField(max_length=200)
	staff_phone_number = serializers.CharField(max_length=13)
	lecture_time = serializers.DateTimeField()

	class Meta:
		model = Add_Staff
		fields = "__all__"