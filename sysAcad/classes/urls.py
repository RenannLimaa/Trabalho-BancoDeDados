from django.urls import path

from .views import ClassDetailAPIView, ClassList

urlpatterns = [
    path("", ClassList.as_view()),
    path("<int:id>", ClassDetailAPIView.as_view()),
]
