
from execution_engine import ExecutionEngine
from workflow_builder import WorkflowBuilder

from multi_agent_router import MultiAgentRouter
from collab_manager import CollabManager


class OrchestratorV7:

    def __init__(self):

        self.execution_engine = ExecutionEngine()

        self.workflow_builder = WorkflowBuilder()

        self.router = MultiAgentRouter()

        self.collab_manager = CollabManager()

    def run(self, task):

        print("\n==============================")
        print(" SYNERGIA ORCHESTRATOR v7")
        print("==============================")

        print("\n🧠 TASK:")
        print(task)

        agents = self.router.route(task)

        print("\n🤖 AGENTS:")
        print(agents)

        workflow = self.workflow_builder.build(agents)

        print("\n⚙️ WORKFLOW:")
        for step in workflow:
            print(step)

        results = self.execution_engine.execute(
            workflow=workflow,
            task=task
        )

        final_output = self.collab_manager.merge(results)

        print(final_output)

        print("\n==============================")
        print(" ORCHESTRATION COMPLETE v7")
        print("==============================")

        return final_output


if __name__ == "__main__":

    orchestrator = OrchestratorV7()

    orchestrator.run(
        "Crear SaaS IA para restaurantes"
    )
