import os
import base64
import streamlit as st

from core.bridge import SynergiaBridge

from ui.runtime_panel import (
    render_runtime,
    render_models
)

from ui.terminal_panel import (
    render_terminal
)

from graph_engine.live_graph import (
    render_live_graph
)

from live_agents.agent_runtime import (
    render_live_agents
)


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="SYNERGIA OS v2",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================================
# INIT SYSTEM
# =====================================================

bridge = SynergiaBridge()


# =====================================================
# LOAD BACKGROUND
# =====================================================

banner_path = "assets/synergia_banner.jpg"

background_style = ""

if os.path.exists(banner_path):

    with open(banner_path, "rb") as image_file:

        encoded = base64.b64encode(
            image_file.read()
        ).decode()

    background_style = f"""

    background-image:
        linear-gradient(
            rgba(0,0,0,0.50),
            rgba(0,0,0,0.62)
        ),
        url("data:image/jpg;base64,{encoded}");

    background-size: cover;

    background-position: center;

    background-attachment: fixed;
    """


# =====================================================
# GLOBAL CSS
# =====================================================

st.markdown(
    f"""
    <style>

    /* ================================================= */
    /* MAIN APP                                           */
    /* ================================================= */

    .stApp {{

        {background_style}
    }}

    /* ================================================= */
    /* TITLES                                             */
    /* ================================================= */

    h1 {{

        color: #74F9FF;

        text-align: center;

        font-size: 58px;

        font-weight: 900;

        letter-spacing: 2px;

        text-shadow:
            0 0 10px rgba(91,231,255,0.95),
            0 0 25px rgba(91,231,255,0.75),
            0 0 40px rgba(91,231,255,0.45);
    }}

    h2, h3, h4 {{

        color: white;
    }}

    /* ================================================= */
    /* GLASS PANELS                                       */
    /* ================================================= */

    div[data-testid="stVerticalBlock"] > div:has(div.stButton) {{

        background:
            rgba(15,15,15,0.25);

        border:
            1px solid rgba(255,255,255,0.08);

        border-radius: 18px;

        padding: 25px;

        backdrop-filter: blur(12px);

        box-shadow:
            0 0 18px rgba(0,255,255,0.12),
            0 0 35px rgba(0,255,255,0.05);
    }}

    /* ================================================= */
    /* BUTTONS                                            */
    /* ================================================= */

    .stButton > button {{

        width: 100%;

        background:
            linear-gradient(
                90deg,
                #00FFF7,
                #00C6FF
            );

        color: black;

        border: none;

        border-radius: 14px;

        padding: 14px;

        font-size: 18px;

        font-weight: bold;

        transition: 0.3s;
    }}

    .stButton > button:hover {{

        transform: scale(1.03);

        box-shadow:
            0 0 24px rgba(0,255,247,0.45);
    }}

    /* ================================================= */
    /* TEXT AREA                                          */
    /* ================================================= */

    textarea {{

        background:
            rgba(0,0,0,0.42) !important;

        color: white !important;

        border-radius: 14px !important;

        border:
            1px solid rgba(255,255,255,0.08) !important;

        font-size: 16px !important;
    }}

    /* ================================================= */
    /* SIDEBAR                                            */
    /* ================================================= */

    section[data-testid="stSidebar"] {{

        background:
            rgba(0,0,0,0.65);

        border-right:
            1px solid rgba(255,255,255,0.08);
    }}

    /* ================================================= */
    /* METRICS                                            */
    /* ================================================= */

    div[data-testid="metric-container"] {{

        background:
            rgba(0,0,0,0.28);

        border:
            1px solid rgba(255,255,255,0.06);

        border-radius: 14px;

        padding: 12px;

        box-shadow:
            0 0 12px rgba(0,255,255,0.05);
    }}

    /* ================================================= */
    /* CODE BLOCKS                                        */
    /* ================================================= */

    pre {{

        border-radius: 12px !important;

        border:
            1px solid rgba(255,255,255,0.08);

        background:
            rgba(0,0,0,0.45) !important;
    }}

    /* ================================================= */
    /* EXECUTION COMPLETE                                 */
    /* ================================================= */

    .finish-box {{

        animation: pulse 1.2s infinite;

        background:
            linear-gradient(
                90deg,
                rgba(0,255,180,0.18),
                rgba(0,180,255,0.18)
            );

        border:
            1px solid rgba(0,255,255,0.35);

        padding: 18px;

        border-radius: 14px;

        text-align: center;

        font-size: 22px;

        font-weight: bold;

        color: #00FFF7;

        box-shadow:
            0 0 18px rgba(0,255,255,0.25);
    }}

    @keyframes pulse {{

        0% {{

            box-shadow:
                0 0 8px rgba(0,255,255,0.15);
        }}

        50% {{

            box-shadow:
                0 0 28px rgba(0,255,255,0.55);
        }}

        100% {{

            box-shadow:
                0 0 8px rgba(0,255,255,0.15);
        }}
    }}

    /* ================================================= */
    /* TERMINAL BOX                                       */
    /* ================================================= */

    .terminal-box {{

        background:
            rgba(0,0,0,0.60);

        border:
            1px solid rgba(0,255,255,0.15);

        border-radius: 14px;

        padding: 22px;

        color: #00FFAA;

        font-family: monospace;

        font-size: 15px;

        box-shadow:
            0 0 18px rgba(0,255,255,0.08);
    }}

    hr {{

        border:
            1px solid rgba(255,255,255,0.08);
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# =====================================================
# HEADER
# =====================================================

st.title("🧠 SYNERGIA OS v2")

st.markdown(
    """
    <h3 style='text-align:center;color:#D8D8D8;'>

    AI Cognitive Operating System

    </h3>
    """,
    unsafe_allow_html=True
)

st.markdown("---")


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.header("⚙️ CONTROL CENTER")

    mode = st.selectbox(
        "Execution Mode",
        [
            "AUTONOMOUS",
            "HYBRID",
            "MANUAL"
        ]
    )

    st.success("SYSTEM ONLINE")

    st.info("UREngine Runtime ACTIVE")

    st.markdown("---")

    st.subheader("🧠 ACTIVE SYSTEMS")

    st.write("✅ Runtime Engine")
    st.write("✅ Memory Engine")
    st.write("✅ Node Engine")
    st.write("✅ Graph Engine")
    st.write("✅ Multi-Agent System")

    st.markdown("---")

    st.subheader("🤖 ACTIVE AI MODELS")

    st.write("🟢 llama3")
    st.write("🔵 qwen2.5-coder")
    st.write("🟣 deepseek-coder")
    st.write("🟠 phi3")

    st.markdown("---")

    st.subheader("📡 LIVE STATUS")

    st.metric("Runtime", "ONLINE")
    st.metric("Memory", "ACTIVE")
    st.metric("Agents", "READY")
    st.metric("Graph", "RUNNING")


# =====================================================
# MAIN LAYOUT
# =====================================================

left, right = st.columns([2, 1])


# =====================================================
# LEFT PANEL
# =====================================================

with left:

    st.subheader("🧠 TASK INPUT")

    task = st.text_area(
        "Enter your request",
        height=220,
        placeholder="""
Ejemplos:

• crear CRM inmobiliario con IA y automatización
• automatizar Instagram para restaurantes
• crear plataforma SaaS educativa
• generar backend FastAPI enterprise
• crear dashboard analytics premium
• construir arquitectura SaaS escalable
• crear startup digital automatizada
• generar ecosistema IA multiagente
"""
    )

    execute = st.button(
        "🚀 EXECUTE TASK"
    )


# =====================================================
# RIGHT PANEL
# =====================================================

with right:

    st.subheader("⚡ LIVE ENGINE")

    st.metric("UREngine", "ACTIVE")
    st.metric("Runtime", "ONLINE")
    st.metric("Memory", "CONNECTED")
    st.metric("Agents", "READY")


# =====================================================
# EXECUTION
# =====================================================

if execute and task:

    st.markdown("---")

    st.header("⚡ LIVE EXECUTION")

    progress = st.progress(0)

    status = st.empty()

    # =================================================
    # INITIALIZING
    # =================================================

    status.info("🟡 INITIALIZING SYSTEM")
    progress.progress(10)

    # =================================================
    # RUN ENGINE
    # =================================================

    result = bridge.run(task, mode)

    # =================================================
    # EXECUTION FLOW
    # =================================================

    status.info("🧠 ACTIVATING AGENTS")
    progress.progress(30)

    status.info("⚡ RUNNING ENGINE")
    progress.progress(50)

    status.info("🎮 BUILDING NODE GRAPH")
    progress.progress(70)

    status.info("💾 SAVING MEMORY")
    progress.progress(90)

    status.success("🟢 EXECUTION COMPLETE")
    progress.progress(100)

    # =================================================
    # COMPLETE EFFECT
    # =================================================

    st.markdown(
        """
        <div class="finish-box">

            ⚡ SYNERGIA EXECUTION COMPLETE

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # =================================================
    # LIVE TERMINAL
    # =================================================

    st.subheader("🖥️ LIVE TERMINAL")

    st.markdown(
        f"""
        <div class="terminal-box">

        [OK] Runtime Connected <br><br>

        [OK] Agents Activated <br><br>

        [OK] Memory Engine Active <br><br>

        [OK] Graph Generated <br><br>

        [OK] Task: {task} <br><br>

        [OK] Execution Complete

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # =================================================
    # LIVE AGENT EXECUTION
    # =================================================

    render_live_agents(
        result["runtime"]
    )

    st.markdown("---")

    # =================================================
    # RUNTIME PANEL
    # =================================================

    render_runtime(
        result["runtime"]
    )

    st.markdown("---")

    # =================================================
    # MODELS PANEL
    # =================================================

    render_models(
        result["runtime"]
    )

    st.markdown("---")

    # =================================================
    # MEMORY FILE
    # =================================================

    st.subheader("💾 MEMORY FILE")

    st.code(
        result["memory_file"]
    )

    st.markdown("---")

    # =================================================
    # LIVE GRAPH ENGINE
    # =================================================

    render_live_graph(
        result["graph"]
    )

    st.markdown("---")

    # =================================================
    # FULL OUTPUT
    # =================================================

    st.subheader("📦 FULL SYSTEM OUTPUT")

    st.json(result)

else:

    st.info("🧠 Waiting for execution...")
