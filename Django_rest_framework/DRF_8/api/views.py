from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets


class StudentViewSet(viewsets.ViewSet):

    def list(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)


    def create(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        id = pk
        stu = Student.objects.get(id=id)
        data = request.data
        serializer = StudentSerializer(stu, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        id = pk
        stu = Student.objects.get(id=id)
        data = request.data
        serializer = StudentSerializer(stu, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partially Data Updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        id = pk
        stu = Student.objects.get(id = id)
        stu.delete()
        return Response({'msg':'Data Deleted!'})