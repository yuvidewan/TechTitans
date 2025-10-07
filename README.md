Behavioral Biometrics for Fraud Detection
This project develops a multi-layered fraud detection system for loan applications based on behavioral biometrics. It uses machine learning to analyze user behavior through keystroke dynamics and mouse movements to distinguish between genuine users, human fraudsters, and automated bots.

This system is designed to meet the goals of the "Social Impact" problem statement by protecting students from identity theft, building trust in digital platforms, and supporting financial inclusion.

Models Included
The system uses a multi-model "committee of specialists" approach for robust and explainable fraud detection:

Keystroke User Verification (XGBoost):

Purpose: Verifies the identity of a known user by analyzing their unique typing rhythm.

Algorithm: XGBoost Classifier.

Scripts: keystroke_model.py, predict_user.py

Keystroke Anomaly Detection (Human vs. Bot):

Purpose: Determines if a typing pattern is consistent with a human or is anomalous (e.g., a bot).

Algorithm: Isolation Forest.

Scripts: train_anomaly_detector.py, predict_anomaly.py

Mouse Movement Anomaly Detection (Human vs. Bot):

Purpose: Determines if mouse movements are organic and human-like or suspicious and bot-like.

Algorithm: Isolation Forest.

Scripts: train_mouse_anomaly.py, predict_mouse_anomaly.py

Setup Instructions
Follow these steps to set up the project environment.

1. Clone the Repository
Clone this repository to your local machine.

git clone [https://github.com/yuvidewan/TechTitans.git](https://github.com/yuvidewan/TechTitans.git)
cd TechTitans

2. Create a Virtual Environment
It is highly recommended to use a virtual environment to manage project dependencies.

# For Windows
python -m venv env1

# Activate the environment
.\env1\Scripts\activate

3. Install Dependencies
Install all the required Python libraries using the requirements.txt file.

pip install -r requirements.txt

4. Add Datasets
This project requires two data files. You must download them and place them in the root directory of this project:

keyboard_data.csv: The keystroke dynamics dataset.

Test_Mouse.csv: The mouse movement event log.

Note: You may need to update the filenames inside the Python scripts to match the names of your data files.

How to Run the Scripts
Make sure your virtual environment is activated before running any scripts.

Keystroke Models
To train the Keystroke User Verification model:

python keystroke_model.py

To test the trained Keystroke User Verification model:

python predict_user.py

To train the Keystroke Anomaly (Human vs. Bot) model:

python train_anomaly_detector.py

To test the Keystroke Anomaly model:

python predict_anomaly.py

Mouse Model
To train the Mouse Anomaly (Human vs. Bot) model:
This script will first process the raw mouse data to extract features and then train the model.

python train_mouse_anomaly.py

To test the Mouse Anomaly model:

python predict_mouse_anomaly.py
