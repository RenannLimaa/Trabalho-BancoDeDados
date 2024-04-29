from django.contrib import admin
from django.urls import include, path
from django.urls.conf import include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"api/v1/api-auth/", include("rest_framework.urls")),
    path(f"api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        f"api/v1/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger",
    ),
]
