import streamlit as st
import time
import uuid

class LiveBrainCanvas:

    def __init__(self):
        self.nodes = []
        self.state = {}

    # =====================================================
    # LOAD RUNTIME
    # =====================================================

    def load_runtime(self, runtime: dict):

        self.nodes = runtime.get("agents", [])

        self.state = {
            "task": runtime.get("task"),
            "models": runtime.get("models", []),
            "memory": runtime.get("memory"),
            "ollama": runtime.get("ollama_outputs", [])
        }

    # =====================================================
    # VISUAL RENDER
    # =====================================================

    def render(self):

        st.subheader("🧠 LIVE BRAIN CANVAS")

        html = """
        <style>

        .brain {
            position: relative;
            width: 100%;
            height: 600px;
            background: radial-gradient(circle, #0b0f1a, #05070d);
            border-radius: 16px;
            overflow: hidden;
        }

        .node {
            position: absolute;
            width: 140px;
            height: 70px;
            border-radius: 14px;
            background: rgba(0,255,200,0.12);
            border: 1px solid rgba(0,255,200,0.5);
            color: white;
            text-align: center;
            font-weight: bold;
            padding-top: 20px;
            box-shadow: 0 0 20px rgba(0,255,200,0.25);
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); opacity: 0.8; }
            50% { transform: scale(1.05); opacity: 1; }
            100% { transform: scale(1); opacity: 0.8; }
        }

        .task {
            position: absolute;
            top: 20px;
            left: 20px;
            color: #00ffc8;
            font-size: 14px;
        }

        </style>

        <div class="brain">

        <div class="task">
            ⚡ TASK: %s
        </div>
        """ % self.state.get("task", "NO TASK")

        # =================================================
        # NODES POSITIONING
        # =================================================

        positions = [(120, 120), (420, 180), (720, 120)]

        for i, node in enumerate(self.nodes):

            x, y = positions[i % len(positions)]

            html += f"""
            <div class="node" style="left:{x}px;top:{y}px;">
                🧠 {node.upper()}
            </div>
            """

        # =================================================
        # MEMORY NODE
        # =================================================

        html += f"""
        <div class="node" style="left:420px;top:380px;background:rgba(0,120,255,0.15);">
            💾 MEMORY
        </div>
        """

        # =================================================
        # OUTPUT NODE
        # =================================================

        html += f"""
        <div class="node" style="left:720px;top:380px;background:rgba(255,0,200,0.12);">
            📦 OUTPUT
        </div>
        """

        html += "</div>"

        st.components.v1.html(html, height=650)
