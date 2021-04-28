from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
