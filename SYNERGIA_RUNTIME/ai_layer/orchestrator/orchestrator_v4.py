
# =========================================================
# SYNERGIA ORCHESTRATOR v4
# =========================================================

from decision_engine import DecisionEngine
from workflow_builder import WorkflowBuilder
from execution_engine import ExecutionEngine
from result_merger import ResultMerger
from memory_router import MemoryRouter


class OrchestratorV4:

    def __init__(self):

        self.decision_engine = DecisionEngine()

        self.workflow_builder = WorkflowBuilder()

        self.execution_engine = ExecutionEngine()

        self.result_merger = ResultMerger()

        self.memory_router = MemoryRouter()

    def run(self, task):

        print("\n==============================")
        print(" SYNERGIA ORCHESTRATOR v4")
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

            print(
                f'STEP {item["step"]} '
                f'→ {item["agent"]}'
            )

        results = self.execution_engine.execute(
            workflow,
            task
        )

        final_output = self.result_merger.merge(
            results
        )

        print(final_output)

        print("\n==============================")
        print(" ORCHESTRATION COMPLETE v4")
        print("==============================\n")


if __name__ == "__main__":

    orchestrator = OrchestratorV4()

    orchestrator.run(
        "Crear SaaS IA para restaurantes"
    )
