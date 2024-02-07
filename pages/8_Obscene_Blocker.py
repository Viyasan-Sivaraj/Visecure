import streamlit as st
import soundfile as sf
import numpy as np
import requests

# Text filter
explicit_words = ["explicit", "inappropriate", "vulgar", "offensive"]

# Voice filter
def detect_high_pitch(audio_path):
    data, _ = sf.read(audio_path)
    pitch = np.mean(np.abs(np.diff(np.unwrap(np.angle(np.fft.fft(data))))))
    return pitch > 0.1  # Adjust threshold as needed

# Image filter (using Sightengine API)
SIGHTENGINE_API_KEY = "1208251268"

def is_obscene_image(image_url):
    params = {
        "url": image_url,
        "models": "nudity",
        "api_user": "user_id",
        "api_secret": "user_secret"
    }
    response = requests.get("https://api.sightengine.com/1.0/check.json", params=params)
    result = response.json()
    return result.get("nudity", {}).get("raw") > 0.5

def main():
    st.title(":blue[Obscene] Content Blocker")

    app_mode = st.sidebar.selectbox("Select a page:", ["Obscene Content Blocking", "Real-Time Scanning"])

    if app_mode == "Obscene Content Blocking":
        text_input = st.text_area("Enter text:")
        audio_file = st.file_uploader("Upload audio file:", type=["wav", "mp3"])
        image_url = st.text_input("Enter image URL:")

        if st.button("Submit"):
            explicit_detected = False

            for word in explicit_words:
                if word in text_input.lower():
                    st.warning("Explicit content detected in text.")
                    explicit_detected = True
                    break

            if not explicit_detected and audio_file is not None:
                with open("temp_audio.wav", "wb") as f:
                    f.write(audio_file.read())
                if detect_high_pitch("temp_audio.wav"):
                    st.warning("High-pitched audio detected. It could be explicit content.")
                    explicit_detected = True

            if not explicit_detected and image_url:
                if is_obscene_image(image_url):
                    st.warning("Potentially obscene content detected in the image.")
                    explicit_detected = True
            
            if not explicit_detected:
                st.success("No explicit content detected.")

    elif app_mode == "Real-Time Scanning":
        st.title("Real-Time Scanning for Obscene Content")
        st.write("This feature is under development.")

if __name__ == "__main__":
    main()

c31,c11,c12 = st.columns([3,1,5])
c11.image("logo.png", width=200)
