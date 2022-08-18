from django.urls import path
from . import views

urlpatterns = [
    path('studentapi/', views.StudentList.as_view(), name='studentapi'),
    # path('studentapi/', views.StudentCreate.as_view(), name='studentapi'),
    # path('studentapi/<int:pk>/', views.StudentUpdate.as_view(), name='studentapi'),
    # path('studentapi/<int:pk>/', views.StudentRetrive.as_view(), name='studentapi'),
    path('studentapi/<int:pk>/', views.StudentDelete.as_view(), name='studentapi'),
]
