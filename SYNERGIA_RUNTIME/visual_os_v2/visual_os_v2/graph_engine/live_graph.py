import streamlit as st


# =====================================================
# LIVE GRAPH ENGINE
# =====================================================

def render_live_graph(graph_data):

    st.subheader("🎮 LIVE NODE GRAPH ENGINE")

    nodes_html = ""

    node_positions = {

        "business": (50, 10),
        "dev": (20, 65),
        "social_media": (80, 65),
        "cms": (50, 85)
    }

    node_colors = {

        "business": "#00FFAA",
        "dev": "#00CFFF",
        "social_media": "#FF00AA",
        "cms": "#FFB000"
    }

    # =================================================
    # CREATE NODES
    # =================================================

    for node in graph_data:

        x, y = node_positions.get(node, (50, 50))

        color = node_colors.get(node, "#00FFFF")

        nodes_html += f"""

        <div
            class="node"
            style="
                left:{x}%;
                top:{y}%;
                border-color:{color};
                box-shadow:0 0 25px {color};
            "
        >

            ⚡

            <div class="node-title">

                {node.upper()}

            </div>

            <div class="node-status">

                ACTIVE

            </div>

        </div>
        """

    # =================================================
    # HTML
    # =================================================

    html = f"""

    <style>

    .graph-wrapper {{

        position: relative;

        width: 100%;

        height: 700px;

        background:
            radial-gradient(
                circle at center,
                rgba(0,255,255,0.05),
                rgba(0,0,0,0.55)
            );

        border-radius: 20px;

        overflow: hidden;

        border:
            1px solid rgba(255,255,255,0.08);

        box-shadow:
            0 0 30px rgba(0,255,255,0.08);
    }}

    /* ================================================ */
    /* GRID                                              */
    /* ================================================ */

    .graph-wrapper::before {{

        content: "";

        position: absolute;

        width: 100%;

        height: 100%;

        background-image:

            linear-gradient(
                rgba(255,255,255,0.03) 1px,
                transparent 1px
            ),

            linear-gradient(
                90deg,
                rgba(255,255,255,0.03) 1px,
                transparent 1px
            );

        background-size: 40px 40px;
    }}

    /* ================================================ */
    /* CONNECTION LINES                                  */
    /* ================================================ */

    .line {{

        position: absolute;

        height: 4px;

        background:
            linear-gradient(
                90deg,
                rgba(0,255,255,0.1),
                rgba(0,255,255,0.9),
                rgba(0,255,255,0.1)
            );

        box-shadow:
            0 0 18px rgba(0,255,255,0.45);

        animation: flow 2s linear infinite;
    }}

    @keyframes flow {{

        0% {{

            opacity: 0.3;
        }}

        50% {{

            opacity: 1;
        }}

        100% {{

            opacity: 0.3;
        }}
    }}

    /* ================================================ */
    /* NODE                                               */
    /* ================================================ */

    .node {{

        position: absolute;

        width: 170px;

        height: 170px;

        margin-left: -85px;

        margin-top: -85px;

        border-radius: 50%;

        background:
            radial-gradient(
                circle,
                rgba(255,255,255,0.12),
                rgba(0,0,0,0.85)
            );

        border: 2px solid;

        display: flex;

        flex-direction: column;

        justify-content: center;

        align-items: center;

        color: white;

        animation: pulse 2s infinite;

        backdrop-filter: blur(8px);
    }}

    @keyframes pulse {{

        0% {{

            transform: scale(1);
        }}

        50% {{

            transform: scale(1.06);
        }}

        100% {{

            transform: scale(1);
        }}
    }}

    .node-title {{

        margin-top: 10px;

        font-size: 18px;

        font-weight: bold;

        letter-spacing: 1px;
    }}

    .node-status {{

        margin-top: 10px;

        color: #00FFAA;

        font-size: 14px;
    }}

    </style>

    <div class="graph-wrapper">

        <!-- CONNECTIONS -->

        <div
            class="line"
            style="
                width:320px;
                left:28%;
                top:32%;
                transform: rotate(20deg);
            "
        ></div>

        <div
            class="line"
            style="
                width:320px;
                left:44%;
                top:32%;
                transform: rotate(-20deg);
            "
        ></div>

        <div
            class="line"
            style="
                width:250px;
                left:38%;
                top:62%;
                transform: rotate(90deg);
            "
        ></div>

        {nodes_html}

    </div>
    """

    st.markdown(
        html,
        unsafe_allow_html=True
    )
