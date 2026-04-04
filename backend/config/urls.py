"""
Root URL configuration for the Economic Pulse Platform.

API endpoints live under /api/v1/ — versioned so future breaking
changes can use /api/v2/ without disrupting existing clients.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Django's built-in admin panel
    path("admin/", admin.site.urls),
    # Our REST API — delegates to api/urls.py for specific endpoints.
    # include() means "go look in that app's urls.py for the rest of the path."
    # So a request to /api/v1/health/ becomes just /health/ when it
    # reaches api/urls.py.
    path("api/v1/", include("api.urls")),
]
