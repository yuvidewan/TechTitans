import pandas as pd
import random
import numpy as np

def generate_training_data(num_records: int) -> pd.DataFrame:
    """
    Generates a DataFrame of simulated behavioral data for training.

    Args:
        num_records: The total number of records to generate.

    Returns:
        A pandas DataFrame with features and a target label.
    """
    data = []
    
    for _ in range(num_records):
        # Randomly decide if the record is fraudulent or not
        # 0 = Genuine, 1 = Fraud
        is_fraud = random.choice([0, 1]) 

        if is_fraud:
            # --- Fraudulent User Profile ---
            # High typing speed, often from pasting or bots
            typing_speed = random.uniform(2000, 6000) 
            # Low error rate, as content is often pasted
            error_rate = random.uniform(0.0, 0.05) 
            # High probability of a paste action
            has_paste_action = np.random.choice([0, 1], p=[0.2, 0.8]) 
             # Higher chance of a new or suspicious device
            is_new_device = np.random.choice([0, 1], p=[0.4, 0.6])
        else:
            # --- Genuine User Profile ---
            # Normal human typing speed (Characters Per Minute)
            typing_speed = random.uniform(250, 650)
            # Normal human error rate (making corrections with backspace)
            error_rate = random.uniform(0.05, 0.2)
            # Low probability of a paste action for sensitive fields
            has_paste_action = np.random.choice([0, 1], p=[0.95, 0.05])
            # Low chance of a new device
            is_new_device = np.random.choice([0, 1], p=[0.9, 0.1])

        record = {
            'avg_typing_speed_cpm': round(typing_speed, 2),
            'error_rate': round(error_rate, 4),
            'has_paste_action': has_paste_action,
            'is_new_device': is_new_device,
            'is_fraud': is_fraud
        }
        data.append(record)
        
    return pd.DataFrame(data)

# --- Main part of the script ---

# You can change this number to generate more or fewer samples
NUM_SAMPLES = 2000  
training_df = generate_training_data(NUM_SAMPLES)

# Save the generated data to a CSV file
output_filename = 'training_data.csv'
training_df.to_csv(output_filename, index=False)

print(f"Successfully generated {NUM_SAMPLES} records.")
print(f"Data saved to '{output_filename}'")
print("\nHere's a preview of the data:")
print(training_df.head())