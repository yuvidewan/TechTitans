import pandas as pd
import joblib
from mouse_feature_extractor import extract_mouse_features
import warnings

warnings.filterwarnings('ignore')

def check_mouse_pattern(mouse_features_df: pd.DataFrame):
    """
    Loads the trained mouse anomaly model and predicts whether a given
    set of mouse features is normal (human) or an anomaly (potential bot).

    Args:
        mouse_features_df (pd.DataFrame): A DataFrame with a single row of
                                          extracted mouse features.
    """
    if mouse_features_df.empty:
        print("Warning: Input feature DataFrame is empty. Cannot make a prediction.")
        return

    try:
        # Load the trained mouse model and its specific scaler
        model = joblib.load('models/mouse_anomaly_model.pkl')
        scaler = joblib.load('models/mouse_scaler.pkl')
    except FileNotFoundError:
        print("Error: Could not find the required mouse .pkl files.")
        print("Please run 'train_mouse_anomaly.py' first to generate them.")
        return

    # --- 1. Prepare and Scale the Data ---
    sample_scaled = scaler.transform(mouse_features_df)

    # --- 2. Make the Prediction ---
    prediction = model.predict(sample_scaled)
    anomaly_score = model.decision_function(sample_scaled)

    # --- 3. Interpret and Display the Result ---
    print("\n--- Mouse Anomaly Detection Result ---")
    print(f"Anomaly Score: {anomaly_score[0]:.4f} (Negative scores are more anomalous)")
    
    if prediction[0] == 1:
        print("Prediction: NORMAL Pattern")
        print("Interpretation: Mouse movement is consistent with a human user.")
    else:
        print("Prediction: ANOMALY DETECTED")
        print("Interpretation: Mouse movement is suspicious and could be a bot.")


if __name__ == '__main__':
    # =========================================================================
    # ==  This script demonstrates how to use the trained mouse model.       ==
    # =========================================================================
    
    # --- Example 1: Test with a REAL HUMAN session ---
    try:
        raw_df = pd.read_csv('models/Test_Mouse.csv')
        # Get all events for the first user/session to simulate a real session
        human_session = raw_df[raw_df['uid'] == raw_df['uid'].iloc[0]]
        
        print("--- Checking a sample from a REAL HUMAN USER ---")
        # First, we must extract the features from the raw session data
        human_features = extract_mouse_features(human_session)
        print("Extracted features for the human session:")
        print(human_features)
        
        # Now, check the pattern
        check_mouse_pattern(human_features)

    except (FileNotFoundError, IndexError):
        print("Error: Could not load 'Test_Mouse.csv' to create a human sample.")
        print("Please ensure the dataset file is in the directory and is not empty.")

    print("\n" + "="*50 + "\n")

    # --- Example 2: Test with a fake BOT session ---
    # A bot has perfectly straight, fast movements.
    bot_features_data = {
        'duration_seconds': [2.5],
        'num_clicks': [1],
        'num_moves': [50],
        'total_distance': [800.0],
        'avg_velocity_pixels_per_sec': [320.0],
        'std_dev_velocity': [0.1],  # Very low standard deviation
        'straightness': [0.99]       # Almost a perfectly straight line
    }
    bot_features = pd.DataFrame(bot_features_data)
    
    print("--- Checking a sample from a simulated BOT ---")
    print("Generated features for the bot session:")
    print(bot_features)
    check_mouse_pattern(bot_features)
