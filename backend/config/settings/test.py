"""
Test settings — used when running pytest.

Activated by: DJANGO_SETTINGS_MODULE=config.settings.test
(configured in pyproject.toml under [tool.pytest.ini_options])
"""

from .base import *  # noqa: F401, F403

DEBUG = False

SECRET_KEY = "test-secret-key-not-for-production"

# Use SQLite in-memory for fast unit tests.
# No Docker needed just to run tests — they finish in seconds.
# We'll add PostgreSQL integration tests in later sprints
# when we need PG-specific features.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Speed up password hashing in tests (we don't need security here)
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]
