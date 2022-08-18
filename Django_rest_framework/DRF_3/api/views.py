from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Student
from .serializer import StudentSerializer


# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def studentAPI(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(id=id)
        data = request.data
        serializer = StudentSerializer(stu, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(id=id)
        data = request.data
        serializer = StudentSerializer(stu, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(id = id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
