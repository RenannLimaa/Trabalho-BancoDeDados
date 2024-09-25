from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from classes.urls import *
from courses.urls import *
from grades.urls import *
from professors.urls import *
from students.urls import *
from subjects.urls import *

schema_view = get_schema_view(
    openapi.Info(
        title="SysAcad",
        default_version="v1",
        description="API for managing movies, theaters, and sessions in a cinema",
        contact=openapi.Contact(email="jonas.nogueira@aluno.uece.br"),
    ),
    public=True,
)

urlpatterns = [
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("api/classes/", include("classes.urls")),
    path("api/courses/", include("courses.urls")),
    path("api/grades/", include("grades.urls")),
    path("api/professors/", include("professors.urls")),
    path("api/students/", include("students.urls")),
    path("api/subjects/", include("subjects.urls")),
    path("admin/", admin.site.urls),
]
