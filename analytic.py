import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import warnings

# Ignore minor warnings to keep the output clean
warnings.filterwarnings('ignore')

def train_keystroke_model(csv_filename: str):
    """
    Loads keystroke data, trains a robust XGBoost classifier, 
    evaluates it, and saves the final model and scaler.

    Args:
        csv_filename (str): The path to the CSV file containing the keystroke data.
    """
    # --- 1. Load and Prepare the Data ---
    print(f"Loading data from '{csv_filename}'...")
    try:
        df = pd.read_csv(csv_filename)
    except FileNotFoundError:
        print(f"Error: The file '{csv_filename}' was not found.")
        print("Please make sure the CSV file is in the same directory as this script.")
        return

    print("Data loaded successfully. Shape:", df.shape)

    # Define features (X) and target (y)
    features = df.columns.drop(['subject', 'sessionIndex', 'rep'])
    X = df[features]
    y = df['subject']

    # --- 2. Encode Labels ---
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    
    # --- 3. Split Data into Training and Testing Sets ---
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.25, random_state=42, stratify=y_encoded
    )
    print(f"Training set size: {X_train.shape[0]} samples")
    print(f"Testing set size: {X_test.shape[0]} samples")

    # --- 4. Scale Numerical Features ---
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    print("Features have been scaled.")

    # --- 5. Train the XGBoost Model ---
    print("\nTraining the XGBoost model...")
    
    model = xgb.XGBClassifier(
        objective='multi:softmax',
        num_class=len(label_encoder.classes_),
        n_estimators=200,
        learning_rate=0.1,
        max_depth=5,
        use_label_encoder=False,
        eval_metric='mlogloss',
        n_jobs=-1,
        random_state=42
    )
    
    # The .fit method is now called without the 'callbacks' argument
    model.fit(X_train_scaled, y_train)
    
    print("\nModel training complete.")

    # --- 6. Evaluate the Model ---
    print("\n--- Model Evaluation ---")
    predictions = model.predict(X_test_scaled)
    
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    print("\nClassification Report:")
    report = classification_report(
        label_encoder.inverse_transform(y_test), 
        label_encoder.inverse_transform(predictions)
    )
    print(report)

    # --- 7. Visualize the Confusion Matrix ---
    print("Generating confusion matrix...")
    cm = confusion_matrix(y_test, predictions)
    plt.figure(figsize=(18, 15))
    sns.heatmap(cm, annot=False, fmt='d', cmap='Blues', 
                xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
    plt.title('Confusion Matrix - (Actual vs. Predicted Users)')
    plt.ylabel('Actual Subject')
    plt.xlabel('Predicted Subject')
    plt.savefig('confusion_matrix.png')
    print("Confusion matrix saved to 'confusion_matrix.png'")

    # --- 8. Save the Final Model and Helper Objects ---
    joblib.dump(model, 'final_keystroke_model.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    joblib.dump(label_encoder, 'label_encoder.pkl')
    print("\nFinal trained model, scaler, and label encoder have been saved to .pkl files.")
    print("You can now load these to make predictions on new data without retraining.")


if __name__ == '__main__':
    # =========================================================================
    # ==  IMPORTANT: Change this variable to the name of your CSV file       ==
    # =========================================================================
    DATASET_FILENAME = 'keyboard_data.csv'
    
    train_keystroke_model(DATASET_FILENAME)

