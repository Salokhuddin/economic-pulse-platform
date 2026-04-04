from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckView(APIView):
    """
    Simple health check endpoint.

    Returns 200 OK with status info. Used by:
    - Docker health checks
    - CI pipelines to verify the app starts
    - Load balancers (in production)
    - You, to confirm everything is wired up correctly
    """

    # No authentication needed — anyone can check if the service is alive
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        """Handle GET /api/v1/health/"""
        return Response(
            {
                "status": "healthy",
                "service": "economic-pulse-platform",
                "version": "0.1.0",
            }
        )
