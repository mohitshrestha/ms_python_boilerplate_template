# -------------------------
# Stage 1: Builder stage
# -------------------------
FROM python:{{ _python_version }}-slim AS builder

# Set working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install uv + uv_build
RUN pip install --upgrade pip \
    && pip install --no-cache-dir uv uv_build

# Copy only project metadata for dependency installation
COPY pyproject.toml /app/

# Create UV virtual environment and install dependencies
RUN uv venv \
    && uv pip install --no-cache-dir -e .

# -------------------------
# Stage 2: Production stage
# -------------------------
FROM python:{{ _python_version }}-slim

# Create non-root user
RUN groupadd --gid 1000 appuser \
    && useradd --uid 1000 --gid appuser --shell /bin/bash --create-home appuser

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /app/.venv /app/.venv

# Copy only necessary source code and configuration
COPY src /app/src
COPY shared/src /app/shared/src
COPY .env* README.md /app/

# Set environment variables
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH=/app/src:/app/shared/src
ENV PYTHONUNBUFFERED=1

# Switch to non-root user
USER appuser

# Default command (can be overridden in docker-compose)
CMD ["uv", "run", "main"]
