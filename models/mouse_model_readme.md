Human vs. Bot Mouse Anomaly Model
Following the multi-model approach, these scripts create a specialized model to detect anomalies in mouse movement patterns. This will work alongside your keystroke model.

There are two main steps:

Step 1: Feature Engineering (mouse_feature_extractor.py)
The raw mouse data is a stream of (x, y) coordinates and timestamps. This isn't useful for a model directly. We must first convert this data into a meaningful summary of a user's session.

This script calculates key behavioral features, including:

Average Velocity: How fast the user typically moves the mouse.

Total Distance: How far the mouse traveled across the screen.

Straightness: A crucial metric. Humans move their mouse in curved, imperfect paths. Bots often move in perfectly straight lines. This feature measures the ratio of the direct-line distance to the actual path traveled. A score closer to 1 is more bot-like.

Click Count: How many times the user clicked.

Session Duration: The total time of the user's activity.

Step 2: Model Training (train_mouse_anomaly.py)
This script orchestrates the training process:

It loads your raw mouse event data CSV.

It uses the mouse_feature_extractor to process the raw data into the feature set described above for every user session.

It trains a new IsolationForest anomaly detection model on these features.

It saves the trained model as mouse_anomaly_model.pkl and its scaler as mouse_scaler.pkl.

How to Use
Prepare Your Data:

Save your raw mouse data into a CSV file. Make sure the column names match the format you provided (uid, session_id, timestamp, etc.).

Crucially, edit train_mouse_anomaly.py and change the RAW_MOUSE_DATA_FILENAME variable to match your file's name.

Place Files: Make sure mouse_analytic.py and mouse_feature_extractor.py are in the same folder as your mouse data CSV.

Run the Training Script:

python mouse_analytic.py

After running, you will have two new files (mouse_anomaly_model.pkl and mouse_scaler.pkl) ready to be used for prediction. Your next step will be to create a final script that uses both your keystroke and mouse models to make a combined fraud assessment.