import streamlit as st

from services.web_chat import ask_web_question
from chatbot import ask_question
from utils import build_chat_history, format_sources
from services.upload_service import index_uploaded_files
from services.document_service import get_uploaded_documents

from styles import inject_css
from components import render_sidebar, render_doc_card, render_source_card


def chat_page():
    inject_css()

    documents = get_uploaded_documents()
    render_sidebar(len(documents))

    st.markdown('<div class="app-shell">', unsafe_allow_html=True)

    left, right = st.columns([0.92, 2.08], gap="large")

    with left:
        st.markdown('<div class="left-panel">', unsafe_allow_html=True)

        st.markdown("""
        <div class="panel-heading">
            <span>Upload PDFs</span>
            <span>☁️</span>
        </div>

        <div class="upload-visual">
            <div class="upload-visual-icon">☁️</div>
            <div class="upload-visual-title">Drop PDFs here</div>
            <div class="upload-visual-sub">
                or browse files below<br>
                Supports multiple PDFs
            </div>
        </div>
        """, unsafe_allow_html=True)

        uploaded_files = st.file_uploader(
            "Browse files",
            type=["pdf"],
            accept_multiple_files=True,
            label_visibility="collapsed"
        )

        if uploaded_files:
            st.markdown(
                f'<div class="status-ready">Ready to index {len(uploaded_files)} document(s).</div>',
                unsafe_allow_html=True
            )

            if st.button("⚡ Index Documents", use_container_width=True):
                with st.spinner("Creating embeddings..."):
                    chunks = index_uploaded_files(uploaded_files)

                if chunks:
                    st.success(f"Indexed successfully ({chunks} chunks).")
                    st.session_state.messages = []
                    st.cache_resource.clear()
                    st.rerun()
                else:
                    st.warning("These documents are already indexed.")

        st.markdown(
            f"""
            <div class="docs-title">
                <span>Indexed Documents</span>
                <span class="docs-count">{len(documents)}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        if documents:
            for doc in documents:
                render_doc_card(doc)

            selected_document = st.selectbox(
                "Search in",
                ["All Documents"] + documents,
                index=0
            )
        else:
            selected_document = "All Documents"
            st.markdown(
                '<div class="empty-doc">No documents indexed yet.</div>',
                unsafe_allow_html=True
            )

        smart_mode = st.toggle(
            "🌐 Answer normally when no PDF is indexed",
            value=True
        )

        st.markdown("""
        <div class="tip-card">
            ✨ Ask naturally: summarize, compare, extract key points, or ask a normal question.
        </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="chat-panel">', unsafe_allow_html=True)

        mode = "Document Mode" if documents else "General AI Mode"
        if documents and smart_mode:
            mode = "Smart Document Mode"

        st.markdown(f"""
        <div class="chat-hero">
            <div class="chat-title">👋 Hello! How can I help you today?</div>
            <div class="chat-sub">
                Ask anything. Use indexed PDFs when available, or chat normally without uploads.
            </div>
            <div class="mode-pill">{mode}</div>
        </div>
        """, unsafe_allow_html=True)

        if "messages" not in st.session_state:
            st.session_state.messages = []

        st.session_state.messages = [
            msg for msg in st.session_state.messages
            if msg.get("content") not in [None, "None", ""]
        ]

        clear_col, _ = st.columns([1, 5])
        with clear_col:
            if st.button("🧹 Clear", use_container_width=True):
                st.session_state.messages = []
                st.rerun()

        for message in st.session_state.messages:
            role = message.get("role", "assistant")
            content = message.get("content", "")

            if content:
                with st.chat_message(role):
                    st.markdown(content)

        question = st.chat_input(
            "Ask anything about your documents...",
            key="main_chat_input"
        )

        if question:
            st.session_state.messages.append(
                {"role": "user", "content": question}
            )

            with st.chat_message("user"):
                st.markdown(question)

            history = build_chat_history(st.session_state.messages)

            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    fresh_documents = get_uploaded_documents()

                    if fresh_documents:
                        answer, docs = ask_question(
                            question,
                            history,
                            selected_document
                        )
                    else:
                        answer = ask_web_question(question, history)
                        docs = []

                st.markdown(answer)

                sources = format_sources(docs)

                if sources:
                    st.markdown("#### 📚 Sources")
                    for i, source in enumerate(sources, start=1):
                        render_source_card(i, source)

            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )

        st.markdown('<div class="footer-note">AI can make mistakes. Verify important information.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def summarize_page():
    chat_page()

def keypoints_page():
    chat_page()

def quiz_page():
    chat_page()

def compare_page():
    chat_page()

def settings_page():
    st.header("⚙ Settings")
    st.info("Settings page coming soon.")
