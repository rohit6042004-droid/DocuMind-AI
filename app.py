import streamlit as st
from streamlit_option_menu import option_menu

from pages import (
    chat_page,
    summarize_page,
    keypoints_page,
    quiz_page,
    compare_page,
    settings_page,
)

st.set_page_config(
    page_title="DocuMind AI",
    page_icon="🤖",
    layout="wide"
)

with st.sidebar:
    st.title("🤖 DocuMind AI")
    st.caption("AI Document Workspace")
    st.divider()

    selected = option_menu(
        menu_title=None,
        options=[
            "Chat",
        ],
        icons=[
            "chat-dots",
            "file-earmark-text",
            "list-task",
            "patch-question",
            "files",
            "gear"
        ],
        default_index=0
    )

    st.divider()
    st.caption("Built with LangChain, FAISS, Ollama & Streamlit")

if selected == "Chat":
    chat_page()

elif selected == "Summarize":
    summarize_page()

elif selected == "Key Points":
    keypoints_page()

elif selected == "Quiz":
    quiz_page()

elif selected == "Compare":
    compare_page()

elif selected == "Settings":
    settings_page()