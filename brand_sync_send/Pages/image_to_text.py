
import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import tempfile
from streamlit_extras.switch_page_button import switch_page

def get_image_caption(image_path):
    """
    Generates a short caption for the provided image.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: A string representing the caption for the image.
    """
    image = Image.open(image_path).convert('RGB')

    model_name = "Salesforce/blip-image-captioning-large"
    device = "cpu"  # or "cuda" if using a GPU

    processor = BlipProcessor.from_pretrained(model_name)
    model = BlipForConditionalGeneration.from_pretrained(model_name).to(device)

    inputs = processor(image, return_tensors='pt').to(device)
    output = model.generate(**inputs, max_new_tokens=20)

    caption = processor.decode(output[0], skip_special_tokens=True)

    return caption

# Streamlit app
st.set_page_config(
    page_title='Image to Text',
    page_icon="🖼️",
    layout='wide'
)

# Create a container for the header and the button
header_container = st.container()
with header_container:
    col1, col2 = st.columns([9, 1])
    with col1:
        st.title('🖼️ Image to Text')
    with col2:
        if st.button("Home"):
            switch_page("app")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(uploaded_file.getbuffer())
        tmp_file_path = tmp_file.name

    # Display the uploaded image in a smaller box
    image_container = st.container()
    with image_container:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(tmp_file_path, caption='Uploaded Image', use_column_width=True)
        with col2:
            st.spinner("Generating ...")
            caption = get_image_caption(tmp_file_path)
            st.write("Caption:", caption)
