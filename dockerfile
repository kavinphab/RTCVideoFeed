# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to constrain resources
ENV PYTHONUNBUFFERED=1
ENV LIMIT_CPU="0.5"
ENV LIMIT_MEMORY="512m"

# Install necessary packages, including sysctl
RUN apt-get update && apt-get install -y \
    procps \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make /app directory as working directory
WORKDIR /app

# Make the startup script executable
RUN chmod +x startup.sh

# Run the shell script when the container launches
CMD ["./startup.sh"]
