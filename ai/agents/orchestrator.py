"""
============================================================
SYNERGIA AGENT ORCHESTRATOR (INSTRUMENTED)
Metrics + Performance Tracking Layer
============================================================
"""

import time

from ai.agents.agent_registry import agent_registry
from ai.agents.agent_metrics import agent_metrics


class AgentOrchestrator:

    def __init__(self):

        self.last_execution = []
        self.last_plan = None

    # -------------------------------------------------
    # MAIN DISPATCH
    # -------------------------------------------------

    def dispatch(self, plan, input_text, context=None):

        if not plan:
            plan = ["research"]

        if isinstance(plan, str):
            plan = [plan]

        self.last_plan = plan

        results = []

        for task in plan:

            agent = agent_registry.get(task)

            # -------------------------------------------------
            # MISSING AGENT
            # -------------------------------------------------

            if not agent:

                results.append({
                    "agent": task,
                    "status": "missing",
                    "input": input_text
                })

                continue

            # -------------------------------------------------
            # EXECUTION + METRICS
            # -------------------------------------------------

            start_time = time.time()

            try:

                if hasattr(agent, "safe_run"):
                    result = agent.safe_run(input_text, context)
                else:
                    result = agent.run(input_text, context)

                latency = time.time() - start_time

                success = result.get("status") != "error"

                # 📊 RECORD METRICS
                agent_metrics.record(task, success, latency)

                results.append({
                    "agent": task,
                    "status": "executed",
                    "latency": latency,
                    "result": result
                })

            except Exception as e:

                latency = time.time() - start_time

                agent_metrics.record(task, False, latency)

                results.append({
                    "agent": task,
                    "status": "error",
                    "error": str(e),
                    "latency": latency
                })

        self.last_execution = results

        return results

    # -------------------------------------------------

    def get_state(self):

        return {
            "last_plan": self.last_plan,
            "last_execution": self.last_execution,
            "registered_agents": list(agent_registry.keys())
        }

    # -------------------------------------------------

    def reset(self):

        self.last_execution = []
        self.last_plan = None

        return {"status": "reset"}


agent_orchestrator = AgentOrchestrator()
