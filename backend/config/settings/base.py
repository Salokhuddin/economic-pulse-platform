"""
Base settings shared across all environments.

Environment-specific settings (development, test) import from
this file and override what they need.
"""

from pathlib import Path

import environ

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
# This figures out where your project lives on disk.
# __file__        = backend/config/settings/base.py
# .parent         = backend/config/settings/
# .parent.parent  = backend/config/
# .parent.parent.parent = backend/
# So BASE_DIR = the backend/ folder.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Read .env file from the project root (one level above backend/)
# environ.Env() is from django-environ — it reads .env files and
# provides typed access to environment variables.
env = environ.Env()
env_file = BASE_DIR.parent / ".env"
if env_file.exists():
    env.read_env(str(env_file))

# ---------------------------------------------------------------------------
# Core
# ---------------------------------------------------------------------------
# SECRET_KEY is used for cryptographic signing (sessions, CSRF tokens).
# In development the default is fine. In production you MUST change it.
SECRET_KEY = env("DJANGO_SECRET_KEY", default="insecure-dev-key-change-in-production")

# DEBUG=True shows detailed error pages. NEVER True in production.
DEBUG = env.bool("DJANGO_DEBUG", default=False)

# Which hostnames Django will accept requests for.
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])

# ---------------------------------------------------------------------------
# Installed apps
# ---------------------------------------------------------------------------
# Django loads these in order. Each "app" is a self-contained module.
INSTALLED_APPS = [
    # Django built-in apps
    "django.contrib.admin",  # Admin panel (we'll use this to inspect data)
    "django.contrib.auth",  # User authentication system
    "django.contrib.contenttypes",  # Tracks which models exist
    "django.contrib.sessions",  # Server-side session storage
    "django.contrib.messages",  # One-time notification messages
    "django.contrib.staticfiles",  # Serves CSS/JS for admin panel
    # Third-party apps
    "rest_framework",  # Django REST Framework
    "corsheaders",  # CORS headers for frontend
    # Our apps
    "core",  # Data models (dimensions, facts)
    "api",  # REST API endpoints
]

# ---------------------------------------------------------------------------
# Middleware
# ---------------------------------------------------------------------------
# Middleware runs on EVERY request/response, in order.
# Think of it as a pipeline: request passes through each middleware
# on the way in, and the response passes back through on the way out.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",  # HTTPS redirects, etc.
    "corsheaders.middleware.CorsMiddleware",  # Must be before CommonMiddleware
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",  # CSRF protection
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ---------------------------------------------------------------------------
# URLs and WSGI
# ---------------------------------------------------------------------------
# Points to the root URL configuration file.
ROOT_URLCONF = "config.urls"

# WSGI (Web Server Gateway Interface) is how Python web servers talk
# to Python web apps. This tells the server where our app is.
WSGI_APPLICATION = "config.wsgi.application"

# ---------------------------------------------------------------------------
# Templates (needed for admin panel)
# ---------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------
# Reads connection details from environment variables (which come from .env).
# This is how the same code works on your laptop, in CI, and in production —
# each environment has a different .env file.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB", default="epp_dev"),
        "USER": env("POSTGRES_USER", default="epp_user"),
        "PASSWORD": env("POSTGRES_PASSWORD", default="epp_secret"),
        "HOST": env("POSTGRES_HOST", default="localhost"),
        "PORT": env.int("POSTGRES_PORT", default=5432),
    }
}

# ---------------------------------------------------------------------------
# Internationalization
# ---------------------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"  # Always store times in UTC — convert for display
USE_I18N = False  # We don't need translation support
USE_TZ = True  # Store timezone-aware datetimes

# ---------------------------------------------------------------------------
# Static files (CSS, JavaScript for admin panel)
# ---------------------------------------------------------------------------
STATIC_URL = "static/"

# ---------------------------------------------------------------------------
# Default primary key type
# ---------------------------------------------------------------------------
# BigAutoField = auto-incrementing 64-bit integer. Handles billions of rows.
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---------------------------------------------------------------------------
# Django REST Framework
# ---------------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 50,
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",  # JSON responses
        "rest_framework.renderers.BrowsableAPIRenderer",  # HTML interface at each endpoint
    ],
}

# ---------------------------------------------------------------------------
# CORS
# ---------------------------------------------------------------------------
# Allow the React dev server to call our API.
# Vite runs on port 5173 by default.
CORS_ALLOWED_ORIGINS = env.list(
    "CORS_ALLOWED_ORIGINS",
    default=["http://localhost:5173"],
)
