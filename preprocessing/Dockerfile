# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the preprocessing script into the container
COPY preprocess.py /app/

# Install necessary Python dependencies
RUN pip install pandas scikit-learn

# Set the default command to run the preprocessing script
CMD ["python", "preprocess.py"]
