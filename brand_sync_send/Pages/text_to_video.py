import streamlit as st
from diffusers import AnimateDiffPipeline, MotionAdapter, EulerDiscreteScheduler
from diffusers.utils import export_to_gif
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file
import torch
def app():
    # Setup
    device = "cuda"
    dtype = torch.float16
    step = 4  # Options: [1, 2, 4, 8]
    repo = "ByteDance/AnimateDiff-Lightning"
    ckpt = f"animatediff_lightning_{step}step_diffusers.safetensors"
    base = "emilianJR/epiCRealism"  # Choose your favorite base model.

    # Initialize pipeline
    adapter = MotionAdapter().to(device, dtype)
    adapter.load_state_dict(load_file(hf_hub_download(repo, ckpt), device=device))
    pipe = AnimateDiffPipeline.from_pretrained(base, motion_adapter=adapter, torch_dtype=dtype).to(device)
    pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing", beta_schedule="linear")

    # Streamlit app
    st.title('Text to Video')

    if "messages" not in st.session_state.keys():
        st.session_state.messages = [
            {'role': 'assistant', 'content': "Hello there, ask me to generate a video! I'll do it for you."}
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
                output = pipe(prompt=user_prompt, guidance_scale=1.0, num_inference_steps=step)
                gif_path = "animation.gif"
                export_to_gif(output.frames[0], gif_path)
                st.image(gif_path)
        new_ai_response = {'role': 'assistant', 'content': "Here is your generated video."}
        st.session_state.messages.append(new_ai_response)

if __name__ == "__main__":
    app()