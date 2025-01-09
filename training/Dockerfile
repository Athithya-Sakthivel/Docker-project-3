# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the training script into the container
COPY train.py /app/

# Install necessary Python dependencies
RUN pip install joblib scikit-learn numpy pandas

# Set the default command to run the training script
CMD ["python", "train.py"]
