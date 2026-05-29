
# =========================================================
# SYNERGIA ORCHESTRATOR v3
# =========================================================

from decision_engine import DecisionEngine
from workflow_builder import WorkflowBuilder
from agent_registry import AgentRegistry
from memory_router import MemoryRouter


class OrchestratorV3:

    def __init__(self):

        self.decision_engine = DecisionEngine()
        self.workflow_builder = WorkflowBuilder()
        self.agent_registry = AgentRegistry()
        self.memory_router = MemoryRouter()

    def run(self, task):

        print("\n==============================")
        print(" SYNERGIA ORCHESTRATOR v3")
        print("==============================")

        print("\n🧠 TASK:")
        print(task)

        memory = self.memory_router.load_context()

        print("\n📦 MEMORY:")
        print(memory)

        agents = self.decision_engine.analyze(task)

        print("\n🤖 SELECTED AGENTS:")
        print(agents)

        workflow = self.workflow_builder.build(agents)

        print("\n⚙️ WORKFLOW:")

        for item in workflow:

            agent_name = self.agent_registry.get_agent(
                item["agent"]
            )

            print(
                f'STEP {item["step"]} '
                f'→ {item["agent"]} '
                f'({agent_name})'
            )

        print("\n==============================")
        print(" ORCHESTRATION COMPLETE")
        print("==============================\n")


if __name__ == "__main__":

    orchestrator = OrchestratorV3()

    orchestrator.run(
        "Crear SaaS IA con backend, landing y marketing"
    )
