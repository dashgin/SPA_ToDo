from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.utils.functional import partition

urlpatterns = [
    path(f"{settings.ADMIN_URL}/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("todo.urls")),
]
