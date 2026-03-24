# 🛡️ DeepShield: Real-Time Biometric Identity Guard

**Built for the LevelNext Hackathon 2026**

## 🛑 The Problem
As Generative AI voice cloning (like ElevenLabs) and live deepfakes become indistinguishable from reality, remote corporate meetings have become the new frontier for social engineering and financial fraud. Traditional security stops at the login screen; it doesn't verify *who* is actually speaking.

## 💡 The Solution
**DeepShield** is a zero-trust biometric verification layer. It acts as a forensic man-in-the-middle, analyzing incoming audio/video streams to detect synthetic artifacts, spectral flatness, and lip-sync latency that are invisible to the human ear/eye. 

## ⚙️ The Architecture & Tech Stack
* **Frontend/UI:** `Streamlit` with custom CSS & `Plotly` for 3D real-time spectral rendering.
* **Signal Processing:** `Librosa` for extracting raw Mel-frequency cepstral coefficients (MFCCs) and spectral flatness.
* **AI Neural Engine:** `Google Cloud Vertex AI` (Gemini 1.5 Flash) leveraging multimodal ingestion to analyze audio files for unnatural emotional cadence and breathing patterns.

## 🚀 How to Run Locally
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Place your GCP `credentials.json` in the root directory.
4. Run the forensic suite: `streamlit run app.py`