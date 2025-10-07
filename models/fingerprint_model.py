import pandas as pd
import joblib
import random
from faker import Faker
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from ipaddress import ip_address

# --- Configuration ---
# **IMPORTANT**: Update these paths to point to your TWO most important IP dataset files.
# This file should contain IP ranges mapped to an organization name (e.g., Cloudflare, Inc.)
ASN_FILE_PATH = "models/asn-ipv4.csv" 
# This file should contain IP ranges mapped to a country code (e.g., AU, CN)
COUNTRY_FILE_PATH = "models/geo-whois-asn-country-ipv4.csv"

# --- Part 1: IP Intelligence Database Loader (Upgraded for Multiple Files) ---

class IPIntelligence:
    """
    A class to load and query IP intelligence data from multiple source files.
    It merges ASN and Country data into a unified, fast lookup system.
    """
    def __init__(self, asn_filepath, country_filepath):
        self.ip_db = None
        try:
            print(f"Loading ASN data from: {asn_filepath}")
            asn_df = pd.read_csv(
                asn_filepath, 
                header=None, 
                names=['ip_start', 'ip_end', 'asn', 'organization'],
                # Use a more robust CSV engine for potentially large files
                engine='python', 
                on_bad_lines='skip'
            )

            print(f"Loading Country data from: {country_filepath}")
            country_df = pd.read_csv(
                country_filepath,
                header=None,
                names=['ip_start', 'ip_end', 'country_code'],
                engine='python',
                on_bad_lines='skip'
            )
            
            print("Merging IP intelligence data...")
            # We merge the two datasets based on the IP start and end ranges
            # This creates a single, unified DataFrame for lookups
            self.ip_db = pd.merge(asn_df, country_df, on=['ip_start', 'ip_end'], how='outer')

            # Convert IP strings to integers for fast searching
            self.ip_db['ip_start_int'] = self.ip_db['ip_start'].apply(lambda x: int(ip_address(x)))
            self.ip_db['ip_end_int'] = self.ip_db['ip_end'].apply(lambda x: int(ip_address(x)))
            # Fill any missing values that might result from the merge
            self.ip_db.fillna('Unknown', inplace=True)
            print("IP intelligence database loaded and merged successfully.")

        except FileNotFoundError as e:
            print(f"---! ERROR !--- IP intelligence file not found: {e.filename}")
            print("Please update the file paths at the top of the script.")
        except Exception as e:
            print(f"An error occurred while loading IP data: {e}")

    def lookup_ip(self, ip_str: str) -> dict:
        """Looks up an IP address in the merged database."""
        if self.ip_db is None:
            return {'organization': 'Unknown', 'ip_type': 'Unknown', 'country': 'Unknown'}

        try:
            ip_int = int(ip_address(ip_str))
            result = self.ip_db[
                (self.ip_db['ip_start_int'] <= ip_int) & 
                (self.ip_db['ip_end_int'] >= ip_int)
            ]

            if not result.empty:
                row = result.iloc[0]
                org = str(row['organization']).lower()
                country = str(row['country_code'])
                
                if any(kw in org for kw in ['cloud', 'hosting', 'datacenter', 'cdn', 'google', 'amazon', 'cloudflare']):
                    ip_type = 'Data Center'
                elif any(kw in org for kw in ['vpn', 'proxy']):
                    ip_type = 'VPN/Proxy'
                else:
                    ip_type = 'Residential/Mobile'
                return {'organization': org, 'ip_type': ip_type, 'country': country}
        except ValueError:
            pass
        return {'organization': 'Unknown', 'ip_type': 'Unknown', 'country': 'Unknown'}

# --- Part 2: Feature Engineering (IP + OS) ---

def get_combined_features(ip_str: str, user_agent: str, ip_lookup: IPIntelligence) -> dict:
    """Extracts features from both IP (using the database) and User-Agent."""
    features = {}
    ip_info = ip_lookup.lookup_ip(ip_str)
    
    # IP Features
    features['ip_type_datacenter'] = 1 if ip_info['ip_type'] == 'Data Center' else 0
    features['ip_type_residential'] = 1 if ip_info['ip_type'] == 'Residential/Mobile' else 0
    features['is_from_suspicious_country'] = 1 if ip_info['country'] in ['CN', 'RU', 'IR'] else 0

    # OS Features
    ua_lower = user_agent.lower()
    features['is_outdated_os'] = 1 if 'windows nt 6.1' in ua_lower else 0
    features['is_headless'] = 1 if 'headless' in ua_lower or 'puppeteer' in ua_lower else 0
    features['os_linux_server'] = 1 if 'linux' in ua_lower and 'android' not in ua_lower else 0
    
    return features

# --- Part 3: Model Training (Largely unchanged, now uses the more powerful features) ---

def train_device_intelligence_model(ip_intelligence_db: IPIntelligence):
    """Generates synthetic training data using the real IP database and trains a model."""
    print("\nGenerating synthetic training data using the merged IP database...")
    faker = Faker()
    records = []
    # Use the loaded database to generate more realistic training samples
    known_ips_df = ip_intelligence_db.ip_db.sample(2000, replace=True)

    for _, row in known_ips_df.iterrows():
        is_suspicious = random.choice([0, 1])
        
        if is_suspicious:
            ip = str(ip_address(random.randint(row['ip_start_int'], row['ip_end_int'])))
            ua = random.choice([
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/90.0.4430.212 Safari/537.36"
            ])
            label = 1
        else:
            ip = faker.ipv4_private()
            ua = faker.user_agent()
            label = 0

        features = get_combined_features(ip, ua, ip_intelligence_db)
        features['is_suspicious'] = label
        records.append(features)
        
    df = pd.DataFrame(records)
    print("Synthetic data generated.")

    target = 'is_suspicious'
    features_cols = [col for col in df.columns if col != target]
    X, y = df[features_cols], df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    
    print("\nTraining the XGBoost model for device intelligence...")
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
    model.fit(X_train, y_train)
    print("Model training complete.")
    
    joblib.dump(model, 'models/device_intelligence_model.pkl')
    print("Trained model saved to 'models/device_intelligence_model.pkl'")
    
    print("\n--- Model Evaluation ---")
    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions, target_names=['Trusted', 'Suspicious']))
    
    fig, ax = plt.subplots(figsize=(8, 8))
    ConfusionMatrixDisplay.from_predictions(y_test, predictions, display_labels=['Trusted', 'Suspicious'], cmap='Purples', ax=ax)
    ax.set_title('Device Intelligence Model Confusion Matrix')
    plt.show()

if __name__ == '__main__':
    # Initialize the IP database with paths to both files
    ip_db = IPIntelligence(
        asn_filepath=ASN_FILE_PATH,
        country_filepath=COUNTRY_FILE_PATH
    )
    
    if ip_db.ip_db is not None:
        train_device_intelligence_model(ip_intelligence_db=ip_db)
    else:
        print("\nHalting training due to missing or failed IP intelligence database loading.")

