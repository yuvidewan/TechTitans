import pandas as pd
import joblib
import numpy as np
import warnings

warnings.filterwarnings('ignore')

def check_typing_pattern(sample_data: pd.DataFrame):
    """
    Loads the trained anomaly detection model and predicts whether a given
    typing sample is normal (human) or an anomaly (potential bot).

    Args:
        sample_data (pd.DataFrame): A DataFrame with a single row of keystroke data.
    """
    try:
        # Load the trained model and its specific scaler
        model = joblib.load('models/anomaly_detection_model.pkl')
        scaler = joblib.load('models/anomaly_scaler.pkl')
    except FileNotFoundError:
        print("Error: Could not find the required .pkl files.")
        print("Please run the 'train_anomaly_detector.py' script first to generate the model files.")
        return

    # --- 1. Prepare and Scale the Data ---
    # Apply the same scaling transformation used during training
    sample_scaled = scaler.transform(sample_data)

    # --- 2. Make the Prediction ---
    prediction = model.predict(sample_scaled)
    # The 'decision_function' gives a score. Negative values are more likely to be anomalies.
    anomaly_score = model.decision_function(sample_scaled)

    # --- 3. Interpret and Display the Result ---
    print("\n--- Anomaly Detection Result ---")
    print(f"Anomaly Score: {anomaly_score[0]:.4f} (Negative scores are more anomalous)")
    
    if prediction[0] == 1:
        print("Prediction: NORMAL Pattern")
        print("Interpretation: The typing behavior is consistent with a human user.")
    else:
        print("Prediction: ANOMALY DETECTED")
        print("Interpretation: The typing behavior is suspicious and could be a bot.")


if __name__ == '__main__':
    # =========================================================================
    # ==  You can test the model with different types of input data below.   ==
    # =========================================================================
    
    # --- Example 1: Test with a REAL HUMAN sample ---
    # We'll borrow a sample from the original dataset to simulate a normal user.
    try:
        full_df = pd.read_csv('models/keyboard_data.csv')
        human_sample = full_df.iloc[[250]].drop(['subject', 'sessionIndex', 'rep'], axis=1)
        
        print("--- Checking a sample from a REAL HUMAN USER ---")
        check_typing_pattern(human_sample)

    except FileNotFoundError:
        print("Error: Could not load 'DSL-StrongPasswordData.csv' to create a human sample for testing.")
        print("Please ensure the dataset file is in the directory.")

    print("\n" + "="*50 + "\n")

    # --- Example 2: Test with a fake BOT sample ---
    # A bot would have unnaturally fast and consistent timings.
    # We create a new DataFrame with the correct column names for the bot sample.
    bot_data = {col: [0.015] for col in human_sample.columns}
    bot_sample = pd.DataFrame(bot_data)
    
    print("--- Checking a sample from a simulated BOT ---")
    check_typing_pattern(bot_sample)
