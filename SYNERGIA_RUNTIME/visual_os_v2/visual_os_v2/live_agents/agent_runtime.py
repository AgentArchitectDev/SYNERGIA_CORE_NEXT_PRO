import time
import streamlit as st


# =====================================================
# LIVE AGENT EXECUTION
# =====================================================

def render_live_agents(runtime):

    st.subheader("🤖 LIVE AGENT EXECUTION")

    terminal = st.empty()

    logs = []

    # =================================================
    # BUSINESS
    # =================================================

    if "business" in runtime["agents"]:

        logs.append(
            "[BUSINESS AI] analyzing business model..."
        )

        terminal.code("\n".join(logs))

        time.sleep(0.7)

        logs.append(
            "[BUSINESS AI] generating monetization..."
        )

        terminal.code("\n".join(logs))

        time.sleep(0.7)

    # =================================================
    # DEV
    # =================================================

    if "dev" in runtime["agents"]:

        logs.append(
            "[DEV AI] building backend architecture..."
        )

        terminal.code("\n".join(logs))

        time.sleep(0.7)

        logs.append(
            "[DEV AI] preparing API structure..."
        )

        terminal.code("\n".join(logs))

        time.sleep(0.7)

    # =================================================
    # SOCIAL
    # =================================================

    if "social_media" in runtime["agents"]:

        logs.append(
            "[SOCIAL AI] generating content strategy..."
        )

        terminal.code("\n".join(logs))

        time.sleep(0.7)

        logs.append(
            "[SOCIAL AI] optimizing TikTok automation..."
        )

        terminal.code("\n".join(logs))

        time.sleep(0.7)

    # =================================================
    # MEMORY
    # =================================================

    logs.append(
        "[MEMORY ENGINE] saving cognitive experience..."
    )

    terminal.code("\n".join(logs))

    time.sleep(0.7)

    logs.append(
        "[SYNERGIA CORE] execution complete."
    )

    terminal.code("\n".join(logs))
