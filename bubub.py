import streamlit as st
from PIL import Image
import base64

# Set page title and favicon
st.set_page_config(page_title="Semangat BUBUB!!", page_icon=":heart:")

# Load background image
bg_image = Image.open("https://github.com/underthebed1102/bubub/blob/ba37d89cdd5d839f6f19f7d12a3e07018523342b/IMG-20230505-WA0007.jpg")

# Convert image to bytes
image_bytes = bg_image.tobytes()

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
audio_file = open("https://github.com/underthebed1102/bubub/blob/7c2678fbf0d41906f2017e84eae79dead2f941d5/ost%20mancing%20mania.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3", start_time=0)

# Add text message
st.markdown("<h1 style='text-align: center; color: white;'>Semangat bubub ku besok sidangnya!</h1>", unsafe_allow_html=True)

# Display swans creating love sign
#st.write("Insert code to display swans creating love sign here")
