import threading
import time
from agents.agent_core import AgentCore


class AgentCollabV2:

    def __init__(self):

        self.core = AgentCore()
        self.results = {}
        self.lock = threading.Lock()

    # =========================
    # AGENTE EJECUTOR
    # =========================
    def run_agent(self, name, agent_type, task):

        print(f"\n🚀 Starting {name} agent...")

        try:
            result = self.core.run(agent_type, task)

            with self.lock:
                self.results[name] = result

            print(f"\n✔ [{name.upper()}] finished")

            print(f"\n--- OUTPUT {name.upper()} ---\n")
            print(result)

        except Exception as e:

            with self.lock:
                self.results[name] = f"ERROR: {str(e)}"

            print(f"\n❌ [{name.upper()}] ERROR: {e}")

    # =========================
    # PROJECT RUN (PARALLEL)
    # =========================
    def run_project(self, idea):

        print("\n🤝 SYNERGIA COLLAB v2 (PARALLEL MODE)")
        print("Project:", idea)

        # =========================
        # SHARED CONTEXT TASKS
        # =========================
        business_task = f"Define SaaS completo: {idea}"
        cms_task = f"Crea landing page profesional: {idea}"
        dev_task = f"Crea arquitectura técnica backend: {idea}"
        social_task = f"Crea estrategia marketing completa: {idea}"

        # =========================
        # THREADS
        # =========================
        threads = [
            threading.Thread(target=self.run_agent, args=("business", "business", business_task)),
            threading.Thread(target=self.run_agent, args=("cms", "cms", cms_task)),
            threading.Thread(target=self.run_agent, args=("dev", "dev", dev_task)),
            threading.Thread(target=self.run_agent, args=("social", "social", social_task)),
        ]

        # START
        for t in threads:
            t.start()

        # WAIT
        for t in threads:
            t.join()

        print("\n==============================")
        print(" COLLAB v2 COMPLETE")
        print("==============================\n")

        return {
            "idea": idea,
            "business": self.results.get("business"),
            "cms": self.results.get("cms"),
            "dev": self.results.get("dev"),
            "social": self.results.get("social"),
        }
