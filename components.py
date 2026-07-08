import os
import streamlit as st

try:
    from config import UPLOAD_FOLDER
except Exception:
    UPLOAD_FOLDER = "uploads"


def file_size(filename: str) -> str:
    try:
        path = os.path.join(UPLOAD_FOLDER, filename)
        size = os.path.getsize(path)
        if size < 1024 * 1024:
            return f"{size / 1024:.1f} KB"
        return f"{size / (1024 * 1024):.1f} MB"
    except Exception:
        return "Ready"


def render_sidebar(doc_count: int) -> None:
    with st.sidebar:
        st.markdown(f"""
        <div class="sidebar-brand">
            <div class="sidebar-brand-title">📄 DocuMind <span>AI</span></div>
            <div class="sidebar-brand-sub">Your AI document assistant</div>
        </div>

        <div class="sidebar-new-chat">💬 New Chat <span style="float:right;">＋</span></div>
        <div class="sidebar-item">📁 Documents</div>
        <div class="sidebar-item">🌐 Web Search</div>
        <div class="sidebar-item">🕘 Chat History</div>
        <div class="sidebar-item">⚙️ Settings</div>

        <div class="sidebar-box">
            <div style="font-weight:850;margin-bottom:8px;">Storage</div>
            <div class="sidebar-big">{doc_count}</div>
            <div style="color:#94A3B8;font-size:13px;">indexed document(s)</div>
        </div>

        <div class="sidebar-box">
            <div style="font-weight:850;margin-bottom:8px;">💡 Tip</div>
            <div style="color:#CBD5E1;font-size:13px;line-height:1.55;">
                Upload PDFs for document answers, or ask without PDFs for normal AI chat.
            </div>
        </div>
        """, unsafe_allow_html=True)


def render_doc_card(doc: str) -> None:
    st.markdown(f"""
    <div class="doc-card">
        <div class="doc-row">
            <div class="pdf-icon">PDF</div>
            <div>
                <div class="doc-name">{doc}</div>
                <div class="doc-meta">{file_size(doc)}</div>
                <div class="doc-status">✓ Indexed</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_source_card(i: int, source: dict) -> None:
    st.markdown(
        f"""
        <div class="source-card">
            <div class="source-title">Source {i}: 📄 {source["document"]}</div>
            <div class="source-page">Page {source["page"]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
