# Use slim Python image for smaller footprint
FROM python:{{ _python_version }}-slim

# Set working directory inside the container
WORKDIR /app

# Copy only pyproject.toml first to leverage Docker cache
COPY pyproject.toml /app/

# Install pip and uv_build for building Python packages
RUN pip install --upgrade pip && pip install uv_build

# Copy the rest of the project into the container
COPY . /app

# Ensure Python outputs are immediately flushed
ENV PYTHONUNBUFFERED=1

# Optional: set PATH for scripts if needed
ENV PATH="/app/.venv/bin:$PATH"

# Default command to run the main entry point of the package
CMD ["python", "-m", "src.{{ _package_name }}.main"]
