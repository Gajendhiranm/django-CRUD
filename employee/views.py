from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status,viewsets
 
from employee.models import Employee
from employee.serializers import EmployeeSerializer
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET', 'POST', 'DELETE'])
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employees,many=True)
        return JsonResponse(employee_serializer.data,safe=False)
    
    if request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data = employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse(employee_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(employee_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def employee_detail(request,pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except employee.DoesNotExist:
        return JsonResponse({'message':'Employee does not exists'},status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET':
        employee = Employee.objects.get(pk=pk)
        employee_serializer = EmployeeSerializer(employee)  
        return JsonResponse(employee_serializer.data)
    
    elif request.method == 'DELETE':
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return JsonResponse({'message':'Employee deleted sucessfully'},status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        employee = Employee.objects.get(pk=pk)
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(employee,data = employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse(employee_serializer.data)
        return JsonResponse(employee_serializer.errors,status=status.HTTP_400_BAD_REQUEST)