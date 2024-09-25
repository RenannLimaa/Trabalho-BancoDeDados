from django.urls import path

from .views import GradeDetailAPIView, GradeList

urlpatterns = [
    path("", GradeList.as_view()),
    path("<int:id>", GradeDetailAPIView.as_view()),
]
