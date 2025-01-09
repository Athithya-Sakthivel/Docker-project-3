import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# File paths
RAW_DATA_PATH = "/data/raw_data.csv"
PROCESSED_DATA_PATH = "/data/processed_data.csv"

def preprocess_data():
    # Load raw data
    print(f"Loading raw data from {RAW_DATA_PATH}...")
    try:
        raw_data = pd.read_csv(RAW_DATA_PATH)
    except FileNotFoundError:
        print("Error: Raw data file not found!")
        return

    # Drop rows with missing values
    print("Cleaning data by dropping rows with NaN values...")
    cleaned_data = raw_data.dropna()

    # Separate features and target
    print("Separating features and target...")
    features = cleaned_data.iloc[:, :-1]  # All columns except the last one
    target = cleaned_data.iloc[:, -1]    # Last column (assumed to be the target)

    # Normalize only the features
    print("Normalizing features...")
    scaler = MinMaxScaler()
    normalized_features = pd.DataFrame(
        scaler.fit_transform(features), 
        columns=features.columns
    )

    # Combine normalized features and target
    processed_data = pd.concat([normalized_features, target], axis=1)

    # Save the processed data
    print(f"Saving processed data to {PROCESSED_DATA_PATH}...")
    processed_data.to_csv(PROCESSED_DATA_PATH, index=False)

    # Log a preview of processed data
    print("Processed data preview:")
    print(processed_data.head())

    print("Data preprocessing completed successfully.")

if __name__ == "__main__":
    preprocess_data()
