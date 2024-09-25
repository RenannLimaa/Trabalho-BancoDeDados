from django.urls import path

from .views import StudentDetailAPIView, StudentList

urlpatterns = [
    path("", StudentList.as_view()),
    path("<int:id>", StudentDetailAPIView.as_view()),
]
