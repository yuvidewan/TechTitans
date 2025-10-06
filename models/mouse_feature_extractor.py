import pandas as pd
import numpy as np

def calculate_distance(x1, y1, x2, y2):
    """Calculates the Euclidean distance between two points."""
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def extract_mouse_features(session_df: pd.DataFrame) -> pd.DataFrame:
    """
    Processes a DataFrame of raw mouse event logs for a single session and
    extracts a set of behavioral features.

    Args:
        session_df (pd.DataFrame): DataFrame containing mouse events for one session,
                                   sorted by timestamp.

    Returns:
        pd.DataFrame: A single-row DataFrame containing the calculated features.
    """
    if session_df.empty:
        return pd.DataFrame()

    # Sort by timestamp to ensure correct order
    session_df = session_df.sort_values('timestamp').reset_index(drop=True)

    # --- Basic Metrics ---
    start_time = session_df['timestamp'].min()
    end_time = session_df['timestamp'].max()
    duration_seconds = (end_time - start_time) / 1000.0
    
    clicks = session_df[session_df['event_type'] == 5]  # Assuming 5 is a click
    moves = session_df[session_df['event_type'] == 2]   # Assuming 2 is a move
    
    num_clicks = len(clicks)
    num_moves = len(moves)

    # --- Movement Metrics ---
    total_distance = 0
    velocities = []
    
    # Calculate distance and velocity between consecutive move points
    if len(moves) > 1:
        for i in range(1, len(moves)):
            prev = moves.iloc[i-1]
            curr = moves.iloc[i]
            
            dist = calculate_distance(prev['screen_x'], prev['screen_y'], curr['screen_x'], curr['screen_y'])
            time_delta = (curr['timestamp'] - prev['timestamp']) / 1000.0
            
            if time_delta > 0:
                total_distance += dist
                velocities.append(dist / time_delta)

    avg_velocity = np.mean(velocities) if velocities else 0
    std_velocity = np.std(velocities) if velocities else 0
    
    # --- Straightness Metric (Bots move in straighter lines) ---
    if len(moves) > 1:
        start_point = moves.iloc[0]
        end_point = moves.iloc[-1]
        direct_distance = calculate_distance(start_point['screen_x'], start_point['screen_y'], end_point['screen_x'], end_point['screen_y'])
        
        # Ratio of direct distance to path traveled. Closer to 1 is a straighter line.
        straightness = direct_distance / total_distance if total_distance > 0 else 1.0
    else:
        straightness = 1.0

    features = {
        'duration_seconds': duration_seconds,
        'num_clicks': num_clicks,
        'num_moves': num_moves,
        'total_distance': total_distance,
        'avg_velocity_pixels_per_sec': avg_velocity,
        'std_dev_velocity': std_velocity,
        'straightness': straightness
    }
    
    return pd.DataFrame([features])

if __name__ == '__main__':
    # This is an example of how to use the feature extractor
    print("--- Running Mouse Feature Extractor Example ---")
    
    # Load some sample raw mouse data
    # In a real scenario, you would load your full mouse dataset here
    data = {
        'uid': ['user1']*10,
        'session_id': ['sessionA']*10,
        'timestamp': [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900],
        'event_type': [2, 2, 5, 2, 2, 2, 5, 2, 2, 2],
        'screen_x': [10, 25, 25, 40, 60, 85, 85, 110, 140, 175],
        'screen_y': [10, 20, 20, 30, 45, 65, 65, 90, 120, 155]
    }
    sample_session_df = pd.DataFrame(data)
    
    print("\nSample Raw Mouse Data (1 session):")
    print(sample_session_df.head())
    
    # Extract features for this single session
    extracted_features = extract_mouse_features(sample_session_df)
    
    print("\nExtracted Feature Set:")
    print(extracted_features)
