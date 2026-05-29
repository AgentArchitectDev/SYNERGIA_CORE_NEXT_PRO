# =========================================================
# SYNERGIA OS v3
# LIVE BRAIN CANVAS
# =========================================================

import streamlit as st


# =========================================================
# LIVE BRAIN CANVAS
# =========================================================

class LiveBrainCanvas:

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self):

        self.graph = {}

        self.nodes = []

        self.edges = []

        self.events = []

        print("🧠 LIVE BRAIN CANVAS ONLINE")

    # =====================================================
    # LOAD GRAPH
    # =====================================================

    def load_graph(self, graph):

        self.graph = graph

        self.nodes = list(graph.keys())

        self.edges = []

        for node, data in graph.items():

            for connection in data.get(
                "connections",
                []
            ):

                self.edges.append(
                    (
                        node,
                        connection
                    )
                )

    # =====================================================
    # LOAD EVENTS
    # =====================================================

    def load_events(self, events):

        self.events = events

    # =====================================================
    # RENDER
    # =====================================================

    def render(self):

        st.markdown(
            """
            <div style='margin-top:-25px'></div>
            """,
            unsafe_allow_html=True
        )

        st.subheader(
            "🧠 LIVE BRAIN CANVAS"
        )

        html = """

        <style>

        .brain-canvas {

            position: relative;

            width: 100%;

            height: 700px;

            background:
            radial-gradient(
                circle at center,
                #111827,
                #030712
            );

            border-radius: 18px;

            overflow: hidden;

            border:
            1px solid rgba(0,255,200,0.15);
        }

        .brain-node {

            position: absolute;

            width: 170px;

            height: 72px;

            border-radius: 18px;

            background:
            rgba(0,255,200,0.08);

            border:
            1px solid rgba(0,255,200,0.4);

            color: white;

            display: flex;

            align-items: center;

            justify-content: center;

            font-weight: bold;

            backdrop-filter: blur(8px);

            box-shadow:
            0 0 20px rgba(0,255,200,0.15);

            animation:
            pulse 3s infinite;
        }

        @keyframes pulse {

            0% {

                transform: scale(1);

                opacity: 0.9;
            }

            50% {

                transform: scale(1.05);

                opacity: 1;
            }

            100% {

                transform: scale(1);

                opacity: 0.9;
            }
        }

        .brain-line {

            position: absolute;

            height: 2px;

            background:
            rgba(0,255,200,0.35);

            transform-origin:
            left center;
        }

        .event-box {

            position: absolute;

            bottom: 10px;

            left: 10px;

            width: 96%;

            height: 140px;

            overflow-y: auto;

            border-radius: 14px;

            background:
            rgba(0,0,0,0.35);

            border:
            1px solid rgba(0,255,200,0.2);

            padding: 10px;

            color: #00ffd0;

            font-size: 12px;

            font-family: monospace;
        }

        </style>

        <div class="brain-canvas">
        """

        # =================================================
        # NODE POSITIONS
        # =================================================

        positions = {}

        base_x = 100

        base_y = 100

        spacing_x = 260

        spacing_y = 180

        for i, node in enumerate(self.nodes):

            x = base_x + (i * spacing_x)

            y = base_y + ((i % 2) * spacing_y)

            positions[node] = (x, y)

            html += f"""

            <div
                class="brain-node"

                style="
                left:{x}px;
                top:{y}px;
                "
            >

                🧠 {node.upper()}

            </div>

            """

        # =================================================
        # CONNECTIONS
        # =================================================

        for a, b in self.edges:

            if a in positions and b in positions:

                x1, y1 = positions[a]

                x2, y2 = positions[b]

                dx = x2 - x1

                dy = y2 - y1

                length = (
                    dx ** 2 +
                    dy ** 2
                ) ** 0.5

                angle = 0

                if dx != 0:

                    angle = (

                        dy /
                        (dx + 0.0001)

                    ) * 57

                html += f"""

                <div
                    class="brain-line"

                    style="
                        width:{length}px;
                        left:{x1 + 80}px;
                        top:{y1 + 35}px;
                        transform:
                        rotate({angle}deg);
                    "
                ></div>

                """

        # =================================================
        # EVENTS
        # =================================================

        html += """

        <div class="event-box">

        <b>📡 LIVE EVENTS</b><br><br>

        """

        for event in self.events[-12:]:

            html += f"""

            ➜ [{event.get('type', 'EVENT')}]
            {event.get('sender', 'SYSTEM')}
            →
            {event.get('target', 'ALL')}

            <br>

            """

        html += """

        </div>

        """

        html += "</div>"

        st.components.v1.html(
            html,
            height=760
        )
