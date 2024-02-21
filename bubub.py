import streamlit as st
from PIL import Image
import base64

# Set page title and favicon
st.set_page_config(page_title="Encouragement for Bubub", page_icon=":heart:")

# Load background image
bg_image = Image.open("your_girlfriend_picture.jpg")
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/jpeg;base64,{base64.b64encode(bg_image.getvalue()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Add background music
audio_file = open("your_custom_music.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3", start_time=0)

# Add text message
st.markdown("<h1 style='text-align: center; color: white;'>Semangat bubub ku besok sidangnya!</h1>", unsafe_allow_html=True)

# Display swans creating love sign
st.write("Insert code to display swans creating love sign here")
