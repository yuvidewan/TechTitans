Human vs. Bot Anomaly Detection Model
This script trains a model to distinguish between normal human typing patterns and anomalous (e.g., bot-like) patterns. This creates a powerful security layer for your application.

Why This Approach is Better
Instead of trying to guess what every possible type of bot might look like, we teach the model a very strict definition of "normal human typing." Anything that doesn't fit this learned pattern is flagged as a potential threat.

We use the Isolation Forest algorithm, which is excellent for this task. It works by randomly "isolating" individual data points. Anomalies are easier to isolate and are therefore detected as being different from the normal data points.

How to Use
Install Libraries: Ensure you have the necessary libraries installed.

pip install pandas scikit-learn joblib

Place Files: Make sure your dataset CSV file (e.g., DSL-StrongPasswordData.csv) is in the same folder as the Python script (train_anomaly_detector.py).

Run the Script: Execute the script from your terminal:

python train_anomaly_detector.py

What the Script Does
Trains the Model: It loads all your human typing data, scales it, and trains an IsolationForest model on it. It then saves the trained model as anomaly_detection_model.pkl and its scaler as anomaly_scaler.pkl.

Runs a Test: After training, it automatically runs a test to show you how the model works:

It tests a real sample from your dataset.

It tests a synthetically created "bot" sample with unnaturally perfect timings.

Understanding the Output
The model's prediction is simple:

Prediction: 1 means the data is Normal (Inlier). The model is confident this looks like a human typing pattern.

Prediction: -1 means the data is an Anomaly (Outlier). The model flags this as a suspicious pattern that does not look like the human data it was trained on.

Your New Two-Layer Security System
You now have two powerful models that work together:

Anomaly Detector (Is it Human?): First, you check if the typing pattern is human-like. If this model outputs -1, you can immediately flag the session as high-risk or block it.

User Verifier (Which Human is it?): If the anomaly detector confirms the pattern is human (1), you then pass the data to your XGBoost model to verify if it's the correct human.

This two-step process is much more secure and robust.