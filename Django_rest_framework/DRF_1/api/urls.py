from django.urls import path
from . import views

urlpatterns = [
    path('student_api/', views.StudentAPI.as_view(), name='student_api'),
]