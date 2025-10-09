from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import os
from dotenv import load_dotenv

# --- CONFIGURATION ---
# IMPORTANT: PASTE THE SAME AZURE KEY AND ENDPOINT YOU'VE BEEN TRYING TO USE.
# Let's test these credentials in the simplest way possible.
load_dotenv()
AZURE_FACE_KEY =os.getenv("AZURE_FACE_KEY")
AZURE_FACE_ENDPOINT = os.getenv("AZURE_FACE_ENDPOINT")

# --- Main Test Logic ---

def test_azure_credentials(endpoint, key):
    """
    A simple function to test if the provided credentials are valid.
    This version uses the most basic API call available for maximum compatibility.
    """
    print("--- Attempting to Authenticate with Azure ---")
    print(f"Using Endpoint: {endpoint}")

    try:
        # 1. Create the client object.
        credentials = CognitiveServicesCredentials(key)
        client = FaceClient(endpoint, credentials)

        # 2. Make the most basic API call possible: list Face Lists.
        # This is a fundamental function and will work if your credentials are valid.
        # It doesn't require any other setup.
        client.face_list.list()
        
        print("\n✅ SUCCESS! Authentication successful.")
        print("Your API Key and Endpoint are correct.")
        print("You can now copy these exact values into the main verification script.")

    except Exception as e:
        print("\n❌ FAILED! Authentication failed.")
        print(f"Error details: {e}")
        print("\n--- FINAL TROUBLESHOOTING STEP ---")
        print("The error is almost certainly the Endpoint URL.")
        print("1. Go to your Face resource in the Azure Portal.")
        print("2. On the left menu, click on 'Keys and Endpoint'.")
        print("3. On that page, there is a field called 'Endpoint'. Copy its value.")
        print("   The correct URL will look like: https://centralindia.api.cognitive.microsoft.com/")
        print("   It will NOT contain 'techtitans-yuvraj-face'.")
        print("4. Paste that correct URL into the AZURE_FACE_ENDPOINT variable above.")
        print("5. Also, re-copy 'KEY 1' into the AZURE_FACE_KEY variable.")

# --- Script Execution ---

if __name__ == "__main__":
    if AZURE_FACE_KEY == "PASTE_YOUR_FACE_API_KEY_HERE" or AZURE_FACE_ENDPOINT == "PASTE_YOUR_FACE_API_ENDPOINT_HERE":
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!! ERROR: Please update the AZURE_FACE_KEY and               !!!")
        print("!!!        AZURE_FACE_ENDPOINT variables in this script.      !!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        test_azure_credentials(AZURE_FACE_ENDPOINT, AZURE_FACE_KEY)

