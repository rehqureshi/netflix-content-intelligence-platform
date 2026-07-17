import streamlit as st
from utils.ui import show_header

show_header("Netflix Content Intelligence Platform")

st.set_page_config(
    page_title="Netflix Content Intelligence Platform",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)



st.markdown("""
Welcome to the **Netflix Content Intelligence Platform**.

This application provides business insights into Netflix's global content catalog.

👈 Use the sidebar to navigate between dashboards.
""")