
import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint
from secret_keys import huggingface_key
from streamlit_extras.switch_page_button import switch_page

# models
chat_model = "mistralai/Mistral-7B-Instruct-v0.3"

# LLMs
chat_llm = HuggingFaceEndpoint(repo_id=chat_model, temperature=0.7, huggingfacehub_api_token=huggingface_key)

# Create a container for the header and the button
header_container = st.container()
with header_container:
    col1, col2 = st.columns([9, 1])
    with col1:
        st.title('Chat bot')
    with col2:
        if st.button("Home"):
            switch_page("app")

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {'role': 'assistant', 'content': 'Hello there, ask anything you want.'}
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
            ai_response = chat_llm.invoke(user_prompt)
            st.write(ai_response)
    new_ai_response = {'role': 'assistant', 'content': ai_response}
    st.session_state.messages.append(new_ai_response)
