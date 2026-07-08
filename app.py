import os
import streamlit as st

from services.web_chat import ask_web_question
from chatbot import ask_question
from utils import build_chat_history, format_sources
from services.upload_service import index_uploaded_files
from services.document_service import get_uploaded_documents

try:
    from config import UPLOAD_FOLDER
except Exception:
    UPLOAD_FOLDER = "uploads"


st.set_page_config(
    page_title="DocuMind AI",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

*{font-family:'Inter',sans-serif;}

[data-testid="stAppViewContainer"]{
    background:
    radial-gradient(circle at 12% 12%, rgba(168,85,247,.25), transparent 28%),
    radial-gradient(circle at 90% 5%, rgba(59,130,246,.22), transparent 30%),
    radial-gradient(circle at 70% 95%, rgba(236,72,153,.14), transparent 28%),
    linear-gradient(135deg,#070A16 0%,#0B1020 50%,#0F172A 100%);
}

[data-testid="stHeader"]{background:transparent;}
.block-container{max-width:1500px;padding-top:1rem;padding-bottom:1rem;}

section[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#111827,#020617);
    border-right:1px solid rgba(255,255,255,.08);
}
section[data-testid="stSidebar"] *{color:white;}

.brand{
    padding:18px 6px 24px;
}
.brand-title{
    font-size:30px;
    font-weight:900;
    letter-spacing:-1px;
}
.brand-title span{
    background:linear-gradient(90deg,#60A5FA,#E879F9);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}
.brand-sub{
    color:#94A3B8;
    font-size:13px;
    margin-top:5px;
}

.nav-main{
    padding:15px 16px;
    border-radius:16px;
    background:linear-gradient(135deg,#A855F7,#2563EB);
    font-weight:800;
    box-shadow:0 18px 45px rgba(37,99,235,.28);
    margin:12px 0 18px;
}
.nav-item{
    padding:13px 15px;
    border-radius:15px;
    background:rgba(255,255,255,.055);
    border:1px solid rgba(255,255,255,.07);
    margin:9px 0;
    font-weight:700;
    color:#CBD5E1;
}
.side-card{
    margin-top:24px;
    padding:17px;
    border-radius:18px;
    background:linear-gradient(135deg,rgba(88,28,135,.45),rgba(37,99,235,.22));
    border:1px solid rgba(168,85,247,.28);
}

.app-shell{
    min-height:auto;
    border-radius:28px;
    padding:18px;
    background:rgba(15,23,42,.52);
    border:1px solid rgba(255,255,255,.09);
    box-shadow:0 28px 90px rgba(0,0,0,.40);
}

.glass{
    border-radius:24px;
    padding:20px;
    background:linear-gradient(180deg,rgba(17,24,39,.92),rgba(15,23,42,.80));
    border:1px solid rgba(255,255,255,.10);
    box-shadow:0 20px 70px rgba(0,0,0,.28);
}

.panel-heading{
    font-size:20px;
    font-weight:900;
    color:#E879F9;
    margin-bottom:14px;
    display:flex;
    justify-content:space-between;
}

.upload-box{
    border:1.5px dashed rgba(168,85,247,.58);
    background:radial-gradient(circle at 50% 18%,rgba(168,85,247,.25),transparent 42%),rgba(2,6,23,.32);
    border-radius:21px;
    padding:22px 16px;
    text-align:center;
    margin-bottom:14px;
}
.upload-icon{
    font-size:34px;
    filter:drop-shadow(0 0 22px rgba(168,85,247,.75));
}
.upload-title{
    margin-top:8px;
    font-size:17px;
    font-weight:800;
    color:#F8FAFC;
}
.upload-sub{
    margin-top:6px;
    color:#94A3B8;
    font-size:13px;
    line-height:1.5;
}

div[data-testid="stFileUploader"]{
    background:rgba(30,41,59,.70);
    border:1px solid rgba(255,255,255,.10);
    border-radius:16px;
    padding:12px;
}
div[data-testid="stFileUploader"] section{border:none!important;}

.stButton>button{
    border-radius:15px!important;
    min-height:46px;
    font-weight:850!important;
    border:1px solid rgba(255,255,255,.12)!important;
    background:linear-gradient(135deg,#2563EB,#C026D3)!important;
    color:white!important;
    box-shadow:0 14px 36px rgba(147,51,234,.23);
}
.stButton>button:hover{
    transform:translateY(-1px);
    box-shadow:0 18px 46px rgba(37,99,235,.35);
}

.ready{
    padding:13px 14px;
    margin:12px 0;
    border-radius:14px;
    background:rgba(34,197,94,.13);
    border:1px solid rgba(34,197,94,.24);
    color:#86EFAC;
    font-weight:800;
}

.docs-title{
    display:flex;
    justify-content:space-between;
    margin:20px 0 11px;
    color:#E879F9;
    font-size:18px;
    font-weight:900;
}
.count{
    background:rgba(255,255,255,.08);
    border:1px solid rgba(255,255,255,.08);
    padding:4px 10px;
    border-radius:999px;
    color:#CBD5E1;
    font-size:12px;
}
.doc-card{
    padding:13px 14px;
    margin-bottom:10px;
    border-radius:16px;
    background:linear-gradient(135deg,rgba(255,255,255,.075),rgba(255,255,255,.025));
    border:1px solid rgba(255,255,255,.10);
}
.doc-row{display:flex;gap:12px;align-items:center;}
.pdf-icon{
    min-width:40px;height:40px;
    border-radius:13px;
    background:linear-gradient(135deg,#EF4444,#F97316);
    display:flex;
    justify-content:center;
    align-items:center;
    font-size:11px;
    font-weight:900;
    color:white;
}
.doc-name{
    font-size:14px;
    font-weight:850;
    color:#F8FAFC;
    overflow-wrap:anywhere;
}
.doc-meta{font-size:12px;color:#94A3B8;margin-top:3px;}
.doc-status{font-size:12px;font-weight:800;color:#4ADE80;margin-top:4px;}

.empty{
    padding:15px;
    border-radius:14px;
    background:rgba(59,130,246,.13);
    border:1px solid rgba(59,130,246,.20);
    color:#93C5FD;
    font-weight:650;
}

.tip{
    margin-top:16px;
    padding:14px;
    border-radius:16px;
    background:rgba(168,85,247,.12);
    border:1px solid rgba(168,85,247,.22);
    color:#CBD5E1;
    font-size:13px;
    line-height:1.55;
}

.chat-head{
    padding:10px 6px 18px;
    border-bottom:1px solid rgba(255,255,255,.07);
    margin-bottom:15px;
}
.chat-title{
    font-size:30px;
    font-weight:950;
    letter-spacing:-1px;
    background:linear-gradient(90deg,#F472B6,#A78BFA,#38BDF8);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}
.chat-sub{color:#94A3B8;margin-top:5px;font-size:14px;}
.mode{
    display:inline-block;
    margin-top:10px;
    padding:7px 12px;
    border-radius:999px;
    background:rgba(34,211,238,.12);
    border:1px solid rgba(34,211,238,.24);
    color:#67E8F9;
    font-size:12px;
    font-weight:850;
}

div[data-testid="stChatMessage"]{
    border-radius:19px;
    padding:9px 14px;
    margin-bottom:12px;
    border:1px solid rgba(255,255,255,.09);
    background:linear-gradient(135deg,rgba(30,41,59,.72),rgba(15,23,42,.66));
}

div[data-testid="stChatInput"] textarea{
    border-radius:18px!important;
    border:1px solid rgba(168,85,247,.40)!important;
    background:rgba(15,23,42,.92)!important;
}

.source-card{
    padding:12px;
    border-radius:14px;
    background:rgba(15,23,42,.78);
    border:1px solid rgba(255,255,255,.10);
    margin-bottom:9px;
}
.source-title{color:#F8FAFC;font-weight:850;font-size:13px;}
.source-page{color:#94A3B8;font-size:12px;margin-top:4px;}
.footer{text-align:center;color:#64748B;font-size:12px;margin-top:14px;}
</style>
""", unsafe_allow_html=True)


def get_file_size(filename):
    try:
        path = os.path.join(UPLOAD_FOLDER, filename)
        size = os.path.getsize(path)
        if size < 1024 * 1024:
            return f"{size / 1024:.1f} KB"
        return f"{size / (1024 * 1024):.1f} MB"
    except Exception:
        return "Ready"


def doc_card(doc):
    st.markdown(f"""
    <div class="doc-card">
        <div class="doc-row">
            <div class="pdf-icon">PDF</div>
            <div>
                <div class="doc-name">{doc}</div>
                <div class="doc-meta">{get_file_size(doc)}</div>
                <div class="doc-status">✓ Indexed</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_sidebar(doc_count):
    with st.sidebar:
        st.markdown(f"""
        <div class="brand">
            <div class="brand-title">📄 DocuMind <span>AI</span></div>
            <div class="brand-sub">Your AI document assistant</div>
        </div>

        <div class="nav-main">💬 Chat</div>


        <div class="side-card">
            <div style="font-weight:850;margin-bottom:8px;">Storage</div>
            <div style="font-size:30px;font-weight:900;color:#67E8F9;">{doc_count}</div>
            <div style="color:#94A3B8;font-size:13px;">indexed document(s)</div>
        </div>

        <div class="side-card">
            <div style="font-weight:850;margin-bottom:8px;">💡 Tip</div>
            <div style="color:#CBD5E1;font-size:13px;line-height:1.55;">
                Upload PDFs for document answers, or ask without PDFs for normal AI chat.
            </div>
        </div>
        """, unsafe_allow_html=True)


documents = get_uploaded_documents()
render_sidebar(len(documents))

st.markdown('<div class="app-shell">', unsafe_allow_html=True)

left, right = st.columns([0.92, 2.08], gap="large")

with left:
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.markdown("""
    <div class="panel-heading">
        <span>Upload PDFs</span>
        <span>☁️</span>
    </div>

    <div class="upload-box">
        <div class="upload-icon">☁️</div>
        <div class="upload-title">Drop PDFs here</div>
        <div class="upload-sub">or browse files below<br>Supports multiple PDFs</div>
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
            f'<div class="ready">Ready to index {len(uploaded_files)} document(s).</div>',
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
            <span class="count">{len(documents)}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    if documents:
        for doc in documents:
            doc_card(doc)

        selected_document = st.selectbox(
            "Search in",
            ["All Documents"] + documents,
            index=0
        )
    else:
        selected_document = "All Documents"
        st.markdown('<div class="empty">No documents indexed yet.</div>', unsafe_allow_html=True)

    smart_mode = st.toggle("🌐 Answer normally when no PDF is indexed", value=True)

    st.markdown("""
    <div class="tip">
        ✨ Ask naturally: summarize, compare, extract key points, or ask a normal question.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="glass chat-panel">', unsafe_allow_html=True)

    mode = "Document Mode" if documents else "General AI Mode"
    if documents and smart_mode:
        mode = "Smart Document Mode"

    st.markdown(f"""
    <div class="chat-head">
        <div class="chat-title">👋 Hello! How can I help you today?</div>
        <div class="chat-sub">Ask anything. Use indexed PDFs when available, or chat normally without uploads.</div>
        <div class="mode">{mode}</div>
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
        if st.button("Clear Chat"):
            st.session_state.messages = []
            st.rerun()

    for message in st.session_state.messages:
        role = message.get("role", "assistant")
        content = message.get("content", "")
        if content:
            with st.chat_message(role):
                st.markdown(content)

    question = st.chat_input("Ask anything about your documents...", key="main_chat_input")

    if question:
        st.session_state.messages.append({"role": "user", "content": question})

        with st.chat_message("user"):
            st.markdown(question)

        history = build_chat_history(st.session_state.messages)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                fresh_documents = get_uploaded_documents()

                if fresh_documents:
                    answer, docs = ask_question(question, history, selected_document)
                else:
                    answer = ask_web_question(question, history)
                    docs = []

            st.markdown(answer)

            sources = format_sources(docs)
            if sources:
                st.markdown("#### 📚 Sources")
                for i, source in enumerate(sources, start=1):
                    st.markdown(
                        f"""
                        <div class="source-card">
                            <div class="source-title">Source {i}: 📄 {source["document"]}</div>
                            <div class="source-page">Page {source["page"]}</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

        st.session_state.messages.append({"role": "assistant", "content": answer})

    st.markdown('<div class="footer">AI can make mistakes. Verify important information.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
