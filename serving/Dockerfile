FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY serve.py /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the serving port
EXPOSE 8000

# Set the default command
CMD ["python", "serve.py"]
