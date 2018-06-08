from rest_framework import serializers


class DetactLanguageSerializer(serializers.Serializer):
    text = serializers.CharField(required=False, allow_blank=True, min_length=3, max_length=100)
