
# =========================================================
# SYNERGIA ORCHESTRATOR v5
# =========================================================

from decision_engine import DecisionEngine
from workflow_builder import WorkflowBuilder
from execution_engine import ExecutionEngine
from result_merger import ResultMerger
from memory_router import MemoryRouter

from context_manager import ContextManager
from collab_engine import CollabEngine


class OrchestratorV5:

    def __init__(self):

        self.decision_engine = DecisionEngine()

        self.workflow_builder = WorkflowBuilder()

        self.execution_engine = ExecutionEngine()

        self.result_merger = ResultMerger()

        self.memory_router = MemoryRouter()

        self.context_manager = ContextManager()

        self.collab_engine = CollabEngine()

    # =====================================================
    # RUN
    # =====================================================

    def run(self, task):

        print("\n==============================")
        print(" SYNERGIA ORCHESTRATOR v5")
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

        results = {}

        # =================================================
        # CONTEXTUAL EXECUTION
        # =================================================

        for item in workflow:

            agent = item["agent"]

            print(f"\n🚀 Running contextual agent: {agent}")

            shared_context = (
                self.context_manager.build_context()
            )

            prompt = self.collab_engine.build_prompt(
                task,
                shared_context
            )

            output = self.execution_engine.agent_core.run_agent(
                agent,
                prompt
            )

            results[agent] = output

            self.context_manager.add(
                agent,
                output
            )

        # =================================================
        # FINAL OUTPUT
        # =================================================

        final_output = self.result_merger.merge(
            results
        )

        print(final_output)

        print("\n==============================")
        print(" ORCHESTRATION COMPLETE v5")
        print("==============================\n")


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":

    orchestrator = OrchestratorV5()

    orchestrator.run(
        "Crear plataforma IA SaaS para automatizar negocios"
    )
