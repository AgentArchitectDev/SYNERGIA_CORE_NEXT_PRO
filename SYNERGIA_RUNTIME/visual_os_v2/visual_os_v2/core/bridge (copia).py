# =========================================================
# SYNERGIA OS v2
# CORE BRIDGE (STABLE VERSION)
# =========================================================

import json
import os
from datetime import datetime

from core.node_mapper import NodeMapper
from core.visual_engine import VisualEngine
from ollama_engine.ollama_runtime import OllamaRuntime


# =========================================================
# BRIDGE CORE
# =========================================================

class SynergiaBridge:

    def __init__(self):

        print("\n🚀 INITIALIZING SYNERGIA BRIDGE")

        self.mapper = NodeMapper()
        self.visual = VisualEngine()
        self.ollama = OllamaRuntime()

        print("⚡ VISUAL ENGINE ONLINE")
        print("✅ BRIDGE READY")

    # =====================================================
    # MEMORY SYSTEM
    # =====================================================

    def save_memory(self, data):

        print("\n💾 SAVING EXPERIENCE")

        memory_dir = "memory/experiences"
        os.makedirs(memory_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        safe_name = data["task"].replace(" ", "_").lower()

        filepath = os.path.join(
            memory_dir,
            f"{safe_name}_{timestamp}.json"
        )

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"\n💾 MEMORY SAVED:\n{filepath}")

        return filepath

    # =====================================================
    # GRAPH ENGINE
    # =====================================================

    def build_graph(self, nodes):

        print("\n🎮 BUILDING NODE GRAPH")

        connections = {

            "business": ["dev", "social_media", "cms"],
            "dev": ["business", "cms"],
            "social_media": ["business"],
            "cms": ["business", "social_media"]
        }

        graph = {}

        for node in nodes:

            graph[node] = {

                "status": "ACTIVE",
                "connections": connections.get(node, [])
            }

        print("✅ GRAPH GENERATED")

        return graph

    # =====================================================
    # MAIN RUN
    # =====================================================

    def run(self, task, mode="AUTONOMOUS"):

        print("\n🧠 SYNERGIA ENGINE ACTIVE")
        print(f"📌 TASK: {task}")
        print(f"⚙️ MODE: {mode}")

        # -----------------------------
        # NODE DETECTION
        # -----------------------------

        nodes = self.mapper.detect_nodes(task)

        print("\n🧩 NODES GENERATED:")
        for n in nodes:
            print(f"   ├── {n}")

        print("\n🤖 ACTIVE AGENTS:")
        for n in nodes:
            print(f"   ├── {n}")

        # -----------------------------
        # RUNTIME STATE (FIXED)
        # -----------------------------

        runtime = {

            "task": task,
            "mode": mode,
            "agents": nodes,

            "status": "RUNNING",
            "runtime": "ONLINE",

            "memory": "CONNECTED",
            "ollama": "CONNECTED",

            "models": [
                "llama3",
                "qwen2.5-coder",
                "mistral",
                "phi3"
            ],

            "ollama_outputs": []
        }

        # -----------------------------
        # VISUAL ENGINE
        # -----------------------------

        print("\n⚡ STARTING VISUAL ENGINE")

        engine_output = self.visual.execute(
            task=task,
            mode=mode,
            nodes=nodes
        )

        print("⚡ VISUAL ENGINE RUNNING")
        print("✅ ENGINE EXECUTED")

        # -----------------------------
        # GRAPH
        # -----------------------------

        graph = self.build_graph(nodes)

        # -----------------------------
        # OLLAMA AGENTS
        # -----------------------------

        print("\n🤖 STARTING OLLAMA AGENTS")

        for agent in nodes:

            result = self.ollama.run_agent(
                agent=agent,
                task=task
            )

            runtime["ollama_outputs"].append(result)

            print(f"🧠 {agent.upper()} → {result['model']}")

        print("\n✅ OLLAMA EXECUTION COMPLETE")

        # -----------------------------
        # FINAL OUTPUT
        # -----------------------------

        final_output = {

            "status": "SUCCESS",
            "task": task,
            "mode": mode,

            "runtime": runtime,

            "nodes": nodes,
            "graph": graph,

            "engine_output": engine_output,

            "timestamp": datetime.now().isoformat()
        }

        # -----------------------------
        # SAVE MEMORY
        # -----------------------------

        memory_file = self.save_memory(final_output)
        final_output["memory_file"] = memory_file

        print("\n📦 GENERATING FINAL OUTPUT")
        print("✅ SYNERGIA EXECUTION COMPLETE")

        return final_output
