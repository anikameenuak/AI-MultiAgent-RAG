import streamlit as st
from graph.workflow import build_graph

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"], .stApp {
    font-family: 'Space Grotesk', sans-serif !important;
    background: #060612 !important;
    color: #f0eeff !important;
}

section[data-testid="stSidebar"] { display: none; }
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

.hero {
    background: #060612;
    padding: 60px 60px 40px;
    position: relative;
    overflow: hidden;
    border-bottom: 1px solid #1a1535;
}

.hero-bg {
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse 60% 50% at 20% 50%, rgba(99,57,255,0.18) 0%, transparent 70%),
        radial-gradient(ellipse 40% 60% at 80% 30%, rgba(0,212,170,0.12) 0%, transparent 70%),
        radial-gradient(ellipse 30% 40% at 60% 80%, rgba(255,77,141,0.10) 0%, transparent 70%);
    pointer-events: none;
}

.hero-content { position: relative; z-index: 1; }

.eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(99,57,255,0.15);
    border: 1px solid rgba(99,57,255,0.4);
    border-radius: 999px;
    padding: 6px 16px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #a98bff;
    margin-bottom: 24px;
}

.pulse {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #6339ff;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.8); }
}

.hero-title {
    font-size: 64px;
    font-weight: 700;
    line-height: 1.05;
    letter-spacing: -2px;
    color: #ffffff;
    margin-bottom: 20px;
}

