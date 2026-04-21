import streamlit as st
import re

st.set_page_config(
    page_title="Word Counter",
    page_icon="✍️",
    layout="centered"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    .stApp {
        background-color: #0f0f0f;
        color: #f0f0f0;
    }

    h1 {
        font-family: 'DM Sans', sans-serif;
        font-weight: 700;
        font-size: 1.8rem !important;
        color: #f0f0f0 !important;
        letter-spacing: -0.5px;
    }

    .subtitle {
        color: #666;
        font-size: 0.85rem;
        margin-top: -12px;
        margin-bottom: 24px;
    }

    textarea {
        font-family: 'DM Mono', monospace !important;
        font-size: 0.9rem !important;
        background-color: #1a1a1a !important;
        color: #e0e0e0 !important;
        border: 1px solid #2a2a2a !important;
        border-radius: 10px !important;
        caret-color: #a3e635;
    }

    textarea:focus {
        border-color: #a3e635 !important;
        box-shadow: 0 0 0 1px #a3e63530 !important;
    }

    .stat-card {
        background: #1a1a1a;
        border: 1px solid #2a2a2a;
        border-radius: 12px;
        padding: 16px 20px;
        text-align: center;
    }

    .stat-number {
        font-family: 'DM Mono', monospace;
        font-size: 2rem;
        font-weight: 500;
        color: #a3e635;
        line-height: 1;
        margin-bottom: 4px;
    }

    .stat-label {
        font-size: 0.72rem;
        color: #555;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .divider {
        border: none;
        border-top: 1px solid #1e1e1e;
        margin: 20px 0;
    }

    .info-row {
        display: flex;
        justify-content: space-between;
        font-family: 'DM Mono', monospace;
        font-size: 0.78rem;
        color: #444;
        padding: 4px 0;
    }

    .info-row span:last-child {
        color: #777;
    }

    .badge-empty {
        display: inline-block;
        background: #1e1e1e;
        color: #444;
        font-size: 0.7rem;
        padding: 2px 8px;
        border-radius: 20px;
        font-family: 'DM Mono', monospace;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .block-container {
        padding-top: 2.5rem !important;
        max-width: 640px !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>✍️ Word Counter</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">Paste or type your text below</p>', unsafe_allow_html=True)

# Text area
text = st.text_area(
    label="",
    placeholder="Paste your text here...",
    height=260,
    label_visibility="collapsed",
    key="main_input"
)

# Stats calculation
char_total = len(text)
char_no_space = len(text.replace(" ", "").replace("\n", "").replace("\t", ""))
words = len(text.split()) if text.strip() else 0
sentences = len([s for s in re.split(r'[.!?]+', text) if s.strip()]) if text.strip() else 0
paragraphs = len([p for p in text.split("\n\n") if p.strip()]) if text.strip() else 0
lines = len([l for l in text.split("\n") if l.strip()]) if text.strip() else 0

# Stat cards
if text.strip():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{char_total:,}</div>
            <div class="stat-label">Characters</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{words:,}</div>
            <div class="stat-label">Words</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{sentences:,}</div>
            <div class="stat-label">Sentences</div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-row"><span>Characters (no spaces)</span><span>{char_no_space:,}</span></div>
    <div class="info-row"><span>Lines</span><span>{lines:,}</span></div>
    <div class="info-row"><span>Paragraphs</span><span>{paragraphs:,}</span></div>
    <div class="info-row"><span>Avg word length</span><span>{(char_no_space / words):.1f} chars</span></div>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div style="text-align:center; padding: 28px 0 16px;">
        <span class="badge-empty">waiting for input...</span>
    </div>
    """, unsafe_allow_html=True)
