from django.urls import path

from .views import CourseDetailAPIView, CourseList

urlpatterns = [
    path("", CourseList.as_view()),
    path("<int:id>", CourseDetailAPIView.as_view()),
]
