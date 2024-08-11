from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='professor_home'),
    path('remove_professor/', views.remove_professor, name='remove_professor'),
    path('home/edit_info/', views.edit_professor, name='edit_professor'),
]
