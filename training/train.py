import pandas as pd
from sklearn.linear_model import LogisticRegression
import os
import joblib

# File paths
PROCESSED_DATA_PATH = "/data/processed_data.csv"
MODEL_PATH = "/models/model.joblib"

def train_model():
    # Check if processed data exists
    if not os.path.exists(PROCESSED_DATA_PATH):
        print(f"Error: {PROCESSED_DATA_PATH} not found!")
        return

    print(f"Loading processed data from {PROCESSED_DATA_PATH}...")
    try:
        data = pd.read_csv(PROCESSED_DATA_PATH)
    except pd.errors.EmptyDataError:
        print("Error: Processed data file is empty!")
        return

    # Split into features and target
    print("Splitting data into features and target...")
    features = data.iloc[:, :-1]
    target = data.iloc[:, -1]

    if target.nunique() < 2:
        print("Error: Data must have at least two classes in the target variable!")
        return

    # Train logistic regression model
    print("Training logistic regression model...")
    model = LogisticRegression()

    try:
        model.fit(features, target)
    except Exception as e:
        print(f"Error during model training: {e}")
        return

    # Save the trained model
    print(f"Saving model to {MODEL_PATH}...")
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    try:
        joblib.dump(model, MODEL_PATH)
    except Exception as e:
        print(f"Error saving the model: {e}")
        return

    print("Model training completed successfully.")

if __name__ == "__main__":
    train_model()
