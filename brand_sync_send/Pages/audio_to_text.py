
import streamlit as st
from pydub import AudioSegment, silence
import speech_recognition as sr
import tempfile
import os
from streamlit_extras.switch_page_button import switch_page

recog = sr.Recognizer()
final_result = ""

# Create a container for the header and the button
header_container = st.container()
with header_container:
    col1, col2 = st.columns([9, 1])
    with col1:
        st.markdown("<h1 style='text-align: center;'>Audio To Text Converter</h1>", unsafe_allow_html=True)
    with col2:
        if st.button("Home"):
            switch_page("app")

st.markdown("**_**", unsafe_allow_html=True)

audio = st.file_uploader("Upload Your Audio File", type=["mp4", "wav"])

if audio:
    st.audio(audio)

    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(audio.read())
        temp_file_path = tmp_file.name
    
    # Load the audio file using pydub
    audio_segment = AudioSegment.from_file(temp_file_path)
    chunks = silence.split_on_silence(audio_segment, min_silence_len=500, silence_thresh=audio_segment.dBFS-20, keep_silence=100)
    
    for index, chunk in enumerate(chunks):
        chunk_file_path = f"{index}.wav"
        chunk.export(chunk_file_path, format="wav")
        with sr.AudioFile(chunk_file_path) as source:
            recorded = recog.record(source)
            try:
                text = recog.recognize_google(recorded)
                final_result += text
                print(text)
            except:
                print("None")
                final_result += " Unintelligible"
        # Optionally remove the chunk file after processing
        os.remove(chunk_file_path)
    
    # Optionally remove the temporary uploaded file
    os.remove(temp_file_path)
    
    with st.form("Result:"):
        result = st.text_area("", value=final_result)
        btn = st.form_submit_button("Download")
        
        if btn:
            with open("transcription.txt", "w") as file:
                file.write(final_result)
