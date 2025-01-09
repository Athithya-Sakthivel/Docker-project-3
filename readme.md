# Dockerized ML Pipeline

This repository contains a fully dockerized pipeline for training and serving a machine learning model. The pipeline is designed to preprocess data, train a logistic regression model, and serve predictions via a FastAPI web application.

## Overview

This project demonstrates a machine learning workflow wrapped in Docker containers. It performs the following steps:

1. **Preprocessing**: Processes raw data into a usable format.
2. **Training**: Trains a logistic regression model using the processed data.
3. **Serving**: Serves predictions through an API endpoint using FastAPI.

## Project Structure

```
.
|-- Makefile                 # Commands for building, running, and cleaning up the pipeline
|-- docker-compose.yml       # Orchestrates the containers for each pipeline stage
|-- data/                    # Directory for raw and processed data
|   |-- raw_data.csv
|   |-- processed_data.csv
|-- preprocessing/           # Preprocessing stage
|   |-- Dockerfile
|   |-- preprocess.py
|-- training/                # Training stage
|   |-- Dockerfile
|   |-- train.py
|-- serving/                 # Serving stage
|   |-- Dockerfile
|   |-- serve.py
|   |-- requirements.txt
|-- requirements.txt         # Python dependencies for the project
```

## Pipeline Stages

### 1. Preprocessing

- Reads raw data from `data/raw_data.csv`.
- Processes the data and saves the result in `data/processed_data.csv`.

### 2. Training

- Reads the processed data from `data/processed_data.csv`.
- Trains a logistic regression model and saves it to `models/model.joblib`.

### 3. Serving

- Exposes a FastAPI-based HTTP endpoint on port 8000 for predictions.
- `/predict` endpoint accepts JSON data with features and returns predictions.

## Usage

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Athithya-Sakthivel/Docker-project-3.git
   cd Docker-project-3
   ```

2. Install Docker and Docker Compose:

   - [Docker Installation Guide](https://docs.docker.com/get-docker/)
   - [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

### Run the Pipeline

1. Build and start the pipeline:

   ```bash
   docker-compose up --build
   ```

2. Stop the pipeline when done:

   ```bash
   docker-compose down
   ```

### Test the API

Once the pipeline is running, use the following steps to test the API:

1. Check the root endpoint:

   ```bash
   curl http://localhost:8000/
   ```

   **Response:**

   ```json
   {"message": "Welcome to the ML API. Use /predict endpoint to make predictions."}
   ```

2. Make a prediction:

   ```bash
   curl -X POST "http://localhost:8000/predict" \
   -H "Content-Type: application/json" \
   -d '{"features": [1.2, 3.4]}'
   ```

   **Response:**

   ```json
   {"prediction":[30.0]}
   ```



## Technologies Used

- **Docker**: Containerization of the pipeline stages.
- **Python**: Programming language used for preprocessing, training, and serving.
- **Scikit-learn**: Machine learning library for training the logistic regression model.
- **FastAPI**: Framework for serving predictions through an HTTP API.
- **Pandas**: Data manipulation library for preprocessing.

## Future Improvements

- **Add Data Validation**: Validate input data format and handle missing or incorrect values.
- **Extend Model Support**: Add support for other machine learning models.
- **Logging**: Integrate logging for better debugging and monitoring.
- **Automated Testing**: Add tests for each stage of the pipeline.

## Screenshots

![Screenshot (98)](https://github.com/user-attachments/assets/ea3104d8-ac7a-4770-bbc5-5608ecee6a37)
![Screenshot (99)](https://github.com/user-attachments/assets/c4dc5250-f520-4264-9c0c-caf4419bc3cf)
