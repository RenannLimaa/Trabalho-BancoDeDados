from django.urls import path
from professor import views
from authentication.views import user_login
urlpatterns = [
    path('home/', views.home, name='professor_home'),
    path('remove_professor/', views.remove_professor, name='remove_professor'),
    path('home/edit_info/', views.edit_professor, name='edit_professor'),
    path('register-in-class/', views.register_in_class, name='register_in_class'),
    path('my-classes/', views.view_current_classes, name='view_current_classes'),
    path('turmas/<int:class_id>/estudantes/', views.view_students_in_class, name='view_students_in_class'),
    path("login", user_login, name="login"),

]
