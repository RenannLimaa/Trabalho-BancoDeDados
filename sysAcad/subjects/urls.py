from django.urls import include, path

from .views import SubjectDetailAPIView, SubjectList

urlpatterns = [
    path("", SubjectList.as_view()),
    path("<int:id>", SubjectDetailAPIView.as_view()),
]
