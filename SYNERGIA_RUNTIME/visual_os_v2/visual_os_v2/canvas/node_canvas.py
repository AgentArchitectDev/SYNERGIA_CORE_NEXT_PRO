# =========================================================
# SYNERGIA OS v2
# VISUAL NODE CANVAS v1
# Cognitive Graph Renderer (Streamlit + HTML)
# =========================================================

import streamlit as st
import uuid


# =========================================================
# NODE CANVAS ENGINE
# =========================================================

class NodeCanvasV1:

    def __init__(self):

        self.nodes = []
        self.edges = []

        print("🎮 NODE CANVAS v1 INITIALIZED")

    # =====================================================
    # LOAD GRAPH
    # =====================================================

    def load_graph(self, graph: dict):

        self.nodes = list(graph.keys())

        self.edges = []

        for node, data in graph.items():

            for conn in data.get("connections", []):

                self.edges.append((node, conn))

    # =====================================================
    # RENDER CANVAS
    # =====================================================

    def render(self):

        st.subheader("🧠 VISUAL NODE CANVAS v1")

        # container
        html = """
        <style>
        .canvas {
            position: relative;
            width: 100%;
            height: 500px;
            background: radial-gradient(circle, #0b0f1a, #05070d);
            border-radius: 12px;
            overflow: hidden;
        }

        .node {
            position: absolute;
            width: 120px;
            height: 60px;
            border-radius: 12px;
            background: rgba(0,255,200,0.12);
            border: 1px solid rgba(0,255,200,0.5);
            color: white;
            text-align: center;
            line-height: 60px;
            font-weight: bold;
            box-shadow: 0 0 20px rgba(0,255,200,0.2);
        }

        .line {
            position: absolute;
            height: 2px;
            background: rgba(0,255,200,0.4);
            transform-origin: left center;
        }
        </style>

        <div class="canvas">
        """

        # simple layout positions
        positions = {}
        x = 80
        y = 80

        for i, node in enumerate(self.nodes):

            positions[node] = (x + (i * 160), y + ((i % 2) * 120))

            html += f"""
            <div class="node" style="left:{positions[node][0]}px;top:{positions[node][1]}px;">
                {node.upper()}
            </div>
            """

        # edges
        for a, b in self.edges:

            if a in positions and b in positions:

                x1, y1 = positions[a]
                x2, y2 = positions[b]

                dx = x2 - x1
                dy = y2 - y1
                length = (dx ** 2 + dy ** 2) ** 0.5
                angle = 0 if dx == 0 else (dy / (dx + 0.0001)) * 57

                html += f"""
                <div class="line"
                    style="
                        width:{length}px;
                        left:{x1}px;
                        top:{y1}px;
                        transform: rotate({angle}deg);
                    ">
                </div>
                """

        html += "</div>"

        st.components.v1.html(html, height=520)


# =========================================================
# TEST LOCAL
# =========================================================

if __name__ == "__main__":

    canvas = NodeCanvasV1()

    sample_graph = {

        "business": {"connections": ["dev", "social_media"]},
        "dev": {"connections": ["business"]},
        "social_media": {"connections": ["business"]}
    }

    canvas.load_graph(sample_graph)
    canvas.render()

