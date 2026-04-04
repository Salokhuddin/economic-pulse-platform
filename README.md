# Economic Pulse Platform

A real-time economic intelligence system that ingests data from 10+ free public APIs, stores raw data in a data lake, transforms it into a dimensional data warehouse, and serves it through a universal REST API.

## Tech Stack

- **Backend:** Django 5 + Django REST Framework
- **Database:** PostgreSQL 16
- **CI/CD:** GitHub Actions
- **Testing:** pytest + pytest-django

## Quick Start

### Prerequisites

- Python 3.10+
- Docker Desktop
- Git

### Setup
```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/economic-pulse-platform.git
cd economic-pulse-platform

# Create and activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -e ".[dev]"

# Copy environment variables
copy .env.example .env

# Start PostgreSQL
docker compose -f docker/docker-compose.yml up -d

# Run migrations
cd backend
python manage.py migrate

# Run tests
pytest

# Start the dev server
python manage.py runserver
```

The API will be available at http://localhost:8000/api/v1/health/

## Development
```bash
# Run linter
ruff check backend/

# Run tests with coverage
cd backend && pytest --cov=. --cov-report=term-missing
