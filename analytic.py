import time
import math
from typing import List, Dict, Any

class BehavioralAnalyzer:

    def __init__(self, raw_logs: List[Dict[str, Any]]):
        self.raw_logs = raw_logs
        self.features = {}

    def _calculate_typing_metrics(self):
        """
        Processes key-up/key-down logs to derive speed and error features.
        """
        keystrokes = [log for log in self.raw_logs if log['type'] == 'KEYSTROKE']
        
        if not keystrokes:
            self.features['avg_typing_speed_cpm'] = 0.0
            self.features['error_rate'] = 0.0
            return

        # 1. Total Time and Keystrokes
        start_time = min(k['timestamp'] for k in keystrokes)
        end_time = max(k['timestamp'] for k in keystrokes)
        total_time_seconds = (end_time - start_time) / 1000.0  # Convert ms to seconds
        total_keystrokes = len(keystrokes)
        
        # 2. Backspace/Error Count
        backspace_count = sum(1 for k in keystrokes if k.get('key') == 'BACKSPACE')
        
        # Calculate Features
        self.features['total_keystrokes'] = total_keystrokes
        self.features['total_time_seconds'] = total_time_seconds
        
        # Avg. Characters Per Minute (CPM)
        if total_time_seconds > 0:
            self.features['avg_typing_speed_cpm'] = (total_keystrokes / total_time_seconds) * 60
        else:
            self.features['avg_typing_speed_cpm'] = 0.0
            
        # Error Rate (ratio of backspaces to total keystrokes)
        if total_keystrokes > 0:
            self.features['error_rate'] = backspace_count / total_keystrokes
        else:
            self.features['error_rate'] = 0.0

    def _detect_suspicious_actions(self):
        """
        Detects binary fraud indicators like copying/pasting or rapid scrolling.
        """
        # Copy/Paste Detection
        paste_event = any(log for log in self.raw_logs if log['type'] == 'PASTE')
        self.features['has_paste_action'] = 1 if paste_event else 0

        # Device Consistency (Simulated - in a real app, this would check against a user history DB)
        device_changes = sum(1 for log in self.raw_logs if log['type'] == 'DEVICE_CHANGE')
        self.features['device_change_count'] = device_changes
        self.features['is_new_device'] = 1 if device_changes > 0 else 0


    def get_behavioral_features(self) -> Dict[str, float]:
        """
        Runs all feature extraction methods and returns the final feature set.
        """
        self._calculate_typing_metrics()
        self._detect_suspicious_actions()
        
        # Clean up and return
        final_features = {k: round(v, 4) if isinstance(v, float) else v for k, v in self.features.items()}
        return final_features