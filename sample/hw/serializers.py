from rest_framework import serializers

from .models import Student, Teacher, Subject, Group


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    degree = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.degree = validated_data.get('degree', instance.degree)
        instance.save()
        return instance


class SubjectSerializer(serializers.Serializer):
    subj = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Subject.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.subj = validated_data.get('subj', instance.name)
        instance.save()
        return instance


class GroupSerializer(serializers.Serializer):
    group_name = serializers.CharField(max_length=255)
    # students = serializers.PrimaryKeyRelatedField()

    def create(self, validated_data):
        return Group.create(**validated_data)

    def update(self, instance, validated_data):
        instance.group_name = validated_data.get('group_name', instance.group_name)
        instance.students = validated_data.get('students', instance.students)
        instance.save()
        return instance
