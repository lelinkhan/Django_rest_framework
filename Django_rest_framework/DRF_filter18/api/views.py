from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter


# Create your views here.

class Studentapi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # Search filter........>>>>
    filter_backends = [SearchFilter]
    search_fields = ['city']

    # filterset_fields = ['city']
    filterset_fields = ['name','city']
    # Easy and manual filter ........>>>
    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)
