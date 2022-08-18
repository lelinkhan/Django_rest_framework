from django.urls import path
from . import views

urlpatterns = [
    path('studentapi/', views.LCStudentApi.as_view(), name='studentapi'),
    path('studentapi/<int:pk>/', views.RUDStudentApi.as_view(), name='studentapi'),
]
