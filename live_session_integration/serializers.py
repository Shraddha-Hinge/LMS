from rest_framework import serializers
from .models import Batch, LiveSession

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'


class LiveSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveSession
        fields = '__all__'