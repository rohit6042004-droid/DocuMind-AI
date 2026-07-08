import streamlit as st
from pages import chat_page

st.set_page_config(
    page_title="DocuMind AI",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

chat_page()
