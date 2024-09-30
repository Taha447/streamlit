import streamlit as st
import torch
import torchaudio

# Load the model
model_path = 'baseline.pth'
model = torch.load(model_path)

# Streamlit app title
st.title("Vocal Remover App")

# File uploader for audio files
uploaded_file = st.file_uploader("Upload an audio file", type=['wav', 'mp3'])

if uploaded_file is not None:
    # Load the audio file
    audio, sr = torchaudio.load(uploaded_file)

    # Process the audio using your model (add your processing logic here)
    with torch.no_grad():
        # Placeholder for model processing
        output = model(audio)

    # Display the original and processed audio
    st.audio(uploaded_file, format='audio/wav')
    # Adjust this based on your output format