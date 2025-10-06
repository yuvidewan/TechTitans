import time
from analytic import BehavioralAnalyzer
# --- Simulated Data ---

# Current time in milliseconds (to simulate frontend logging)
NOW_MS = int(time.time() * 1000)

# 1. Genuine Applicant Data (Slow, careful typing, no copy/paste)
genuine_logs = [
    {'timestamp': NOW_MS + 100, 'type': 'KEYSTROKE', 'key': 'A'},
    {'timestamp': NOW_MS + 350, 'type': 'KEYSTROKE', 'key': 'L'},
    {'timestamp': NOW_MS + 400, 'type': 'KEYSTROKE', 'key': 'L'},
    {'timestamp': NOW_MS + 420, 'type': 'KEYSTROKE', 'key': 'BACKSPACE'}, # A small correction
    {'timestamp': NOW_MS + 600, 'type': 'KEYSTROKE', 'key': 'I'},
    {'timestamp': NOW_MS + 900, 'type': 'KEYSTROKE', 'key': 'C'},
    {'timestamp': NOW_MS + 1100, 'type': 'KEYSTROKE', 'key': 'E'},
    # Total time: 1100 - 100 = 1000ms (1 second) for 6 valid characters + 1 backspace (7 total strokes)
]

# 2. Fraudulent Applicant Data (Rapid typing, instant copy/paste)
fraud_logs = [
    {'timestamp': NOW_MS + 100, 'type': 'PASTE', 'field_id': 'income_field'}, # INSTANT PASTE
    {'timestamp': NOW_MS + 150, 'type': 'KEYSTROKE', 'key': '1'},
    {'timestamp': NOW_MS + 170, 'type': 'KEYSTROKE', 'key': '2'},
    {'timestamp': NOW_MS + 190, 'type': 'KEYSTROKE', 'key': '3'},
    {'timestamp': NOW_MS + 210, 'type': 'KEYSTROKE', 'key': '4'},
    # Total time: 210 - 150 = 60ms for 4 keystrokes (very fast)
    {'timestamp': NOW_MS + 500, 'type': 'DEVICE_CHANGE', 'old_ip': '1.1.1.1', 'new_ip': '9.9.9.9'}, # IP/Device Inconsistency
]


# --- Run the Analyzer ---

genuine_analyzer = BehavioralAnalyzer(genuine_logs)
genuine_features = genuine_analyzer.get_behavioral_features()

fraud_analyzer = BehavioralAnalyzer(fraud_logs)
fraud_features = fraud_analyzer.get_behavioral_features()


print("\n--- Genuine Applicant Features ---")
print(genuine_features)
# Expected: Low speed, Low error, has_paste_action=0

print("\n--- Fraudulent Applicant Features ---")
print(fraud_features)
# Expected: High speed, has_paste_action=1, device_change_count > 0