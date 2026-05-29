# =========================================================
# SYNERGIA OS v2 - STABLE UI + CSS FIXED
# =========================================================

import sys
import os
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from core.bridge import SynergiaBridge
from canvas.live_brain_canvas import LiveBrainCanvas

# =========================================================
# CONFIG
# =========================================================

st.set_page_config(
    page_title="SYNERGIA OS v2",
    layout="wide"
)

bridge = SynergiaBridge()

# =========================================================
# 🎨 CSS (AQUÍ VA TODO EL ESTILO)
# =========================================================

st.markdown("""
<style>

/* BACKGROUND GENERAL */
.main {
    background-color: #0e1117;
}

/* HEADER / BANNER */
.synergia-header {
    background: rgba(40,40,40,0.65);
    padding: 12px;
    border-radius: 14px;
    margin-bottom: 15px;
    box-shadow: 0 0 25px rgba(0,255,200,0.12);
}

/* INPUT BOX */
.stTextInput > div > div > input {
    background-color: rgba(255,255,255,0.05);
    color: white;
}

/* BUTTON */
.stButton > button {
    background: linear-gradient(90deg, #00ffc8, #0066ff);
    color: black;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #0b0f1a;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER / BANNER
# =========================================================

logo_path = os.path.join(BASE_DIR, "assets", "synergia_banner.jpg")

st.markdown('<div class="synergia-header">', unsafe_allow_html=True)

if os.path.exists(logo_path):
    st.image(logo_path, use_container_width=True)
else:
    st.title("🧠 SYNERGIA OS v2")

st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.title("⚙️ CONTROL CENTER")

    mode = st.selectbox("Mode", ["AUTONOMOUS", "ASSISTED"])

    st.markdown("---")
    st.write("Runtime: ONLINE")
    st.write("Memory: ACTIVE")
    st.write("Agents: READY")
    st.write("Ollama: CONNECTED")

# =========================================================
# INPUT
# =========================================================

st.title("🧠 TASK ENGINE")

task = st.text_input("Enter your request")
run = st.button("🚀 EXECUTE")

# =========================================================
# EXECUTION
# =========================================================

if run and task:

    result = bridge.run(task, mode)

    st.success("⚡ EXECUTION COMPLETE")

    runtime = result.get("runtime", {})

    # AGENTS
    st.subheader("🤖 AGENTS")
    for a in runtime.get("agents", []):
        st.write(f"🧠 {a}")

    # OLLAMA
    st.subheader("🤖 OLLAMA")
    for o in runtime.get("ollama_outputs", []):
        st.write(o)

    # CANVAS
    st.subheader("🧠 LIVE BRAIN CANVAS")

    brain = LiveBrainCanvas()
    brain.load_runtime(runtime)
    brain.render()

else:
    st.info("Enter a task to start")
