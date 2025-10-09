import boto3
from dotenv import load_dotenv
import os
import io
from PIL import Image
import requests

load_dotenv()

# --- DEMO IMAGES ---
# In a real application, you would get these image files from a web request.
# For this demo, we'll use placeholder images from the web.
ID_CARD_IMAGE_URL = "https://placehold.co/400x400/003049/FFFFFF?text=ID+Card"
LIVE_SELFIE_IMAGE_URL = "https://placehold.co/400x400/D62828/FFFFFF?text=Live+Selfie"
# An image of a different person for testing failed matches
DIFFERENT_PERSON_IMAGE_URL = "https://placehold.co/400x400/F77F00/FFFFFF?text=Different+Person"


def get_rekognition_client():
    """
    Initializes and returns the boto3 client for AWS Rekognition,
    using credentials from the .env file.
    """
    try:
        aws_access_key = os.getenv("AZURE_FACE_KEY")
        aws_secret_key = os.getenv("AZURE_FACE_ENDPOINT")
        aws_region = os.getenv("AZURE_FACE_REGION")

        if not all([aws_access_key, aws_secret_key, aws_region]):
            print("Error: AWS credentials or region not found in .env file.")
            return None

        return boto3.client(
            'rekognition',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=aws_region
        )
    except Exception as e:
        print(f"Error creating Rekognition client: {e}")
        return None


def get_image_bytes_from_url(url):
    """Downloads an image from a URL and returns its byte content."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image from {url}: {e}")
        return None


def verify_facial_identity(source_image_bytes, target_image_bytes, similarity_threshold=99.0):
    """
    Compares two faces using Amazon Rekognition for identity verification.

    Args:
        source_image_bytes (bytes): The byte content of the source image (e.g., photo ID).
        target_image_bytes (bytes): The byte content of the target image (e.g., live selfie).
        similarity_threshold (float): The minimum confidence score to be considered a match (99.0 is recommended by AWS).

    Returns:
        A dictionary containing the verification result.
    """
    rekognition_client = get_rekognition_client()
    if not rekognition_client:
        return {"error": "Could not initialize Rekognition client."}

    try:
        response = rekognition_client.compare_faces(
            SourceImage={'Bytes': source_image_bytes},
            TargetImage={'Bytes': target_image_bytes},
            SimilarityThreshold=similarity_threshold
        )

        if response['FaceMatches']:
            similarity = response['FaceMatches'][0]['Similarity']
            return {
                "match": True,
                "confidence": f"{similarity:.2f}%",
                "message": "Identity VERIFIED. The faces are a confident match."
            }
        else:
            # This part runs if no faces match with at least 99% confidence.
            # We can check the un-matched faces to see the highest similarity found.
            max_similarity = 0
            if response.get('UnmatchedFaces'):
                # This key may not exist if no faces were found at all
                # We check similarity of the target face if it was detected
                 pass # In a real app you might log this
            
            return {
                "match": False,
                "confidence": f"< {similarity_threshold}%",
                "message": "Identity FAILED. The faces do not match."
            }
            
    except rekognition_client.exceptions.InvalidParameterException:
        return {"error": True, "message": "No face could be detected in one or both of the images."}
    except Exception as e:
        return {"error": True, "message": f"An AWS Rekognition API error occurred: {e}"}


# --- Main Execution Block ---
if __name__ == "__main__":
    print("--- Running Backend Facial Verification Service ---")

    # 1. Get image bytes from URLs (simulates receiving file uploads)
    id_card_bytes = get_image_bytes_from_url(ID_CARD_IMAGE_URL)
    live_selfie_bytes = get_image_bytes_from_url(LIVE_SELFIE_IMAGE_URL)
    different_person_bytes = get_image_bytes_from_url(DIFFERENT_PERSON_IMAGE_URL)

    if id_card_bytes and live_selfie_bytes and different_person_bytes:
        
        # --- Test Case 1: SUCCESSFUL MATCH ---
        print("\n[TEST 1] Verifying a matching identity (ID Card vs. Live Selfie)...")
        result_success = verify_facial_identity(id_card_bytes, live_selfie_bytes)
        print("Result:", result_success)
        
        # --- Test Case 2: FAILED MATCH ---
        print("\n[TEST 2] Verifying a non-matching identity (ID Card vs. Different Person)...")
        result_fail = verify_facial_identity(id_card_bytes, different_person_bytes)
        print("Result:", result_fail)

    else:
        print("\nCould not run tests because one or more demo images failed to download.")
