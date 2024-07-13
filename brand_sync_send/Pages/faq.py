import streamlit as st

def faq():
    # st.set_page_config(
    #     page_title="FAQ",
    #     page_icon="❓",
    #     layout="centered"
    # )

    st.title("Frequently Asked Questions (FAQ)")

    faqs = [
        {
            "question": "What is this application about?",
            "answer": "This application demonstrates the integration of various machine learning models to perform tasks such as generating images from text, captioning images, and interacting with a chatbot."
        },
        {
            "question": "How do I use the Text to Image feature?",
            "answer": "Go to the Text to Image page, enter a descriptive text in the input box, and click the submit button. The model will generate an image based on the description."
        },
        {
            "question": "How do I use the Image to Text feature?",
            "answer": "Go to the Image to Text page, upload an image, and wait for the model to generate a caption for the image."
        },
        {
            "question": "How do I interact with the Chat Bot?",
            "answer": "Go to the Chat Bot page, enter your query in the chat input box, and press enter. The chatbot will respond to your query."
        },
        {
            "question": "What models are used in this application?",
            "answer": "This application uses the Stable Diffusion model for Text to Image, BLIP model for Image to Text, and Mistral AI for the Chat Bot."
        },
        {
            "question": "How can I provide feedback?",
            "answer": "Go to the Feedback page, fill in the feedback form with your name, contact details, and feedback, then submit the form."
        },
        {
            "question": "How can I contact support?",
            "answer": "You can contact support by going to the Contact Us page and filling in the contact form, or by reaching out directly via email, phone, or address provided on the page."
        },
        {
            "question": "What is Stable Diffusion?",
            "answer": "Stable Diffusion is a model that generates images from textual descriptions using diffusion-based techniques."
        },
        {
            "question": "What is BLIP?",
            "answer": "BLIP (Bootstrapped Language-Image Pre-training) is a model that generates captions for images by processing the input image and producing descriptive text."
        },
        {
            "question": "What is Mistral AI?",
            "answer": "Mistral AI is a large language model that powers the chatbot in this application, providing informative and engaging responses to user queries."
        },
        {
            "question": "Can I use this application on my mobile device?",
            "answer": "Yes, this application is responsive and can be accessed on both desktop and mobile devices."
        },
        {
            "question": "Is my data secure?",
            "answer": "Yes, we take data security seriously and ensure that your data is protected and used responsibly."
        },
        {
            "question": "How often is the application updated?",
            "answer": "The application is regularly updated to improve performance, add new features, and ensure security."
        },
        {
            "question": "Do I need to create an account to use this application?",
            "answer": "No, you do not need to create an account to use the features of this application."
        },
        {
            "question": "Who can I contact for more information?",
            "answer": "For more information, you can contact our support team via the Contact Us page or email us at support@mlapp.com."
        }
    ]

    for faq in faqs:
        with st.expander(faq["question"]):
            st.write(faq["answer"])

if __name__ == "__main__":
    faq()
