from django.urls import path
from . import views

urlpatterns = [
      path('studentapi/',views.StudentLC.as_view(),name='studentapi'),
      path('studentapi/<int:pk>', views.StudentRUD.as_view(), name='studentapi'),
]