.hero-title .grad1 { color: #6339ff; }
.hero-title .grad2 { color: #00d4aa; }
.hero-title .grad3 { color: #ff4d8d; }

.hero-sub {
    font-size: 17px;
    color: #7a6fa0;
    font-weight: 300;
    max-width: 560px;
    line-height: 1.7;
    margin-bottom: 40px;
}

.tech-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 50px;
}

.pill {
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 500;
    letter-spacing: 0.3px;
    border: 1px solid;
}

.pill-purple { background: rgba(99,57,255,0.12); border-color: rgba(99,57,255,0.35); color: #a98bff; }
.pill-teal   { background: rgba(0,212,170,0.10); border-color: rgba(0,212,170,0.30); color: #00d4aa; }
.pill-pink   { background: rgba(255,77,141,0.10); border-color: rgba(255,77,141,0.30); color: #ff4d8d; }
.pill-amber  { background: rgba(255,180,0,0.10);  border-color: rgba(255,180,0,0.30);  color: #ffb400; }

.pipeline-wrap {
    display: flex;
    align-items: center;
    gap: 0;
}

.pipe-step {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 20px;
    border-radius: 10px;
    border: 1px solid;
    font-size: 13px;
    font-weight: 500;
}

.pipe-1 { background: rgba(99,57,255,0.12); border-color: rgba(99,57,255,0.4); color: #a98bff; }
.pipe-2 { background: rgba(0,212,170,0.10); border-color: rgba(0,212,170,0.35); color: #00d4aa; }
.pipe-3 { background: rgba(255,180,0,0.10);  border-color: rgba(255,180,0,0.35);  color: #ffb400; }
.pipe-4 { background: rgba(255,77,141,0.10); border-color: rgba(255,77,141,0.35); color: #ff4d8d; }

.pipe-icon {
    width: 26px; height: 26px;
    border-radius: 6px;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px;
    font-weight: 700;
}
.pi-1 { background: rgba(99,57,255,0.3); color: #d4c4ff; }
.pi-2 { background: rgba(0,212,170,0.25); color: #80ffe8; }
.pi-3 { background: rgba(255,180,0,0.25); color: #ffe080; }
.pi-4 { background: rgba(255,77,141,0.25); color: #ffaac8; }

.pipe-arrow {
    font-size: 18px;
    color: #2a2250;
    padding: 0 8px;
}

.input-zone {
    background: #0c0a1e;
    border-top: 1px solid #1a1535;
    border-bottom: 1px solid #1a1535;
    padding: 40px 60px;
}

.input-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #4a3f6e;
    margin-bottom: 12px;
}

.stTextInput > div > div > input {
    background: #0f0c20 !important;
    border: 1.5px solid #2a2250 !important;
    border-radius: 12px !important;
    color: #f0eeff !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 16px !important;
    padding: 14px 18px !important;
    transition: border-color 0.2s !important;
    height: 52px !important;
}

.stTextInput > div > div > input:focus {
    border-color: #6339ff !important;
    box-shadow: 0 0 0 3px rgba(99,57,255,0.15) !important;
    outline: none !important;
}

.stTextInput > div > div > input::placeholder {
    color: #3d3460 !important;
}

.stButton > button {
    background: #6339ff !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 28px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    font-size: 15px !important;
    letter-spacing: 0.3px !important;
    width: 100% !important;
    height: 52px !important;
    transition: all 0.2s !important;
    cursor: pointer !important;
}

.stButton > button:hover {
    background: #7a52ff !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 12px 30px rgba(99,57,255,0.4) !important;
}

.results-zone {
    padding: 40px 60px;
    background: #060612;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-bottom: 36px;
}

.stat-card {
    border-radius: 14px;
    padding: 20px;
    border: 1px solid;
    text-align: center;
}

.sc-purple { background: rgba(99,57,255,0.08); border-color: rgba(99,57,255,0.25); }
.sc-teal   { background: rgba(0,212,170,0.07); border-color: rgba(0,212,170,0.22); }
.sc-amber  { background: rgba(255,180,0,0.07);  border-color: rgba(255,180,0,0.22);  }
.sc-pink   { background: rgba(255,77,141,0.07); border-color: rgba(255,77,141,0.22); }

.stat-num {
    font-size: 36px;
    font-weight: 700;
    line-height: 1;
    margin-bottom: 6px;
    font-family: 'JetBrains Mono', monospace;
}
.sn-purple { color: #8c6bff; }
.sn-teal   { color: #00d4aa; }
.sn-amber  { color: #ffb400; }
.sn-pink   { color: #ff4d8d; }

.stat-lbl { font-size: 12px; font-weight: 500; letter-spacing: 0.5px; color: #5a4f80; text-transform: uppercase; }

.section-card {
    border-radius: 16px;
    border: 1px solid;
    margin-bottom: 20px;
    overflow: hidden;
}

.sc-hdr {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 16px 22px;
    border-bottom: 1px solid;
    cursor: pointer;
}

.sc-hdr-dot {
    width: 10px; height: 10px;
    border-radius: 50%;
    flex-shrink: 0;
}

.sc-hdr-title {
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    flex: 1;
}

.sc-body {
    padding: 22px;
    font-size: 14px;
    line-height: 1.85;
    font-weight: 300;
}

.section-plan {
    background: rgba(99,57,255,0.05);
    border-color: rgba(99,57,255,0.2);
}
.section-plan .sc-hdr { border-color: rgba(99,57,255,0.2); }
.section-plan .sc-hdr-dot { background: #6339ff; }
.section-plan .sc-hdr-title { color: #a98bff; }
.section-plan .sc-body { color: #c8bff0; }

.section-research {
    background: rgba(0,212,170,0.04);
    border-color: rgba(0,212,170,0.18);
}
.section-research .sc-hdr { border-color: rgba(0,212,170,0.18); }
.section-research .sc-hdr-dot { background: #00d4aa; }
.section-research .sc-hdr-title { color: #00d4aa; }
.section-research .sc-body { color: #b0ffe8; }

.final-card {
    background: rgba(255,77,141,0.05);
    border: 1px solid rgba(255,77,141,0.25);
    border-radius: 16px;
    overflow: hidden;
    margin-top: 8px;
}

.final-hdr {
    background: rgba(255,77,141,0.12);
    border-bottom: 1px solid rgba(255,77,141,0.2);
    padding: 16px 22px;
    display: flex;
    align-items: center;
    gap: 12px;
}

.final-hdr-dot {
    width: 10px; height: 10px;
    border-radius: 50%;
    background: #ff4d8d;
    flex-shrink: 0;
}

.final-hdr-title {
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #ff4d8d;
    flex: 1;
}

.final-badge {
    background: rgba(255,77,141,0.2);
    border: 1px solid rgba(255,77,141,0.35);
    border-radius: 999px;
    padding: 3px 12px;
    font-size: 10px;
    font-weight: 600;
    color: #ff4d8d;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.final-body {
    padding: 28px;
    font-size: 15px;
    line-height: 1.9;
    color: #f0eeff;
    font-weight: 300;
}

.stSpinner > div { border-top-color: #6339ff !important; }

label { color: #4a3f6e !important; font-family: 'Space Grotesk', sans-serif !important; }

.stMarkdown h1, .stMarkdown h2, .stMarkdown h3 { color: #f0eeff !important; }
.stMarkdown p, .stMarkdown li { color: #c8bff0 !important; }
.stMarkdown strong { color: #f0eeff !important; }

div[data-testid="stMarkdownContainer"] p {
    color: inherit !important;
}
</style>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
    <div class="hero-bg"></div>
    <div class="hero-content">
        <div class="eyebrow"><div class="pulse"></div>Multi-Agent System · Active</div>
        <div class="hero-title">
            Research.<br>
            <span class="grad1">Reason.</span>
            <span class="grad2">Write.</span>
            <span class="grad3">Refine.</span>
        </div>
        <p class="hero-sub">
            Four specialized AI agents collaborate in real-time —
            planning, researching, writing, and critiquing — to deliver
            polished, accurate answers to any question.
        </p>
        <div class="tech-pills">
            <span class="pill pill-purple">⚡ LangGraph</span>
            <span class="pill pill-teal">◈ Groq LLaMA 3.3</span>
            <span class="pill pill-pink">◉ ChromaDB RAG</span>
            <span class="pill pill-amber">◎ DuckDuckGo Search</span>
        </div>
        <div class="pipeline-wrap">
            <div class="pipe-step pipe-1"><div class="pipe-icon pi-1">P</div>Planner</div>
            <div class="pipe-arrow">→</div>
            <div class="pipe-step pipe-2"><div class="pipe-icon pi-2">R</div>Researcher</div>
            <div class="pipe-arrow">→</div>
            <div class="pipe-step pipe-3"><div class="pipe-icon pi-3">W</div>Writer</div>
            <div class="pipe-arrow">→</div>
            <div class="pipe-step pipe-4"><div class="pipe-icon pi-4">C</div>Critic</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# INPUT
st.markdown('<div class="input-zone">', unsafe_allow_html=True)
col1, col2 = st.columns([5, 1])
with col1:
    st.markdown('<div class="input-label">Your Research Query</div>', unsafe_allow_html=True)
    query = st.text_input(
        "",
        placeholder="e.g. How does reinforcement learning work in robotics?",
        label_visibility="collapsed"
    )
with col2:
    st.markdown('<div style="margin-top:28px"></div>', unsafe_allow_html=True)
    run = st.button("⚡ Run")
st.markdown('</div>', unsafe_allow_html=True)

# RUN
if run:
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        with st.spinner("Agents working in parallel..."):
            graph = build_graph()
            result = graph.invoke({"query": query})

        plan     = result.get("plan", "")
        research = result.get("research", "")
        final    = result.get("final", "")

        word_count  = len(final.split())
        plan_steps  = len([l for l in plan.split('\n') if l.strip() and l.strip()[0].isdigit()])
        research_wc = len(research.split())

        st.markdown('<div class="results-zone">', unsafe_allow_html=True)

        # Stats
        st.markdown(f"""
        <div class="stats-grid">
            <div class="stat-card sc-purple">
                <div class="stat-num sn-purple">4</div>
                <div class="stat-lbl">Agents Used</div>
            </div>
            <div class="stat-card sc-teal">
                <div class="stat-num sn-teal">{plan_steps}</div>
                <div class="stat-lbl">Plan Steps</div>
            </div>
            <div class="stat-card sc-amber">
                <div class="stat-num sn-amber">{research_wc}</div>
                <div class="stat-lbl">Research Words</div>
            </div>
            <div class="stat-card sc-pink">
                <div class="stat-num sn-pink">{word_count}</div>
                <div class="stat-lbl">Output Words</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Plan
        with st.expander("📋  Execution Plan — Planner Agent", expanded=False):
            st.markdown(plan)

        # Research
        with st.expander("🔍  Research Data — Researcher Agent", expanded=False):
            if research:
                st.markdown(research)
            else:
                st.info("No research data captured.")

        # Final Output
        st.markdown(f"""
        <div class="final-card">
            <div class="final-hdr">
                <div class="final-hdr-dot"></div>
                <div class="final-hdr-title">Final Output — Writer + Critic Agents</div>
                <div class="final-badge">Reviewed</div>
            </div>
            <div class="final-body">{final}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)