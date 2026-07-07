# LeadFlow.AI - Enterprise Autonomous SDR & Cloud Web Agency Dockerfile
# Optimized for Render, Railway, AWS EC2, and VPS deployment
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Prevent Python from writing pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# Install git and essential system utilities for CloudDeploymentEngine
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# Create necessary directories for runtime output
RUN mkdir -p generated_sites/live_demos generated_sites/handover_packages uploads

# Expose server port
EXPOSE 8000

# Healthcheck to verify FastAPI backend responsiveness
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/docs || exit 1

# Launch Uvicorn high-performance async server
CMD ["uvicorn", "web_app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
