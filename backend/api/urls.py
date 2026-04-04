"""
API v1 URL routing.

All endpoints are prefixed with /api/v1/ (configured in config/urls.py).
So path("health/") here becomes /api/v1/health/ in the full URL.
"""

from django.urls import path

from api.views.health import HealthCheckView

urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health-check"),
]
