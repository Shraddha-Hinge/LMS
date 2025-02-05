from rest_framework import serializers
from .models import Admin



class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'username', 'email', 'phone_number', 'is_staff', 'is_superuser', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Admin.objects.create_user(**validated_data)
        return user



