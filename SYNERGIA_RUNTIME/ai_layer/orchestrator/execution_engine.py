
# =========================================================
# SYNERGIA EXECUTION ENGINE
# =========================================================

import sys
import os

CURRENT_DIR = os.path.dirname(__file__)

AI_LAYER_PATH = os.path.abspath(
    os.path.join(CURRENT_DIR, "..")
)

sys.path.append(AI_LAYER_PATH)

from agents.agent_core import AgentCore


class ExecutionEngine:

    def __init__(self):

        self.agent_core = AgentCore()

    def execute(self, workflow, task):

        results = {}

        print("\n🚀 EXECUTING WORKFLOW...")

        for item in workflow:

            agent = item["agent"]

            print(f"\n⚙️ Running Agent: {agent}")

            output = self.agent_core.run_agent(
                agent,
                task
            )

            results[agent] = output

        return results
