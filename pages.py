import streamlit as st

from chatbot import ask_question
from utils import build_chat_history, format_sources
from services.upload_service import index_uploaded_files


def chat_page():
    st.title("💬 Chat with Documents")

    with st.expander("📂 Upload & Index PDFs", expanded=False):
        uploaded_files = st.file_uploader(
            "Upload PDF documents",
            type=["pdf"],
            accept_multiple_files=True,
        )

        if uploaded_files:
            if st.button("⚡ Index Documents"):
                with st.spinner("Indexing uploaded PDFs..."):
                    chunks_count = index_uploaded_files(uploaded_files)

                st.success(f"Indexed successfully! Created {chunks_count} chunks.")
                st.session_state.messages = []
                st.cache_resource.clear()
                st.rerun()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    question = st.chat_input("Ask something about your document...")

    if question:
        st.session_state.messages.append({"role": "user", "content": question})

        with st.chat_message("user"):
            st.markdown(question)

        history = build_chat_history(st.session_state.messages)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer, docs = ask_question(question, history)

            st.markdown(answer)

            sources = format_sources(docs)

            with st.expander("📄 Sources Used"):
                for i, source in enumerate(sources, start=1):
                    st.markdown(
                        f"""
**Source {i}**

📄 Document: `{source["document"]}`  
📖 Page: `{source["page"]}`

---
"""
                    )

        st.session_state.messages.append({"role": "assistant", "content": answer})


def summarize_page():
    st.title("📝 Summarize Document")
    st.info("Summarizer coming soon.")


def keypoints_page():
    st.title("📄 Key Points")
    st.info("Key point extractor coming soon.")


def quiz_page():
    st.title("❓ Quiz Generator")
    st.info("Quiz generator coming soon.")


def compare_page():
    st.title("📊 Compare Documents")
    st.info("Compare documents coming soon.")


def settings_page():
    st.title("⚙️ Settings")
    st.info("Settings coming soon.")