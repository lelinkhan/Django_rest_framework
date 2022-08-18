from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from . customspermission import MyPermission



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]


