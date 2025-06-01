# backend/Dockerfile
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install netcat for wait-for script
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Django code
COPY . .

# Make the wait script executable
RUN chmod +x wait-for-it.sh

# Run the server (can be overridden by docker-compose)
CMD ["sh", "-c", "./wait-for-it.sh db -- python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]


