from django.urls import path

from .views import ProfessorDetailAPIView, ProfessorList

urlpatterns = [
    path("", ProfessorList.as_view()),
    path("<int:id>", ProfessorDetailAPIView.as_view()),
]
