from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student, Subject, Lesson, Teacher, Group
from .serializers import StudentSerializer


'''
CRUD Student
'''
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
