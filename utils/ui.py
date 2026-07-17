import streamlit as st

def show_header(title):
    col1, col2 = st.columns([1, 4])

    with col1:
        st.image("assets/netflix_logo.png", width=80)

    with col2:
        st.title(title)

    st.markdown("---")