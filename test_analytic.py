import pandas as pd
import joblib
import warnings

# Ignore minor warnings to keep the output clean
warnings.filterwarnings('ignore')

def predict_from_sample(sample_data: pd.DataFrame):
    """
    Loads the trained model and associated files to predict the user
    based on a new sample of keystroke data.

    Args:
        sample_data (pd.DataFrame): A DataFrame containing a single row of keystroke timing data.
    """
    try:
        # --- 1. Load the saved model, scaler, and label encoder ---
        print("Loading the trained model and helper files...")
        model = joblib.load('final_keystroke_model.pkl')
        scaler = joblib.load('scaler.pkl')
        label_encoder = joblib.load('label_encoder.pkl')
        print("Files loaded successfully.")

    except FileNotFoundError:
        print("Error: Could not find the required .pkl files.")
        print("Please make sure 'final_keystroke_model.pkl', 'scaler.pkl', and 'label_encoder.pkl' are in the same directory.")
        return

    # --- 2. Prepare the new sample data ---
    # Ensure the sample data has the same columns as the training data
    # (We assume the sample_data DataFrame is already structured correctly)
    
    # Apply the SAME scaling transformation that was used during training
    sample_scaled = scaler.transform(sample_data)
    print("\nNew sample data has been scaled.")

    # --- 3. Make the prediction ---
    print("Making a prediction...")
    prediction_encoded = model.predict(sample_scaled)
    
    # The model outputs a numerical prediction (e.g., [0])
    # We need to decode it back to the original subject ID (e.g., 's002')
    predicted_subject = label_encoder.inverse_transform(prediction_encoded)

    # --- 4. Display the result ---
    print("\n--- Prediction Result ---")
    print(f"The model predicts that this typing pattern belongs to: {predicted_subject[0]}")


if __name__ == '__main__':
    # =========================================================================
    # ==  This is a sample of new, unseen data.                              ==
    # ==  In a real application, this would come from the live user session. ==
    # =========================================================================
    
    # For this example, we'll just take the first row from your original dataset
    # to simulate a new login attempt.
    # IMPORTANT: You can replace this with any other row from your data to test.
    try:
        full_df = pd.read_csv('keyboard_data.csv')
        # Select a single row to test (e.g., the 100th row) and drop the labels
        new_sample = full_df.iloc[[1000]].drop(['subject', 'sessionIndex', 'rep'], axis=1)
        
        # Display the user this sample actually belongs to
        actual_user = full_df.iloc[1000]['subject']
        print(f"--- Testing with a sample from user: {actual_user} ---")

        # Call the prediction function
        predict_from_sample(new_sample)

    except FileNotFoundError:
        print("Error: The original dataset 'keyboard_data.csv' is needed to create a test sample.")
        print("Please ensure it is in the same directory.")
