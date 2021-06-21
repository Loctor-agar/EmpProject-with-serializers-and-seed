from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Employee
from .serialaizers import EmpSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def emp_list(request):

    if request.method == "GET":
        emps = Employee.objects.all() #select * from employee
        serializer = EmpSerializer(emps, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        emp = request.POST
        serializer = EmpSerializer(data=emp)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

