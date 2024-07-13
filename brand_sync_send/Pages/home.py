
import streamlit as st
from streamlit_card import card
from streamlit_extras.switch_page_button import switch_page


def home():

    # Project description
    st.header("BrandSync AI")
    st.title("Welcome to the ML-Powered Web Application")
    st.markdown("""
    Our innovative platform harnesses the power of cutting-edge machine learning models to offer a diverse range of advanced functionalities. Explore the seamless integration of AI technology across multiple domains:

 

    Explore the future of AI-powered solutions with our ML-Powered Web Application.""")

 # Create columns for containers
    col1, col2, col3 ,col4 , col5= st.columns(5)

    with col1:
        with st.container():
            st.markdown('<div class="container">', unsafe_allow_html=True)
            st.image("C:/Clg/project/brand_sync/images/text_to_imahe.jpeg")
            st.header("Text to Image")
            st.write("Generate high-quality images from text using the Stable Diffusion model.")
            if st.button("Text to Image"):
                switch_page("text_to_image")
            st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        with st.container():
            st.markdown('<div class="container">', unsafe_allow_html=True)
            st.image("C:/Clg/project/brand_sync/images/image_to_text.jpeg")
            st.header("Image to Text")
            st.write("Automatically create descriptive captions for images with the BLIP model.")
            if st.button("Image to Text"):
                switch_page("image_to_text")
            st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        with st.container():
            st.markdown('<div class="container">', unsafe_allow_html=True)
            st.image("C:/Clg/project/brand_sync/images/chat_bot.jpeg")
            st.header("Chat Bot")
            st.write("Engage with an intelligent chatbot for informative and interactive conversations.")
            if st.button("Chat Bot"):
                switch_page("chat_bot")
            st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        with st.container():
            st.markdown('<div class="container">', unsafe_allow_html=True)
            st.image("C:/Clg/project/brand_sync/images/text_to_video.jpeg")
            st.header("Text to Video")
            st.write("Transform text into dynamic video content using VideoGen.")
            if st.button("Text to Video"):
                switch_page("text_to_video")
            st.markdown('</div>', unsafe_allow_html=True)

    with col5:
        with st.container():
            st.markdown('<div class="container">', unsafe_allow_html=True)
            st.image("C:/Clg/project/brand_sync/images/audio_to_text.jpeg")
            st.header("Audio to Text")
            st.write("Accurately transcribe audio recordings into text with SonicTranscribe.")
            if st.button("Audio to Text"):
                switch_page("audio_to_text")
            st.markdown('</div>', unsafe_allow_html=True)            


if __name__ == "__main__":
    home()
