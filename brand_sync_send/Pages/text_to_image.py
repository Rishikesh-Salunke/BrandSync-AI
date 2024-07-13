
import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from streamlit_extras.switch_page_button import switch_page

# models
model_id = "runwayml/stable-diffusion-v1-5"

# LLMs
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

# Navigation function
def switch_to_home():
    switch_page("app")

# Create a container for the header and the button
header_container = st.container()
with header_container:
    col1, col2 = st.columns([9, 1])
    with col1:
        st.title('Text to Image')
    with col2:
        if st.button("Home"):
            switch_to_home()

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {'role': 'assistant', 'content': "Hello there, ask me to generate an Image! I'll do it for you."}
    ]

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.write(message['content'])

user_prompt = st.chat_input()
if user_prompt is not None:
    st.session_state.messages.append({'role': 'user', 'content': user_prompt})
    with st.chat_message('user'):
        st.write(user_prompt)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            ai_response = pipe(user_prompt).images[0]
            st.image(ai_response)
    new_ai_response = {'role': 'assistant', 'content': ai_response}
    st.session_state.messages.append(new_ai_response)
