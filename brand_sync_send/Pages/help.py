
import streamlit as st

def help():
    st.title("Help")

    with st.container():
        st.header("Text to Image")
        st.markdown("""
        **Model**: Stable Diffusion

        **Description**: The Stable Diffusion model generates images from textual descriptions. It interprets the input text provided by the user and creates a corresponding image based on the description.

        **Steps to Use**:
        1. Go to the **Text to Image** page from the navigation sidebar.
        2. Enter a descriptive text in the input box. For example, "A sunset over a mountain range."
        3. Click the **Submit** button or press Enter.
        4. Wait for the model to generate the image. The generated image will be displayed below the input box.

        This model leverages a pre-trained diffusion model to produce high-quality images that match the user's description.
        """)

    with st.container():
        st.header("Image to Text")
        st.markdown("""
        **Model**: BLIP (Bootstrapped Language-Image Pre-training)

        **Description**: The BLIP model generates captions for images. It processes an input image and produces a descriptive text that summarizes the content of the image.

        **Steps to Use**:
        1. Go to the **Image to Text** page from the navigation sidebar.
        2. Upload an image file by clicking the **Choose an image...** button. Supported formats are JPG, JPEG, and PNG.
        3. Once the image is uploaded, wait for the model to generate the caption.
        4. The generated caption will be displayed below the uploaded image.

        This model is particularly useful for applications in accessibility, image search, and content generation, providing a textual description of the visual content.
        """)

    with st.container():
        st.header("Chat Bot")
        st.markdown("""
        **Model**: Mistral AI

        **Description**: Our chatbot is powered by Mistral AI, which uses a large language model to understand and respond to user queries. This model is designed to handle a wide range of conversational topics, providing informative and engaging interactions.

        **Steps to Use**:
        1. Go to the **Chat Bot** page from the navigation sidebar.
        2. Enter your query or message in the chat input box. For example, "Tell me a joke."
        3. Press Enter or click the **Submit** button.
        4. Wait for the chatbot to generate a response. The response will be displayed in the chat window.

        This model leverages advanced natural language processing techniques to provide meaningful and contextually appropriate responses to user inputs.
        """)

    with st.container():
        st.header("Text to Video")
        st.markdown("""
        **Model**: VideoGen

        **Description**: Embark on a visual journey with Text to Video feature powered by VideoGen. This model breathes life into your textual narratives, transforming them into dynamic and engaging video content. Seamlessly integrating text and visuals, VideoGen creates captivating videos that captivate and inspire.

        **How to Use**:
        1. Navigate to the **Text to Video** page from the sidebar.
        2. Enter your narrative text in the provided textbox.
        3. Click the **Generate Video** button to commence the video creation process.
        4. Sit back and enjoy as VideoGen crafts a compelling video based on your story.

        Elevate your storytelling prowess and unleash your creativity with VideoGen, where words transcend into moving images.
        """)

    with st.container():
        st.header("Audio to Text")
        st.markdown("""
        **Model**: SonicTranscribe

        **Description**: Experience the power of transcription with our Audio to Text feature powered by SonicTranscribe. This model accurately converts audio recordings into precise textual representations, enabling seamless access to spoken content. SonicTranscribe's advanced algorithms ensure reliable transcriptions, facilitating various applications such as transcription services and accessibility tools.

        **How to Use**:
        1. Visit the **Audio to Text** page from the sidebar.
        2. Upload your audio file using the designated button (supported formats: MP3, WAV).
        3. Await the model's processing and transcription.
        4. Explore the textual representation of your audio content displayed below the upload box.

        Empower your audio content with SonicTranscribe, bridging the gap between spoken and written word.
        """)

    st.markdown("""
    If you encounter any issues or have further questions, feel free to reach out through the **Contact Us** page. Our support team is here to help you.
    """)

if __name__ == "__main__":
    help()
