# ============================================
# SYNERGIA VISUAL OS v1
# STREAMLIT CONTROL CENTER
# ============================================

import streamlit as st
from core.mode_manager import set_mode
from core.synergia_bridge import run_synergia


# ============================================
# UI CONFIG
# ============================================

st.set_page_config(page_title="SYNERGIA OS", layout="wide")

st.title("🧠 SYNERGIA VISUAL OPERATING SYSTEM v1")


# ============================================
# MODE SELECTOR
# ============================================

st.sidebar.header("⚙️ SYSTEM MODE")

mode = st.sidebar.radio(
    "Select Mode",
    ["AUTONOMOUS", "HYBRID", "MANUAL"]
)

set_mode(mode)


# ============================================
# TASK INPUT
# ============================================

st.header("🚀 Task Input")

task = st.text_input("Enter your request:")

if st.button("RUN SYNERGIA"):

    if task:

        result = run_synergia(task, mode)

        st.success("Execution completed")

        st.subheader("📦 OUTPUT")
        st.write(result)

    else:
        st.warning("Please enter a task")


# ============================================
# SYSTEM INFO
# ============================================

st.sidebar.markdown("---")
st.sidebar.info("SYNERGIA OS v1 - AI Operating System Core")
