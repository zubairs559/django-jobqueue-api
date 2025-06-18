from rest_framework import serializers

class JobCreateSerializer(serializers.Serializer):
    payload = serializers.CharField()
