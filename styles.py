import streamlit as st

def inject_css():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(circle at 12% 12%, rgba(168,85,247,.24), transparent 28%),
        radial-gradient(circle at 88% 10%, rgba(59,130,246,.20), transparent 28%),
        radial-gradient(circle at 78% 88%, rgba(236,72,153,.12), transparent 26%),
        linear-gradient(135deg, #070A16 0%, #0B1020 50%, #0F172A 100%);
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1540px;
    padding-top: 1rem;
    padding-bottom: 1rem;
}

section[data-testid="stSidebar"] {
    background:
        radial-gradient(circle at 45% 0%, rgba(124,58,237,.40), transparent 30%),
        linear-gradient(180deg, rgba(15,23,42,.98), rgba(2,6,23,.98));
    border-right: 1px solid rgba(255,255,255,.09);
}

section[data-testid="stSidebar"] * {
    color: #F8FAFC;
}

.sidebar-brand {
    padding: 18px 4px 20px;
}

.sidebar-brand-title {
    font-size: 28px;
    font-weight: 900;
    letter-spacing: -1px;
}

.sidebar-brand-title span {
    background: linear-gradient(90deg,#60A5FA,#E879F9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.sidebar-brand-sub {
    color: #94A3B8;
    font-size: 13px;
    margin-top: 4px;
}

.sidebar-new-chat {
    margin-top: 14px;
    padding: 15px 16px;
    border-radius: 16px;
    background: linear-gradient(135deg,#A855F7,#2563EB);
    font-weight: 800;
    box-shadow: 0 18px 45px rgba(37,99,235,.28);
}

.sidebar-item {
    margin-top: 10px;
    padding: 13px 15px;
    border-radius: 15px;
    background: rgba(255,255,255,.055);
    border: 1px solid rgba(255,255,255,.07);
    color: #CBD5E1;
    font-weight: 700;
}

.sidebar-box {
    margin-top: 24px;
    padding: 17px;
    border-radius: 18px;
    background: linear-gradient(135deg, rgba(88,28,135,.45), rgba(37,99,235,.20));
    border: 1px solid rgba(168,85,247,.28);
}

.sidebar-big {
    font-size: 30px;
    font-weight: 900;
    color: #67E8F9;
}

.app-shell {
    min-height: 91vh;
    padding: 18px;
    border-radius: 28px;
    background: rgba(15,23,42,.52);
    border: 1px solid rgba(255,255,255,.09);
    box-shadow: 0 28px 90px rgba(0,0,0,.40);
    backdrop-filter: blur(18px);
}

.left-panel,
.chat-panel {
    border-radius: 24px;
    padding: 20px;
    background:
        linear-gradient(180deg, rgba(17,24,39,.92), rgba(15,23,42,.78));
    border: 1px solid rgba(255,255,255,.10);
    box-shadow: 0 20px 70px rgba(0,0,0,.28);
}

.panel-heading {
    font-size: 20px;
    font-weight: 900;
    margin-bottom: 14px;
    color: #E879F9;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.upload-visual {
    border: 1.5px dashed rgba(168,85,247,.58);
    background:
        radial-gradient(circle at 50% 18%, rgba(168,85,247,.25), transparent 42%),
        rgba(2,6,23,.32);
    border-radius: 21px;
    text-align: center;
    padding: 30px 18px;
    margin-bottom: 14px;
}

.upload-visual-icon {
    font-size: 48px;
    filter: drop-shadow(0 0 22px rgba(168,85,247,.75));
}

.upload-visual-title {
    margin-top: 8px;
    font-size: 17px;
    font-weight: 800;
    color: #F8FAFC;
}

.upload-visual-sub {
    margin-top: 6px;
    color: #94A3B8;
    font-size: 13px;
    line-height: 1.5;
}

div[data-testid="stFileUploader"] {
    padding: 12px;
    border-radius: 16px;
    background: rgba(30,41,59,.70);
    border: 1px solid rgba(255,255,255,.10);
    margin-bottom: 12px;
}

div[data-testid="stFileUploader"] section {
    border: none !important;
}

.stButton > button {
    border-radius: 15px !important;
    min-height: 46px;
    font-weight: 850 !important;
    border: 1px solid rgba(255,255,255,.12) !important;
    background: linear-gradient(135deg,#2563EB,#C026D3) !important;
    color: white !important;
    box-shadow: 0 14px 36px rgba(147,51,234,.23);
}

.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 18px 46px rgba(37,99,235,.35);
}

.status-ready {
    padding: 13px 14px;
    margin: 11px 0 12px;
    border-radius: 14px;
    background: rgba(34,197,94,.13);
    border: 1px solid rgba(34,197,94,.24);
    color: #86EFAC;
    font-weight: 800;
}

.docs-title {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 20px 0 11px;
    color: #E879F9;
    font-size: 18px;
    font-weight: 900;
}

.docs-count {
    background: rgba(255,255,255,.08);
    border: 1px solid rgba(255,255,255,.08);
    padding: 4px 10px;
    border-radius: 999px;
    color: #CBD5E1;
    font-size: 12px;
}

.doc-card {
    padding: 13px 14px;
    margin-bottom: 10px;
    border-radius: 16px;
    background: linear-gradient(135deg, rgba(255,255,255,.075), rgba(255,255,255,.025));
    border: 1px solid rgba(255,255,255,.10);
    transition: .2s ease;
}

.doc-card:hover {
    transform: translateY(-2px);
    border-color: rgba(168,85,247,.48);
    box-shadow: 0 15px 34px rgba(0,0,0,.25);
}

.doc-row {
    display: flex;
    gap: 12px;
    align-items: center;
}

.pdf-icon {
    min-width: 40px;
    height: 40px;
    border-radius: 13px;
    background: linear-gradient(135deg,#EF4444,#F97316);
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 11px;
    font-weight: 900;
    color: white;
    box-shadow: 0 10px 24px rgba(239,68,68,.20);
}

.doc-name {
    font-size: 14px;
    font-weight: 850;
    color: #F8FAFC;
    overflow-wrap: anywhere;
}

.doc-meta {
    font-size: 12px;
    color: #94A3B8;
    margin-top: 3px;
}

.doc-status {
    font-size: 12px;
    font-weight: 800;
    color: #4ADE80;
    margin-top: 4px;
}

.empty-doc {
    padding: 15px;
    border-radius: 14px;
    background: rgba(59,130,246,.13);
    border: 1px solid rgba(59,130,246,.20);
    color: #93C5FD;
    font-weight: 650;
}

div[data-baseweb="select"] > div {
    border-radius: 15px;
    background: rgba(15,23,42,.78);
    border-color: rgba(255,255,255,.12);
}

.tip-card {
    margin-top: 16px;
    padding: 14px;
    border-radius: 16px;
    background: rgba(168,85,247,.12);
    border: 1px solid rgba(168,85,247,.22);
    color: #CBD5E1;
    font-size: 13px;
    line-height: 1.55;
}

.chat-panel {
    min-height: 84vh;
}

.chat-hero {
    padding: 10px 6px 18px;
    border-bottom: 1px solid rgba(255,255,255,.07);
    margin-bottom: 15px;
}

.chat-title {
    font-size: 30px;
    font-weight: 950;
    letter-spacing: -1px;
    background: linear-gradient(90deg,#F472B6,#A78BFA,#38BDF8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.chat-sub {
    color: #94A3B8;
    margin-top: 5px;
    font-size: 14px;
}

.mode-pill {
    display: inline-block;
    margin-top: 10px;
    padding: 7px 12px;
    border-radius: 999px;
    background: rgba(34,211,238,.12);
    border: 1px solid rgba(34,211,238,.24);
    color: #67E8F9;
    font-size: 12px;
    font-weight: 850;
}

div[data-testid="stChatMessage"] {
    border-radius: 19px;
    padding: 9px 14px;
    margin-bottom: 12px;
    border: 1px solid rgba(255,255,255,.09);
    background: linear-gradient(135deg, rgba(30,41,59,.72), rgba(15,23,42,.66));
}

[data-testid="stChatMessageAvatarUser"] {
    background: linear-gradient(135deg,#A855F7,#2563EB) !important;
}

[data-testid="stChatMessageAvatarAssistant"] {
    background: linear-gradient(135deg,#22D3EE,#A855F7) !important;
}

div[data-testid="stChatInput"] textarea {
    border-radius: 18px !important;
    border: 1px solid rgba(168,85,247,.40) !important;
    background: rgba(15,23,42,.92) !important;
}

.source-card {
    padding: 12px;
    border-radius: 14px;
    background: rgba(15,23,42,.78);
    border: 1px solid rgba(255,255,255,.10);
    margin-bottom: 9px;
}

.source-title {
    color: #F8FAFC;
    font-weight: 850;
    font-size: 13px;
}

.source-page {
    color: #94A3B8;
    font-size: 12px;
    margin-top: 4px;
}

.footer-note {
    text-align: center;
    color: #64748B;
    font-size: 12px;
    margin-top: 14px;
}
</style>
""", unsafe_allow_html=True)
