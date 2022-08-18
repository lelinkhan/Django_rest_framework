from . models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class StudentLC(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

