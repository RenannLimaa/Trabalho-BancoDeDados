from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='student_home'),
    path('remove_student/', views.remove_student, name='remove_student'),
    path('home/edit_info/', views.edit_student, name='edit_student'),
]
