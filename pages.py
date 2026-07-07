import streamlit as st

from chatbot import ask_question
from utils import build_chat_history, format_sources
from services.upload_service import index_uploaded_files
from services.document_service import get_uploaded_documents


def chat_page():
    st.title("💬 Chat with Documents")

    with st.expander("📂 Upload & Index PDFs", expanded=True):
        uploaded_files = st.file_uploader(
            "Upload PDF documents",
            type=["pdf"],
            accept_multiple_files=True,
        )

        if uploaded_files:
            if st.button("⚡ Index Documents"):
                with st.spinner("Indexing uploaded PDFs..."):
                    chunks_count = index_uploaded_files(uploaded_files)

                if chunks_count == 0:
                    st.warning("No new documents indexed. These files may already exist.")
                else:
                    st.success(f"Indexed successfully! Created {chunks_count} chunks.")

                st.session_state.messages = []
                st.cache_resource.clear()
                st.rerun()

    st.subheader("📚 Uploaded Documents")

    documents = get_uploaded_documents()

    if documents:
        for doc in documents:
            st.markdown(f"✅ `{doc}`")

        selected_document = st.selectbox(
            "🔍 Search In",
            ["All Documents"] + documents,
        )
    else:
        st.info("No documents uploaded yet.")
        selected_document = "All Documents"

    st.divider()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    question = st.chat_input("Ask something about your documents...")

    if question:
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.markdown(question)

        history = build_chat_history(st.session_state.messages)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer, docs = ask_question(
                    question,
                    history,
                    selected_document
                )

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

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )


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