import streamlit as st

def contact():
    # st.set_page_config(
    #     page_title="Contact Us",
    #     page_icon="📞",
    #     layout="centered"
    # )

    st.title("Contact Us")
    st.markdown("""
    We'd love to hear from you! If you have any questions, feedback, or suggestions, please reach out to us using the form below or through our contact details provided at the end of the page.
    """)

    with st.form(key='contact_form'):
        name = st.text_input("Name")
        contact_number = st.text_input("Contact Number")
        email = st.text_input("Email")
        problem = st.text_area("Describe your problem or inquiry")
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.success("Thank you for contacting us! We will get back to you soon.")
        st.markdown(f"**Name:** {name}")
        st.markdown(f"**Contact Number:** {contact_number}")
        st.markdown(f"**Email:** {email}")
        st.markdown(f"**Problem/Inquiry:** {problem}")

    st.markdown("""
    ### Our Contact Details
    - **Email**: support@mlapp.com
    - **Phone**: +1 234 567 890
    - **Address**: 123 ML Street, AI City, Data Country
    """)

if __name__ == "__main__":
    contact()
