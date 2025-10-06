import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
import joblib
import warnings

warnings.filterwarnings('ignore')

def train_anomaly_model(csv_filename: str):
    """
    Trains an Isolation Forest model on the keystroke data to detect anomalies.

    Args:
        csv_filename (str): The path to the CSV file with normal human keystroke data.
    """
    # --- 1. Load the Data ---
    print(f"Loading data from '{csv_filename}'...")
    try:
        df = pd.read_csv(csv_filename)
        # We only need the timing features for this model
        features_df = df.drop(['subject', 'sessionIndex', 'rep'], axis=1)
    except FileNotFoundError:
        print(f"Error: The file '{csv_filename}' was not found.")
        return
    print("Data loaded successfully.")

    # --- 2. Scale the Features ---
    # It's crucial to scale data for distance-based algorithms like this
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(features_df)
    print("Features have been scaled.")

    # --- 3. Train the Isolation Forest Model ---
    print("\nTraining the Anomaly Detection model (Isolation Forest)...")
    # contamination='auto' is a good starting point. It lets the model decide
    # the threshold for what constitutes an anomaly.
    # A random_state ensures the results are reproducible.
    anomaly_model = IsolationForest(contamination='auto', random_state=42, n_jobs=-1)
    
    # We train the model on ALL the available human data
    anomaly_model.fit(X_scaled)
    print("Model training complete.")

    # --- 4. Save the Model and Scaler ---
    joblib.dump(anomaly_model, 'anomaly_detection_model.pkl')
    joblib.dump(scaler, 'anomaly_scaler.pkl') # Use a different name to not overwrite the other scaler
    print("\nAnomaly detection model and its scaler have been saved to .pkl files.")
    print("You can now use these to detect non-human typing patterns.")


def test_anomaly_predictions(csv_filename: str):
    """
    Loads the trained anomaly model and tests it on a normal sample and a
    synthetically generated "bot" sample.
    """
    print("\n--- Testing Anomaly Predictions ---")
    try:
        # Load the saved model and scaler
        model = joblib.load('anomaly_detection_model.pkl')
        scaler = joblib.load('anomaly_scaler.pkl')
        
        # --- Create a NORMAL test sample (from the original data) ---
        full_df = pd.read_csv(csv_filename)
        normal_sample = full_df.iloc[[50]].drop(['subject', 'sessionIndex', 'rep'], axis=1)
        
        # --- Create an ANOMALOUS (bot-like) test sample ---
        # A bot would have very fast, unnaturally consistent timings.
        bot_data = {col: [0.01] for col in normal_sample.columns} # All timings are exactly 0.01s
        bot_sample = pd.DataFrame(bot_data)

    except FileNotFoundError:
        print("Error: Could not find required files (.pkl or .csv). Please run the training function first.")
        return

    # --- 1. Test the NORMAL Sample ---
    normal_scaled = scaler.transform(normal_sample)
    normal_prediction = model.predict(normal_scaled)
    
    print("\nPrediction for NORMAL (Human) Sample:")
    print(f"Input Data: A real sample from user '{full_df.iloc[50]['subject']}'")
    print(f"Model Output: {normal_prediction[0]}")
    print(f"Interpretation: {'This is a NORMAL pattern (Human).' if normal_prediction[0] == 1 else 'This is an ANOMALY (Potential Bot).'}")

    # --- 2. Test the ANOMALOUS Sample ---
    bot_scaled = scaler.transform(bot_sample)
    bot_prediction = model.predict(bot_scaled)

    print("\nPrediction for ANOMALOUS (Bot) Sample:")
    print("Input Data: Synthetically generated bot-like timings.")
    print(f"Model Output: {bot_prediction[0]}")
    print(f"Interpretation: {'This is a NORMAL pattern (Human).' if bot_prediction[0] == 1 else 'This is an ANOMALY (Potential Bot).'}")


if __name__ == '__main__':
    DATASET_FILENAME = 'keyboard_data.csv'
    
    # Step 1: Train and save the model
    train_anomaly_model(DATASET_FILENAME)
    
    # Step 2: Run a test to see it in action
    test_anomaly_predictions(DATASET_FILENAME)
