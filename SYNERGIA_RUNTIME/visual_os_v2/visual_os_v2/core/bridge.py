# =========================================================
# SYNERGIA OS v3
# LIVE COGNITIVE BRIDGE
# FULL STABLE VERSION
# =========================================================

import sys

from pathlib import Path

from datetime import datetime


# =========================================================
# ROOT FIX
# =========================================================

ROOT_DIR = Path(__file__).resolve().parents[4]

sys.path.append(str(ROOT_DIR))


# =========================================================
# IMPORTS
# =========================================================

from SYNERGIA_RUNTIME.core.runtime.live_agent_bus import LiveAgentBus

from graph_engine.live_graph import LiveGraphEngine

from ollama_engine.ollama_runtime import OllamaRuntime

from memory.memory_engine import MemoryEngine

from modes.node_mapper import NodeMapper

from runtime.visual_engine import VisualEngine


# =========================================================
# BRIDGE
# =========================================================

class SynergiaBridge:

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self):

        print()
        print("🚀 INITIALIZING SYNERGIA BRIDGE")
        print()

        self.mapper = NodeMapper()

        self.visual = VisualEngine()

        self.graph_engine = LiveGraphEngine()

        self.ollama = OllamaRuntime()

        self.memory = MemoryEngine()

        self.bus = LiveAgentBus()

        print("🧠 NODE MAPPER ONLINE")
        print("🎮 VISUAL ENGINE ONLINE")
        print("🌐 LIVE GRAPH ONLINE")
        print("🤖 OLLAMA RUNTIME ONLINE")
        print("💾 MEMORY ENGINE ONLINE")
        print("📡 LIVE AGENT BUS ONLINE")

        print()
        print("✅ SYNERGIA BRIDGE READY")
        print()

    # =====================================================
    # MODEL ROUTER
    # =====================================================

    def route_model(self, agent):

        if agent == "dev":

            return "qwen2.5-coder:7b"

        elif agent == "business":

            return "llama3"

        elif agent == "social_media":

            return "mistral"

        elif agent == "cms":

            return "phi3"

        return "phi3"

    # =====================================================
    # RUN
    # =====================================================

    def run(
        self,
        task,
        mode="AUTONOMOUS"
    ):

        print()
        print("=================================================")
        print("🧠 SYNERGIA EXECUTION STARTED")
        print("=================================================")

        print()
        print(f"📌 TASK: {task}")
        print(f"⚙️ MODE: {mode}")
        print()

        # =================================================
        # NODE DETECTION
        # =================================================

        print("🧠 DETECTING NODES...")

        nodes = self.mapper.detect_nodes(task)

        print(f"✅ NODES DETECTED: {nodes}")

        agents = nodes

        # =================================================
        # REGISTER AGENTS
        # =================================================

        print()
        print("📡 REGISTERING AGENTS")

        for agent in agents:

            self.bus.register(agent)

            print(f"✅ REGISTERED: {agent}")

        # =================================================
        # BUILD GRAPH
        # =================================================

        print()
        print("🌐 BUILDING GRAPH")

        graph = self.graph_engine.build_graph(nodes)

        print("✅ GRAPH CREATED")

        # =================================================
        # VISUAL ENGINE
        # =================================================

        print()
        print("🎮 EXECUTING VISUAL ENGINE")

        engine_output = self.visual.execute(

            nodes=nodes,

            mode=mode
        )

        print("✅ VISUAL ENGINE COMPLETE")

        # =================================================
        # OLLAMA EXECUTION
        # =================================================

        print()
        print("🤖 STARTING AI EXECUTION")

        ollama_outputs = []

        # =================================================
        # EXECUTE AGENTS
        # =================================================

        for agent in agents:

            print()
            print("-------------------------------------------------")

            model = self.route_model(agent)

            print(f"🧠 AGENT: {agent}")
            print(f"🤖 MODEL: {model}")

            # =============================================
            # TASK EVENT
            # =============================================

            self.bus.send_event(

                sender="SYSTEM",

                target=agent,

                event_type="TASK",

                content=task
            )

            # =============================================
            # PROMPT
            # =============================================

            prompt = f"""
            You are the {agent} AI agent inside SYNERGIA OS.

            TASK:
            {task}

            Return professional structured output.
            """

            # =============================================
            # OLLAMA EXECUTION
            # =============================================

            response = self.ollama.generate(

                model=model,

                prompt=prompt
            )

            # =============================================
            # STORE OUTPUT
            # =============================================

            ollama_outputs.append({

                "agent": agent,

                "model": model,

                "response": response
            })

            # =============================================
            # RESPONSE EVENT
            # =============================================

            self.bus.send_event(

                sender=agent,

                target="SYSTEM",

                event_type="RESPONSE",

                content=response[:250]
            )

            print(f"✅ RESPONSE GENERATED: {agent}")

        # =================================================
        # MEMORY SAVE
        # =================================================

        print()
        print("💾 SAVING MEMORY")

        memory_data = {

            "task": task,

            "mode": mode,

            "nodes": nodes,

            "graph": graph,

            "events": self.bus.get_all_events(),

            "outputs": ollama_outputs,

            "timestamp": str(datetime.now())
        }

        memory_file = self.memory.save_experience(

            memory_data
        )

        print(f"✅ MEMORY SAVED: {memory_file}")

        # =================================================
        # RUNTIME STATUS
        # =================================================

        runtime = {

            "task": task,

            "mode": mode,

            "runtime": "ONLINE",

            "memory": "CONNECTED",

            "ollama": "CONNECTED",

            "agents": agents,

            "models": [

                "llama3",

                "qwen2.5-coder:7b",

                "mistral",

                "phi3"
            ],

            "ollama_outputs": ollama_outputs
        }

        # =================================================
        # FINAL OUTPUT
        # =================================================

        final_output = {

            "status": "SUCCESS",

            "task": task,

            "mode": mode,

            "nodes": nodes,

            "graph": graph,

            "events": self.bus.get_all_events(),

            "runtime": runtime,

            "engine_output": engine_output,

            "memory_file": memory_file,

            "timestamp": str(datetime.now())
        }

        print()
        print("=================================================")
        print("✅ SYNERGIA EXECUTION COMPLETE")
        print("=================================================")
        print()

        return final_output
