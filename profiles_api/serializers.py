from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field or testing our APIView"""
    name = serializers.CharField(max_length=10)
