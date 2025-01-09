from fastapi import FastAPI
import joblib
from pydantic import BaseModel
from typing import List

# Path to the trained model
MODEL_PATH = "/models/model.joblib"

# Load the trained model
model = joblib.load(MODEL_PATH)

# Create the FastAPI app
app = FastAPI()

# Input schema for prediction
class PredictionRequest(BaseModel):
    features: List[float]

@app.get("/")
async def read_root():
    return {"message": "Welcome to the ML API. Use /predict endpoint to make predictions."}

@app.post("/predict")
async def predict(request: PredictionRequest):
    # Use the model to make predictions
    features = [request.features]  # Wrap features in a 2D list
    prediction = model.predict(features)
    return {"prediction": prediction.tolist()}
