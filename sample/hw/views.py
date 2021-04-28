from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView


def index(request):
    return HttpResponse('Начальная страница')

