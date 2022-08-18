from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from .customsauth import MyAuthentication
from rest_framework.permissions import IsAuthenticated




class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [MyAuthentication]
    permission_classes = [IsAuthenticated]


