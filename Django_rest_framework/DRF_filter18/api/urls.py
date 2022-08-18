from django.urls import path
from . import views

urlpatterns = [
    path('studentapi/', views.Studentapi.as_view(), name='studentapi'),
]