# 🛡️ DeepShield: Real-Time Biometric "Identity Guard"
**A Zero-Trust Biometric Verification Suite for the Age of Generative AI**

DeepShield is a proactive cybersecurity layer designed to protect the integrity of digital communications. By combining advanced signal processing with multimodal AI, it detects synthetic voice clones and deepfakes in real-time, ensuring that the person you are talking to is exactly who they claim to be.

**Built for the Solution Challenge 2026 - Build with AI**

## 🛑 The Problem
In 2026, Generative AI voice cloning has reached a point where traditional **"identity verification"** is no longer sufficient.
- **Voice Cloning:** Tools like ElevenLabs can clone a human voice with near-perfect accuracy from just seconds of audio.
- **Social Engineering:** Attackers use these clones in live meetings to bypass security and authorize fraudulent transactions.
- **Verification Gap:** Existing security (MFA/Passwords) only verifies the login, not the biological presence of the speaker.

## 💡 The Solution
**DeepShield** provides a *Zero-Trust Biometric Layer*. It does not trust audio simply because it comes from a verified account; instead, it analyzes the physical and emotional markers of the speaker.
- **Live Forensic Auditing:** Analyzes audio/video streams as they happen.
- **Multi-Layered Analysis:** Combines scientific frequency analysis (Spectral Flatness) with high-level AI reasoning.
- **Trust Scoring:** Provides an intuitive 0-100% "Identity Trust Index" for non-technical users. 

## 🚀 Key Features
- **Real-time Biometric Analysis:** Continuous monitoring of audio streams for synthetic artifacts.
- **3D Spectral Topography:** Interactive visualization of vocal tract consistency using Plotly.
- **AI Forensic Diagnostics:** Detailed reasoning from Gemini 1.5 Flash identifying specific "risk markers".
- **Cloud-Native Deployment:** Scalable prototype hosted on Streamlit Cloud.

## ⚙️ The Architecture & Tech Stack
* **Frontend/UI:** `Streamlit` with custom CSS & `Plotly` for 3D real-time spectral rendering.
* **Signal Processing:** `Librosa` for extracting raw Mel-frequency cepstral coefficients (MFCCs) and spectral flatness.
* **AI Neural Engine:** `Google Cloud Vertex AI` (Gemini 1.5 Flash) leveraging multimodal ingestion to analyze audio files for unnatural emotional cadence and breathing patterns.
* **Backend:** Python 3.13.
* **Deployment:** Streamlit Cloud & Google Cloud Platform.

## 💻 Local Setup & Installation
**Prerequisites**

- Python 3.10+
- A Google Cloud Project with Vertex AI API enabled.

**Installation**
**Clone the repository:**

*Bash*-

git clone https://github.com/himanshujain1official/DeepShield.git
cd deepshield

**Install dependencies:**

*Bash*-

pip install -r requirements.txt

**Configure Environment:**

- Create a .env file and add your GCP_PROJECT_ID.
- Place your credentials.json in the root folder.

**Run the Application:**

*Bash*-

streamlit run app.py

## 📽️ Demo Video
Watch the 3-minute technical walkthrough: []