from . serializer import StudentSerializer
from . models import Student
from rest_framework.generics import ListAPIView
from . customPagination import MyPagination

# Create your views here.
class StudentApi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPagination
