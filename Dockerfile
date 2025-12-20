FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install system dependencies required for PostgreSQL client libraries (e.g. psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
 && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r /app/requirements.txt

# Copy application code
COPY . /app

# Default port (can be overridden at runtime)
ENV PORT=8000
EXPOSE 8000

# Default start command — change to your project's entry point if needed
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
