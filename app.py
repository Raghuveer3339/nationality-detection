import streamlit as st
import cv2
import numpy as np
from deepface import DeepFace
from utils.color_utils import detect_dress_color

# Page config
st.set_page_config(page_title="Nationality Detection", layout="centered")

# Custom CSS (🔥 makes UI beautiful)
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
}
.sub-title {
    text-align: center;
    color: gray;
    margin-bottom: 20px;
}
.result-card {
    background-color: #111;
    padding: 20px;
    border-radius: 12px;
    margin-top: 20px;
}
.result-text {
    font-size: 18px;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">🌍 Nationality Detection System</div>', unsafe_allow_html=True)


# Upload
uploaded_file = st.file_uploader("📤 Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    # Show image nicely
    st.image(img, channels="BGR", caption="📸 Input Image", width="stretch")

    st.markdown("---")

    if st.button("🚀 Analyze Image"):

        with st.spinner("Analyzing... please wait ⏳"):

            result = DeepFace.analyze(
                img,
                actions=['age', 'emotion', 'race'],
                enforce_detection=False
            )

            age = result[0]['age']
            emotion = result[0]['dominant_emotion']
            race = result[0]['dominant_race']

            # Nationality mapping
            if race == "indian":
                nationality = "Indian"
            elif race == "white":
                nationality = "USA"
            elif race == "black":
                nationality = "African"
            else:
                nationality = "Other"

            # Dress color
            h, w, _ = img.shape
            dress_region = img[int(h * 0.5):h, 0:w]
            dress_color = detect_dress_color(dress_region)

        # -------- RESULTS UI --------
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.subheader("📊 Results")

        st.markdown(f'<div class="result-text">🌎 <b>Nationality:</b> {nationality}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-text">😊 <b>Emotion:</b> {emotion}</div>', unsafe_allow_html=True)

        if nationality == "Indian":
            st.markdown(f'<div class="result-text">🎂 <b>Age:</b> {age}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="result-text">🎨 <b>Dress Color:</b> {dress_color}</div>', unsafe_allow_html=True)

        elif nationality == "USA":
            st.markdown(f'<div class="result-text">🎂 <b>Age:</b> {age}</div>', unsafe_allow_html=True)

        elif nationality == "African":
            st.markdown(f'<div class="result-text">🎨 <b>Dress Color:</b> {dress_color}</div>', unsafe_allow_html=True)

        else:
            st.markdown('<div class="result-text">⚠ Basic prediction shown</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)