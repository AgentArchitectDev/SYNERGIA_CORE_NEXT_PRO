
# =========================================================
# SYNERGIA WORKFLOW BUILDER
# =========================================================

class WorkflowBuilder:

    def build(self, agents):

        workflow = []

        priority = {
            "business": 1,
            "dev": 2,
            "cms": 3,
            "social": 4
        }

        ordered = sorted(
            agents,
            key=lambda x: priority.get(x, 999)
        )

        for step, agent in enumerate(ordered, start=1):

            workflow.append({
                "step": step,
                "agent": agent
            })

        return workflow
