import streamlit as st
from gtts import gTTS
from io import BytesIO

st.title("MLOps Text-To-Speech App")

# Main layout
text = st.text_area("Ingresar el texto a reproducir", "Hello, Streamlit!")

# Sidebar for language selection
st.sidebar.title("Audio Options")
language = st.sidebar.selectbox("Elegir lenguaje", ['en', 'es', 'fr', 'de', 'it'], index=0)

# Generate and save the audio as bytes
if st.button("Generar audio"):
    tts = gTTS(text, lang=language)
    st.balloons()

    # Save audio to a BytesIO buffer (in memory)
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)  # Rewind to the beginning of the buffer

    # Display the audio using Streamlit audio widget
    st.audio(audio_buffer, format='audio/mp3')
