# Use official Python image as base
FROM python:3.11-buster

# Set working directory inside container
WORKDIR /app

# Copy application files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for FastAPI
EXPOSE 8000

# Run FastAPI app (Updated path)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
