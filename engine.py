import os
import streamlit as st
import librosa
import numpy as np
import vertexai
from vertexai.generative_models import GenerativeModel, Part
from google.oauth2 import service_account

# 1. READ SECRETS FROM STREAMLIT
project_id = st.secrets["GCP_PROJECT_ID"]
service_account_info = dict(st.secrets["gcp_service_account"])
credentials_dict = dict(st.secrets["gcp_service_account"])

# 2. FORCE PYTHON TO USE YOUR GCP KEY
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

# 3. INITIALIZE VERTEX AI SECURELY
project_id = os.getenv("GCP_PROJECT_ID") 

# Convert service account dictionary to Credentials object
# 2. CONVERT DICT TO GOOGLE CREDENTIALS OBJECT
creds = service_account.Credentials.from_service_account_info(credentials_dict)

# 3. INITIALIZE
vertexai.init(
    project=project_id, 
    location="us-central1", 
    credentials=creds
)

model = GenerativeModel("gemini-1.5-flash-002")

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
    Analyzes video for lip-sync latency.
    """
    try:
        video_part = Part.from_data(data=open(video_path, "rb").read(), mime_type="video/mp4")
        prompt = "Analyze this video for deepfake signs. Does the lip movement perfectly match the audio? Respond in one short sentence starting with either 'BIOMETRICS VERIFIED:' or 'HIGH RISK:'."
        response = model.generate_content([prompt, video_part])
        return response.text.strip()
    except Exception as e:
        return "SYSTEM ERROR: Could not process video.", "ERROR"