import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
import joblib
import warnings
from mouse_feature_extractor import extract_mouse_features

warnings.filterwarnings('ignore')

def train_mouse_model(raw_data_filename: str):
    """
    Processes a raw mouse event log, extracts features for each session,
    and trains an Isolation Forest model on those features.

    Args:
        raw_data_filename (str): Path to the CSV file with raw mouse event logs.
    """
    # --- 1. Load Raw Data ---
    print(f"Loading raw mouse data from '{raw_data_filename}'...")
    try:
        raw_df = pd.read_csv(raw_data_filename)
    except FileNotFoundError:
        print(f"Error: The file '{raw_data_filename}' was not found.")
        return
    print(f"Loaded {len(raw_df)} events.")

    # --- 2. Extract Features for Each Session ---
    print("\nExtracting features for each session... (This may take a moment)")
    # Group the data by user and session, then apply the feature extractor to each group
    all_features = []
    # Using 'uid' as we assume one session per user in this example dataset structure.
    # If a user could have multiple sessions, you would group by ['uid', 'session_id'].
    for user_id, session_df in raw_df.groupby('uid'):
        features = extract_mouse_features(session_df)
        features['uid'] = user_id  # Keep track of the user
        all_features.append(features)
    
    # Combine all the single-row feature DataFrames into one big DataFrame
    features_df = pd.concat(all_features, ignore_index=True)
    print(f"Successfully extracted features for {len(features_df)} unique user sessions.")
    
    # Prepare data for the model (drop the user ID)
    X = features_df.drop('uid', axis=1)

    # --- 3. Scale the Features ---
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("Mouse features have been scaled.")

    # --- 4. Train the Anomaly Detection Model ---
    print("\nTraining the Mouse Anomaly model (Isolation Forest)...")
    anomaly_model = IsolationForest(contamination='auto', random_state=42, n_jobs=-1)
    anomaly_model.fit(X_scaled)
    print("Model training complete.")

    # --- 5. Save the Model and Scaler ---
    joblib.dump(anomaly_model, 'models/mouse_anomaly_model.pkl')
    joblib.dump(scaler, 'models/mouse_scaler.pkl')
    print("\nMouse anomaly detection model and scaler have been saved to .pkl files.")


if __name__ == '__main__':
    # Make sure you have a CSV file with the raw mouse data in this folder
    # The file should have columns: uid, session_id, timestamp, event_type, screen_x, screen_y
    RAW_MOUSE_DATA_FILENAME = 'models/Test_Mouse.csv' 
    train_mouse_model(RAW_MOUSE_DATA_FILENAME)
