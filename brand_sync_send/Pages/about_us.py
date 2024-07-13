# import streamlit as st

# def about():
#     # st.set_page_config(
#     #     page_title="About Us",
#     #     page_icon="ℹ️",
#     #     layout="centered"
#     # )

#     st.title("About Us")
#     st.markdown("""
#     Welcome to our ML-Powered Web Application! Experience the pinnacle of machine learning innovation at your fingertips. Explore a seamless integration of cutting-edge models, from generating images from text to engaging with our intelligent chatbot
#      """)

#     st.header("Our Models")
#     st.markdown("""
#     ### Text to Image
#     - **Model**: Stable Diffusion
#     - **Description**: Employs advanced diffusion techniques to generate high-fidelity images from textual descriptions, making it indispensable for creative and visual content initiatives.
                
#     ### Image to Text
#     - **Model**: BLIP (Bootstrapped Language-Image Pre-training)
#     - **Description**: Analyzes visual content to produce precise and descriptive captions, significantly enhancing accessibility, image search capabilities, and automated content generation.

#     ### Text to Video
#     - **Model**: VideoGen
#     - **Description**: Transforms textual narratives into dynamic and engaging video content, offering a sophisticated tool for content creators and marketers.
                
#     ### Audio to Text
#     - **Model**: SonicTranscribe
#     - **Description**: Utilizes cutting-edge speech recognition algorithms to transcribe audio recordings into precise text, essential for transcription services and accessibility applications.
                
#     ### Chat Bot
#     - **Model**: Mistral AI
#     - **Description**: Delivers intelligent and nuanced conversational interactions through a large language model, enhancing customer service and user engagement.
#     """)

#     st.header("Creators of the Application")

#     st.markdown("### Yash")
#     st.image("C:/Clg/project/brand_sync/yash.jpeg", caption="yash", width=150)
#     st.markdown("""
#     **Name**: Yash 
#     **Details**: Yash is an expert in machine learning and artificial intelligence. With years of experience in developing cutting-edge models, they have contributed significantly to the success of this application. Their expertise in image processing and natural language understanding has been crucial in integrating these advanced models.
#     """)

#     st.markdown("### Rishikesh")
#     st.image("C:/Clg/project/brand_sync/yash.jpeg", caption="Rishikesh", width=150)
#     st.markdown("""
#     **Name**: Rishikesh
#     **Details**: Rishikesh has a strong background in software engineering and application development. Their skills in coding and system integration have been instrumental in bringing this application to life. They are passionate about using technology to solve real-world problems and enhancing user experiences through innovative solutions.
#     """)

  
# if __name__ == "__main__":
#     about()


import streamlit as st

def about():
    st.title("About Us")
    st.markdown("""
    Welcome to our ML-Powered Web Application! Experience the pinnacle of machine learning innovation at your fingertips. Explore a seamless integration of cutting-edge models, from generating images from text to engaging with our intelligent chatbot.
    """)

    st.header("Our Models")

    # Create the first set of containers
    columns = st.columns(3)

    # Column 1: Text to Image
    with columns[0]:
        st.markdown("""
        ### Text to Image
        - **Model**: Stable Diffusion
        - **Description**: Employs advanced diffusion techniques to generate high-fidelity images from textual descriptions, making it indispensable for creative and visual content initiatives.
        """)

    # Column 2: Image to Text
    with columns[1]:
        st.markdown("""
        ### Image to Text
        - **Model**: BLIP (Bootstrapped Language-Image Pre-training)
        - **Description**: Analyzes visual content to produce precise and descriptive captions, significantly enhancing accessibility, image search capabilities, and automated content generation.
        """)

    # Column 3: Text to Video
    with columns[2]:
        st.markdown("""
        ### Text to Video
        - **Model**: VideoGen
        - **Description**: Transforms textual narratives into dynamic and engaging video content, offering a sophisticated tool for content creators and marketers.
        """)

    # Create the second set of containers
    columns = st.columns(3)

    # Column 1: Audio to Text
    with columns[0]:
        st.markdown("""
        ### Audio to Text
        - **Model**: SonicTranscribe
        - **Description**: Utilizes cutting-edge speech recognition algorithms to transcribe audio recordings into precise text, essential for transcription services and accessibility applications.
        """)

    # Column 2: Chat Bot
    with columns[1]:
        st.markdown("""
        ### Chat Bot
        - **Model**: Mistral AI
        - **Description**: Delivers intelligent and nuanced conversational interactions through a large language model, enhancing customer service and user engagement.
        """)

    # Empty column for layout balance
    with columns[2]:
        st.empty()

    st.header("Creators of the Application")
    columns = st.columns(2)

    with columns[0]:
        st.markdown("### Yash Surve")
        st.image("C:/Clg/project/brand_sync/images/image.png", caption="Yash", width=150)
        st.markdown("**Name**: Yash Surve")
        st.markdown("""
        **Details**: Yash is an expert in machine learning and artificial intelligence. With years of experience in developing cutting-edge models, they have contributed significantly to the success of this application. Their expertise in image processing and natural language understanding has been crucial in integrating these advanced models.
        """)

    with columns[1]:
        st.markdown("### Rishikesh Salunke")
        st.image("C:/Clg/project/brand_sync/images/image.png", caption="Rishikesh", width=150)
        st.markdown("**Name**: Rishikesh Salunke")
        st.markdown("""
        **Details**: Rishikesh has a strong background in software engineering and application development. Their skills in coding and system integration have been instrumental in bringing this application to life. They are passionate about using technology to solve real-world problems and enhancing user experiences through innovative solutions.
        """)

if __name__ == "__main__":
    about()
