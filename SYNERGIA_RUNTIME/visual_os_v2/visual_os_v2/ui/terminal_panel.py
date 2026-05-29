import streamlit as st
import time


# =====================================================
# TERMINAL PANEL
# =====================================================

def render_terminal():

    st.subheader("🖥️ LIVE TERMINAL")

    terminal = st.empty()

    logs = [

        "🟡 INITIALIZING RUNTIME...",
        "🧠 ACTIVATING AGENTS...",
        "⚡ STARTING ENGINE...",
        "🎮 BUILDING GRAPH...",
        "💾 SAVING MEMORY...",
        "🟢 EXECUTION COMPLETE"
    ]

    output = ""

    for log in logs:

        output += log + "\n"

        terminal.code(output)

        time.sleep(0.3)
