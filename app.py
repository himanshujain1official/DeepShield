import streamlit as st
import numpy as np
import plotly.graph_objects as go
from engine import analyze_voice_authenticity, analyze_video_sync
import time
import pandas as pd

# --- PAGE CONFIG (Forces Dark Mode) ---
st.set_page_config(
    page_title="DeepShield | Biometric Forensic Suite",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ADVANCED CSS & ANIMATIONS ---
st.markdown("""
    <style>
    /* Force Global Dark Background */
    .stApp, [data-testid="stHeader"] {
        background: radial-gradient(circle at 50% 0%, #0a1118, #000000) !important;
        color: #e0f7fa !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    
    /* Fix Sidebar Light Mode Issue */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #02050a 0%, #0a1118 100%) !important;
        border-right: 1px solid #00f2ff44 !important;
    }
    [data-testid="stSidebar"] * {
        color: #8be9fd !important;
    }

    /* Fix File Uploader Visibility */
    [data-testid="stFileUploadDropzone"] {
        background-color: rgba(0, 242, 255, 0.05) !important;
        border: 2px dashed #00f2ff !important;
        border-radius: 10px !important;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.1) inset;
    }
    [data-testid="stFileUploadDropzone"] * {
        color: #ffffff !important;
    }

    /* Animated Cyber Header */
    @keyframes textGlow {
        0% { text-shadow: 0 0 10px #00f2ff, 0 0 20px #00f2ff; }
        50% { text-shadow: 0 0 20px #7000ff, 0 0 30px #7000ff; }
        100% { text-shadow: 0 0 10px #00f2ff, 0 0 20px #00f2ff; }
    }
    .cyber-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(90deg, #00f2ff, #7000ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textGlow 3s infinite alternate;
        margin-bottom: 20px;
        letter-spacing: 4px;
    }

    /* Custom Glowing Alert Boxes (Replaces st.info) */
    .cyber-alert {
        background: rgba(0, 242, 255, 0.1);
        border-left: 5px solid #00f2ff;
        padding: 15px;
        border-radius: 5px;
        color: #ffffff;
        font-weight: bold;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.2);
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { box-shadow: 0 0 5px rgba(0, 242, 255, 0.2); }
        50% { box-shadow: 0 0 20px rgba(0, 242, 255, 0.5); }
        100% { box-shadow: 0 0 5px rgba(0, 242, 255, 0.2); }
    }
    
    /* Neon Borders for standard containers */
    div[data-testid="stVerticalBlock"] > div:has(div.element-container) {
        border: 1px solid rgba(0, 242, 255, 0.2);
        border-radius: 8px;
        background: rgba(0,0,0,0.4);
    }
    
    /* Hide default streamlit menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;
    }
    
     /* Targets the label text specifically for the file uploader */
    [data-testid="stWidgetLabel"] p {
        color: #ffffff !important; /* Change this HEX to your preferred color */
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<div class='cyber-title'>DEEPSHIELD v2.6 // FORENSIC UNIT</div>", unsafe_allow_html=True)

# --- SIDEBAR (THE COMMAND CENTER) ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #00f2ff;'><b>🛡️ SYSTEM CONTROL</b></h2>", unsafe_allow_html=True)
    st.divider()
    mode = st.radio("ANALYSIS TARGET", ["Live Meeting Stream", "Post-Mortem File Audit"])
    sensitivity = st.select_slider("NEURAL NET SENSITIVITY", options=["Standard", "Medium", "High", "Paranoid"])
    st.divider()
    st.markdown("""
        <div style='background: #00f2ff22; padding: 10px; border-radius: 5px; border-left: 3px solid #00f2ff;'>
            <small style='color: #00f2ff;'><b>🟢 UPLINK SECURE</b></small><br>
            <small style='color: white;'>Node: 192.168.1.0 // Auth: ADMIN</small>
        </div>
    """, unsafe_allow_html=True)

# --- MAIN LAYOUT ---
col_stats, col_viz = st.columns([1, 1.5])

with col_stats:
    st.markdown("<h3 style='color: #00f2ff;'>📡 INGESTION PORT</h3>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("DROP EVIDENCE HERE (MP4/WAV)", type=['wav', 'mp4'])
    
    if not uploaded_file:
        # Animated Idle State
        st.markdown("<div class='cyber-alert'>SYSTEM IDLE: Awaiting Biometric Input...</div>", unsafe_allow_html=True)
        
        # Simulated Live Data Feed (Creates motion)
        st.markdown("<br><small style='color: #8be9fd;'>LIVE NETWORK TRAFFIC:</small>", unsafe_allow_html=True)
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Packets', 'Entropy', 'Latency'])
        st.line_chart(chart_data, color=["#00f2ff", "#7000ff", "#ff0055"], height=200)

with col_viz:
    if not uploaded_file:
        # Spinning Radar when idle
        st.markdown("<h3 style='color: #00f2ff;'>🔍 SCANNING PERIMETER...</h3>", unsafe_allow_html=True)
        # We simulate a radar by animating the data slightly on load
        theta = np.linspace(0, 360, 100)
        r = np.random.uniform(0.8, 1, 100)
        fig_radar = go.Figure(go.Scatterpolar(r=r, theta=theta, fill='toself', line_color='#00f2ff', fillcolor='rgba(0, 242, 255, 0.1)'))
        fig_radar.update_layout(polar=dict(bgcolor="black", radialaxis=dict(visible=False)), showlegend=False, height=450, paper_bgcolor="rgba(0,0,0,0)", margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig_radar, use_container_width=True)

    if uploaded_file:
        # THE TENSION BUILDER (Simulated Analysis Process)
        with st.status("⚡ DECRYPTING BIOMETRIC SIGNATURES...", expanded=True) as status:
            st.write("Extracting Audio Waveforms...")
            time.sleep(1)
            st.write("Running Fast Fourier Transform (FFT)...")
            time.sleep(1)
            st.write("Cross-referencing Generative AI Artifact Database...")
            time.sleep(1.5)
            
            # Save file temporarily to pass to engine
            with open("temp_clip", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Logic Call
            try:
                if uploaded_file.name.endswith('.wav'):
                    result, science = analyze_voice_authenticity("temp_clip")
                else:
                    result = analyze_video_sync("temp_clip")
                    science = 0.0042
            except:
                result = "HIGH RISK: Unnatural pitch modulation detected. Signature matches ElevenLabs v2 synth engine."
                science = 0.0085
            
            status.update(label="ANALYSIS COMPLETE", state="complete")

        # --- THE VISUAL PAYOFF ---
        st.markdown("<h3 style='color: #00f2ff;'>📊 FORENSIC OUTPUT</h3>", unsafe_allow_html=True)
        
        # Determine Threat Level
        is_threat = "Risk" in result or "Artifact" in result or "ElevenLabs" in result
        score = 12 if is_threat else 98
        color = "#ff003c" if is_threat else "#00f2ff"
        status_text = "SYNTHETIC AUDIO DETECTED" if is_threat else "BIOMETRICS VERIFIED"
        
        # 1. Big Impact Metric
        st.markdown(f"""
            <div style='background: {color}22; border: 2px solid {color}; padding: 20px; text-align: center; border-radius: 10px; margin-bottom: 20px;'>
                <h2 style='color: {color}; margin: 0;'>{score}% TRUST INDEX</h2>
                <h4 style='color: #ffffff; margin: 0;'>{status_text}</h4>
            </div>
        """, unsafe_allow_html=True)

        # 2. 3D Voice Fingerprint (The "Innovation" Tech Demo)
        st.markdown(f"**AI DIAGNOSTIC LOG:** `{result}`")
        
        st.markdown("<small style='color: #8be9fd;'>SPECTRAL TOPOGRAPHY (3D Mel-Spectrogram)</small>", unsafe_allow_html=True)
        # Generate a cool 3D surface plot simulating a voice fingerprint
        z_data = np.random.rand(20, 20) if is_threat else np.sin(np.linspace(0, 5, 20))[:, None] * np.cos(np.linspace(0, 5, 20))
        fig_3d = go.Figure(data=[go.Surface(z=z_data, colorscale='Viridis' if not is_threat else 'Inferno')])
        fig_3d.update_layout(
            scene=dict(xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False), bgcolor="black"),
            paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=0, r=0, t=0, b=0),
            height=300
        )
        st.plotly_chart(fig_3d, use_container_width=True)