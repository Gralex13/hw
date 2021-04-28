from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Student, Subject, Lesson, Teacher, Group
from .serializers import StudentSerializer, TeacherSerializer, SubjectSerializer, GroupSerializer


class StudentView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response({"students": serializer.data})

    def post(self, request):
        student = request.data.get('student')
        serializer = StudentSerializer(data=student)
        if serializer.is_valid(raise_exception=True):
            student_saved = serializer.save()
        return Response({"success": "Student '{}' created successfully".format(student_saved.name)})

    def put(self, request, pk):
        student_saved = get_object_or_404(Student.objects.all(), pk=pk)
        data = request.data.get('student')
        serializer = StudentSerializer(instance=student_saved, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            student_saved = serializer.save()
        return Response({"success": "Student '{}' updated successfully".format(student_saved.name)})

    def delete(self, request, pk):
        student = get_object_or_404(Student.objects.all(), pk=pk)
        student.delete()
        return Response({"success": "Student with id '{}' has been deleted".format(pk)}, status=204)



class TeacherView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response({"teachers": serializer.data})

    def post(self, request):
        teacher = request.data.get('teacher')
        serializer = TeacherSerializer(data=teacher)
        if serializer.is_valid(raise_exception=True):
            teacher_saved = serializer.save()
        return Response({"success": "Teacher '{}' created successfully".format(teacher_saved.name)})

    def put(self, request, pk):
        teacher_saved = get_object_or_404(Teacher.objects.all(), pk=pk)
        data = request.data.get('teacher')
        serializer = TeacherSerializer(instance=teacher_saved, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            teacher_saved = serializer.save()
        return Response({"success": "Teacher '{}' updated successfully".format(teacher_saved.name)})

    def delete(self, request, pk):
        teacher = get_object_or_404(Teacher.objects.all(), pk=pk)
        teacher.delete()
        return Response({"success": "Teacher with id '{}' has been deleted".format(pk)}, status=204)


class SubjectView(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response({"subjects": serializer.data})

    def post(self, request):
        subject = request.data.get('subject')
        serializer = SubjectSerializer(data=subject)
        if serializer.is_valid(raise_exception=True):
            subject_saved = serializer.save()
        return Response({"success": "Subject '{}' created successfully".format(subject_saved.name)})

    def put(self, request, pk):
        subject_saved = get_object_or_404(Subject.objects.all(), pk=pk)
        data = request.data.get('subject')
        serializer = SubjectSerializer(instance=subject_saved, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            subject_saved = serializer.save()
        return Response({"success": "Subject '{}' updated successfully".format(subject_saved.name)})

    def delete(self, request, pk):
        subject = get_object_or_404(Subject.objects.all(), pk=pk)
        subject.delete()
        return Response({"success": "Subject with id '{}' has been deleted".format(pk)}, status=204)


class GroupView(APIView):
    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response({"groups": serializer.data})

    def post(self, request):
        group = request.data.get('group')
        serializer = SubjectSerializer(data=group)
        if serializer.is_valid(raise_exception=True):
            group_saved = serializer.save()
        return Response({"success": "Group '{}' created successfully".format(group_saved.name)})

    def put(self, request, pk):
        group_saved = get_object_or_404(Group.objects.all(), pk=pk)
        data = request.data.get('group')
        serializer = SubjectSerializer(instance=group_saved, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            group_saved = serializer.save()
        return Response({"success": "Group '{}' updated successfully".format(group_saved.name)})

    def delete(self, request, pk):
        group = get_object_or_404(Group.objects.all(), pk=pk)
        group.delete()
        return Response({"success": "Group with id '{}' has been deleted".format(pk)}, status=204)
