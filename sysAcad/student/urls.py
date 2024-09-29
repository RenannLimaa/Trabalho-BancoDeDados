from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.student_home, name='student_home'),
    path('remove_student/', views.remove_student, name='remove_student'),
    path('home/edit_info/', views.edit_student, name='edit_student'),
    path('home/class_enrollment/', views.enroll_in_classes, name='class_enrollment'),
    path('home/student-history/', views.student_history, name='student_history'),
    path('home/remove_classes/', views.remove_classes, name='remove_classes'),
]
