import streamlit as st
from PIL import Image
import base64
import requests

def load_image(image_url):
    response = requests.get(image_url)
    img = Image.open(io.BytesIO(response.content))
    return img

# Set page title and favicon
st.set_page_config(page_title="Semangat BUBUB!!", page_icon=":heart:")

# Load background image
bg_image = load_image("https://drive.google.com/file/d/1VK6uShpu7kbYOcCQBAsvp79MDeCfUN8j/view?usp=drive_link")

# Convert image to bytes
image_bytes = io.BytesIO()
bg_image.save(image_bytes, format="JPG")
image_bytes = image_bytes.getvalue()

# Encode image bytes to base64
base64_image = base64.b64encode(image_bytes).decode()

# Display background image
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url('data:image/jpeg;base64,{base64_image}') center;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Add background music
audio_file = open("https://github.com/underthebed1102/bubub/blob/ac4b6c06604ba530c10d039c821654ec08b4ad23/ost%20mancing%20mania.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3", start_time=0)

# Add text message
st.markdown("<h1 style='text-align: center; color: white;'>Semangat bubub ku besok sidangnya!</h1>", unsafe_allow_html=
