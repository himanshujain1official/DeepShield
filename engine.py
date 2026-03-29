import os
import streamlit as st
import librosa
import numpy as np
import vertexai
from vertexai.generative_models import GenerativeModel, Part
from google.oauth2 import service_account
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
# 1. TRY LOCAL FIRST, THEN CLOUD
if os.path.exists("credentials.json"):
    # LOCAL MODE
    load_dotenv()
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
    project_id = os.getenv("GCP_PROJECT_ID")
    vertexai.init(project=project_id, location="us-central1")
else:
    # CLOUD MODE (Streamlit Secrets)
    project_id = st.secrets["GCP_PROJECT_ID"]
    credentials_dict = dict(st.secrets["gcp_service_account"])
    creds = service_account.Credentials.from_service_account_info(credentials_dict)
    vertexai.init(project=project_id, location="us-central1", credentials=creds)

model = GenerativeModel("gemini-2.5-flash")

def analyze_voice_authenticity(audio_path):
    """
    Analyzes audio for synthetic artifacts using Librosa (Science) and Gemini (AI).
    """
    try:
        # --- THE SCIENCE (Librosa Spectral Analysis) ---
        # Load the audio. AI voices often have unnatural 'flatness' in high frequencies.
        y, sr = librosa.load(audio_path, sr=None) 
        flatness = np.mean(librosa.feature.spectral_flatness(y=y))
        
        # Format it to look like a complex scientific metric for the UI
        science_metric = f"{flatness:.6f} Hz/Var"

        # --- THE AI (Vertex AI Multimodal) ---
        audio_part = Part.from_data(data=open(audio_path, "rb").read(), mime_type="audio/wav")
        
        prompt = """
        You are an elite Cybersecurity Forensic Audio Analyst. 
        Analyze this voice clip. Look for:
        1. Synthetic artifacts (robotic jitter, unnatural breathing).
        2. Emotional consistency.
        
        Respond with EXACTLY ONE short sentence. 
        If it sounds real, say: "BIOMETRICS VERIFIED: Natural human vocal tract variations detected."
        If it sounds like AI/ElevenLabs, say: "HIGH RISK: Synthetic pitch modulation and unnatural breathing artifacts detected."
        """
        
        response = model.generate_content([prompt, audio_part])
        return response.text.strip(), science_metric

    except Exception as e:
        return f"SYSTEM ERROR: Could not process audio. {str(e)}", "ERROR"

def analyze_video_sync(video_path):
    """
    Analyzes video for lip-sync latency and deepfake artifacts.
    """
    try:
        # Read the file data into memory
        with open(video_path, "rb") as f:
            video_data = f.read()
            
        video_part = Part.from_data(data=video_data, mime_type="video/mp4")
        
        prompt = """
        Act as a Deepfake Forensic Specialist. Analyze this video for 'High-End Avatar' signatures:
        1. Eye-Gaze: Does the person blink naturally? Is there a 'dead-eye' stare during speech?
        2. Micro-expressions: Do the cheeks and forehead move naturally with the mouth?
        3. Texture: Is the skin too smooth or 'plastic' under lighting changes?
        
        If you see ANY of these subtle AI signs, start your response with 'HIGH RISK:'. 
        Only say 'BIOMETRICS VERIFIED:' if it is 100 percent indistinguishable from a biological human.
        """
        
        response = model.generate_content([prompt, video_part])
        return response.text.strip() # Returns ONLY a string

    except Exception as e:
        # This prints the real error to your VS Code terminal for debugging
        print(f"DEBUG VIDEO ERROR: {e}")
        return f"HIGH RISK: System could not verify biometric integrity. Error: {str(e)[:50]}"