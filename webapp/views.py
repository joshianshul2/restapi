from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees
from .serializers import empserializer
# Create your views here.


class empList(APIView) :
    def get(self,request) :
        emp1=employees.objects.all()
        serializer=empserializer(emp1,many=True)
        return Response(serializer.data)

    def post(self):
        pass