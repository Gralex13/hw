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
