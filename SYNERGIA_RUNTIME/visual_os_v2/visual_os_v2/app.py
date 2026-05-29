# =========================================================
# SYNERGIA OS v3
# LIVE VISUAL OPERATING SYSTEM
# =========================================================

import streamlit as st
from datetime import datetime

from core.bridge import SynergiaBridge

from canvas.live_brain_canvas import LiveBrainCanvas


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="SYNERGIA OS v3",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

html, body, [class*="css"]  {
    background-color: #0A0F1C;
    color: white;
}

.block-container {
    padding-top: 1rem;
}

.main-title {
    font-size: 42px;
    font-weight: bold;
    color: #00FFD0;
}

.subtitle {
    color: #8FA3BF;
    font-size: 18px;
}

.sy-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 18px;
    border-radius: 16px;
    margin-bottom: 15px;
}

.agent-card {
    background: rgba(0,255,180,0.05);
    border: 1px solid rgba(0,255,180,0.2);
    padding: 12px;
    border-radius: 14px;
    margin-bottom: 10px;
}

.status-online {
    color: #00FF99;
    font-weight: bold;
}

canvas {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.image("assets/synergia_banner.jpg")

    st.markdown("## 🧠 SYNERGIA OS v3")

    st.markdown("---")

    st.markdown("### ⚡ Runtime")

    st.success("ONLINE")

    st.markdown("### 🤖 AI Models")

    st.info("llama3")
    st.info("qwen2.5-coder:7b")
    st.info("mistral")
    st.info("phi3")

    st.markdown("---")

    st.markdown("### 🧠 Cognitive Layer")

    st.write("✔ Agent Runtime")
    st.write("✔ Memory Engine")
    st.write("✔ Ollama Runtime")
    st.write("✔ Live Canvas")
    st.write("✔ Graph Engine")

# =========================================================
# MAIN HEADER
# =========================================================

st.markdown("""
<div class='main-title'>
🚀 SYNERGIA LIVE BRAIN OS
</div>

<div class='subtitle'>
AI Cognitive Operating System
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================================================
# TASK INPUT
# =========================================================

task = st.text_area(
    "🧠 TASK INPUT",
    height=120,
    placeholder="Ej: crear SaaS para restaurantes IA..."
)

mode = st.selectbox(
    "⚙️ EXECUTION MODE",
    [
        "AUTONOMOUS",
        "ASSISTED",
        "AGENT"
    ]
)

# =========================================================
# EXECUTION
# =========================================================

if st.button("🚀 EXECUTE SYNERGIA"):

    bridge = SynergiaBridge()

    result = bridge.run(
        task=task,
        mode=mode
    )

    st.success("✅ SYNERGIA EXECUTION COMPLETE")

    # =====================================================
    # RUNTIME STATUS
    # =====================================================

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Agents", len(result["runtime"]["agents"]))
    col2.metric("Models", len(result["runtime"]["models"]))
    col3.metric("Events", len(result["events"]))
    col4.metric("Nodes", len(result["nodes"]))

    st.markdown("---")

    # =====================================================
    # LIVE AGENTS
    # =====================================================

    st.subheader("🤖 LIVE AGENT EXECUTION")

    for output in result["runtime"]["ollama_outputs"]:

        with st.container():

            st.markdown(f"""
            <div class='agent-card'>
            <h4>🧠 {output["agent"].upper()}</h4>
            <b>MODEL:</b> {output["model"]}
            </div>
            """, unsafe_allow_html=True)

            st.code(output["response"])

    # =====================================================
    # LIVE EVENTS
    # =====================================================

    st.subheader("📡 LIVE AGENT EVENTS")

    for event in result["events"]:

        st.markdown(f"""
        <div class='sy-card'>
        <b>{event["sender"]}</b>
        →
        <b>{event["target"]}</b>

        <br><br>

        TYPE:
        <span class='status-online'>
        {event["type"]}
        </span>

        <br><br>

        {event["content"]}
        </div>
        """, unsafe_allow_html=True)

    # =====================================================
    # LIVE BRAIN CANVAS
    # =====================================================

    st.subheader("🧠 LIVE BRAIN CANVAS")

    canvas = LiveBrainCanvas()

    canvas.load_graph(
        result["graph"]
    )

    canvas.load_events(
        result["events"]
    )

    canvas.render()

    # =====================================================
    # MEMORY
    # =====================================================

    st.subheader("💾 MEMORY")

    st.code(result["memory_file"])

    # =====================================================
    # FINAL OUTPUT
    # =====================================================

    with st.expander("📦 FULL SYSTEM OUTPUT"):

        st.json(result)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    f"SYNERGIA OS v3 — {datetime.now()}"
)
