"""
Sprint 0 — First test.

This test does two things:
1. Proves pytest + pytest-django are wired up correctly
2. Proves the health check endpoint works

If this passes in CI, our entire toolchain is working:
Git → GitHub → GitHub Actions → pytest → Django test client → pass
"""

import pytest
from django.test import Client


@pytest.mark.django_db
class TestHealthCheck:
    """Tests for the GET /api/v1/health/ endpoint."""

    def test_health_endpoint_returns_200(self):
        """The health endpoint should return 200 OK."""
        client = Client()
        response = client.get("/api/v1/health/")
        assert response.status_code == 200

    def test_health_endpoint_returns_status_healthy(self):
        """The response should include status and service name."""
        client = Client()
        response = client.get("/api/v1/health/")
        data = response.json()
        assert data["status"] == "healthy"
        assert data["service"] == "economic-pulse-platform"

    def test_health_endpoint_rejects_post(self):
        """The health endpoint should not accept POST requests."""
        client = Client()
        response = client.post("/api/v1/health/")
        assert response.status_code == 405  # Method Not Allowed
