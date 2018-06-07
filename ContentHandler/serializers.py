from rest_framework import serializers


class DetactLanguageSerializer(serializers.Serializer):
    text = serializers.CharField(required=False, allow_blank=True, max_length=100)
