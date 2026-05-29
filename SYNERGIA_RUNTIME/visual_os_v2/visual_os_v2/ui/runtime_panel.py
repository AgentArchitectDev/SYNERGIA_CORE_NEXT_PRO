import streamlit as st


# =====================================================
# RUNTIME PANEL
# =====================================================

def render_runtime(runtime_data):

    st.subheader("🤖 ACTIVE AGENTS")

    agents = runtime_data["agents"]

    st.metric(
        "Agents Running",
        len(agents)
    )

    for agent in agents:

        st.success(
            f"{agent} → ACTIVE"
        )


# =====================================================
# MODELS
# =====================================================

def render_models(runtime_data):

    st.subheader("🧠 ACTIVE AI MODELS")

    models = runtime_data["models"]

    for model in models:

        st.info(model)
