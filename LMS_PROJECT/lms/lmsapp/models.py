from django.db import models


class Add_Student(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email_id = models.EmailField(max_length=200)
	phone_number = models.CharField(max_length=13)
	dob = models.DateField()

'''	def create(self, validated_data):
		return Add_Student.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.first_name = validated_data.get('first_name', instance.first_name)
		instance.last_name = validated_data.get('last_name', instance.last_name)
		instance.email_id = validated_data.get('email_id', instance.email_id)
		instance.phone_number = validated_data.get('phone_number', instance.phone_number)
		instance.dob = validated_data.get('dob', instance.dob)

		instance.save()
		return instance'''

class Add_Staff(models.Model):
	staff_first_name = models.CharField(max_length=100)
	staff_last_name = models.CharField(max_length=100)
	staff_email_id = models.EmailField(max_length=200)
	staff_phone_number = models.CharField(max_length=13)
	lecture_time = models.DateTimeField()

'''	def create(self, validated_data):
		return Add_Staff.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.staff_first_name = validated_data.get('staff_first_name', instance.staff_first_name)
		instance.staff_last_name = validated_data.get('staff_last_name', instance.staff_last_name)
		instance.staff_email_id = validated_data.get('staff_email_id', instance.staff_email_id)
		instance.staff_phone_number = validated_data.get('staff_phone_number', instance.staff_phone_number)
		instance.lecture_time = validated_data.get('lecture_time', instance.lecture_time)

		instance.save()
		return instance'''