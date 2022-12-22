from rest_framework import serializers

class SymbolDeleteSerializer(serializers.Serializer):
    input = serializers.CharField(max_length=None, min_length=None, allow_blank=False)