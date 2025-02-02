# Use the official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Create empty quiz_data.json if it doesn't exist
RUN echo '{"terms": []}' > quiz_data.json

# Make port 8080 available
EXPOSE 8080

# Run the application with gunicorn
CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 server:app
