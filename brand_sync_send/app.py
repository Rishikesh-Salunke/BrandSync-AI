import streamlit as st
from streamlit_navigation_bar import st_navbar
import Pages as pg


def app():
    st.set_page_config(
        page_title="Home",
        page_icon="🏠",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    pages = ["Home","About Us","Help","Contact US", "Feedback","FAQ"]
    styles = {
        "nav": {
            "background-color": "rgb(55, 56, 70, 1)",
            "justify-content": "flex-start",  
        },
        "div": {
            "max-width": "32rem",
        },
        "span": {
            "border-radius": "0.5rem",
            "color": "rgb(255, 255, 255, 1)",
            "margin": "0 0.125rem",
            "padding": "0.4375rem 0.625rem",
        },
        "active": {
            "background-color": "rgba(255, 255, 255, 0.25)"
        },
        "hover": {
            "background-color": "rgba(255, 255, 255, 0.35)"
        }
    }

    
    page = st_navbar(pages,styles=styles)

    functions = {
        "Home": pg.home,
        "About Us": pg.about,
        "Help": pg.help,
        "Contact US":pg.contact,
        "Feedback": pg.feedback,
        "FAQ": pg.faq
        
    }
    go_to = functions.get(page)
    if go_to:
        go_to()
    # with st.sidebar:
    #     st.write("Sidebar")

if __name__ == "__main__":
    app()