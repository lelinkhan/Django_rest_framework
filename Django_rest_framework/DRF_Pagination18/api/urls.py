from django.urls import path
from . import views

urlpatterns = [
    path('studentapi/', views.StudentApi.as_view(), name= 'studentapi'),
]