from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='student_home'),
    path('remove_student/', views.remove_student, name='remove_student')
]
