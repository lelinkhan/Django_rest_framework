from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from .models import Student
from .serializer import StudentSerializer


# Create your views here.
class StudentAPI(APIView):
    def get(self,request, pk=None, format = None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self,request, pk=None, format = None):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request, pk=None, format = None):
        id = pk
        stu = Student.objects.get(id=id)
        data = request.data
        serializer = StudentSerializer(stu, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Created!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request, pk=None, format = None):
        id = pk
        stu = Student.objects.get(id=id)
        data = request.data
        serializer = StudentSerializer(stu, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Created!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk=None, format=None):
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg': 'Complete Data Created!'}, status=status.HTTP_201_CREATED)
