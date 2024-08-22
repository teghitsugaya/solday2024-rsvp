#FROM python:3.10-slim
FROM python:3.9.18-slim as build

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy application code
COPY . .

# Expose port and run the application
EXPOSE 5000
CMD ["python", "app.py"]

