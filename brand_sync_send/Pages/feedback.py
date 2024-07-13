import streamlit as st

def feedback():
    # st.set_page_config(
    #     page_title="Feedback",
    #     page_icon="📝",
    #     layout="centered"
    # )

    st.title("Feedback")
    st.markdown("""
    Your feedback is important to us. Please let us know what you think about our application and how we can improve it.
    """)

    with st.form(key='feedback_form'):
        name = st.text_input("Name")
        contact_number = st.text_input("Contact Number")
        email = st.text_input("Email")
        rating = st.slider("Rating", 1, 5, 3)
        feedback = st.text_area("Feedback")
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.success("Thank you for your feedback!")
        st.markdown(f"**Name:** {name}")
        st.markdown(f"**Contact Number:** {contact_number}")
        st.markdown(f"**Email:** {email}")
        st.markdown(f"**Rating:** {rating}/5")
        st.markdown(f"**Feedback:** {feedback}")

if __name__ == "__main__":
    feedback()

# import streamlit as st
# import sqlite3

# # Database connection
# conn = sqlite3.connect('feedback.db')
# c = conn.cursor()

# # Create table if it doesn't exist
# c.execute('''
#     CREATE TABLE IF NOT EXISTS feedback (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         contact_number TEXT,
#         email TEXT,
#         rating INTEGER,
#         feedback TEXT
#     )
# ''')
# conn.commit()

# def insert_feedback(name, contact_number, email, rating, feedback):
#     c.execute('''
#         INSERT INTO feedback (name, contact_number, email, rating, feedback)
#         VALUES (?, ?, ?, ?, ?)
#     ''', (name, contact_number, email, rating, feedback))
#     conn.commit()

# def get_feedback():
#     c.execute('SELECT * FROM feedback ORDER BY rating DESC')
#     return c.fetchall()

# def feedback_page():
#     st.title("Feedback")
#     st.markdown("""
#     Your feedback is important to us. Please let us know what you think about our application and how we can improve it.
#     """)

#     with st.form(key='feedback_form'):
#         name = st.text_input("Name")
#         contact_number = st.text_input("Contact Number")
#         email = st.text_input("Email")
#         rating = st.slider("Rating", 1, 5, 3)
#         feedback = st.text_area("Feedback")
#         submit_button = st.form_submit_button(label='Submit')

#     if submit_button:
#         insert_feedback(name, contact_number, email, rating, feedback)
#         st.success("Thank you for your feedback!")
#         st.markdown(f"**Name:** {name}")
#         st.markdown(f"**Contact Number:** {contact_number}")
#         st.markdown(f"**Email:** {email}")
#         st.markdown(f"**Rating:** {rating}/5")
#         st.markdown(f"**Feedback:** {feedback}")

#     st.markdown("## All Feedback")
#     feedback_data = get_feedback()
#     for entry in feedback_data:
#         st.markdown(f"**Name:** {entry[1]}")
#         st.markdown(f"**Contact Number:** {entry[2]}")
#         st.markdown(f"**Email:** {entry[3]}")
#         st.markdown(f"**Rating:** {entry[4]}/5")
#         st.markdown(f"**Feedback:** {entry[5]}")
#         st.markdown("---")
