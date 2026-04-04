"""
Development settings — used when running locally.

Activated by: DJANGO_SETTINGS_MODULE=config.settings.development
(this is the default in manage.py)
"""

from .base import *  # noqa: F401, F403

# Show detailed error pages in the browser when something breaks
DEBUG = True

# In development, accept requests from any hostname
ALLOWED_HOSTS = ["*"]
