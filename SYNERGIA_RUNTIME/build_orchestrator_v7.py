from pathlib import Path


BASE = Path(
    "/mnt/71392f5d/SYNERGIA_CORE_NEXT_PRO/"
    "SYNERGIA_RUNTIME/ai_layer/orchestrator"
)


files = {

    "multi_agent_router.py": '''
class MultiAgentRouter:

    def route(self, task):

        task = task.lower()

        agents = []

        if "saas" in task:
            agents.extend([
                "business",
                "dev",
                "cms",
                "social"
            ])

        elif "backend" in task:
            agents.append("dev")

        elif "landing" in task:
            agents.append("cms")

        elif "marketing" in task:
            agents.append("social")

        else:
            agents.append("business")

        return agents
''',

    "collab_manager.py": '''
class CollabManager:

    def merge(self, results):

        final = "\\n==============================\\n"
        final += " SYNERGIA COLLAB OUTPUT\\n"
        final += "==============================\\n"

        for agent, output in results.items():

            final += f"\\n\\n--- {agent.upper()} ---\\n\\n"
            final += str(output)

        return final
''',

    "orchestrator_v7.py": '''
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

        print("\\n==============================")
        print(" SYNERGIA ORCHESTRATOR v7")
        print("==============================")

        print("\\n🧠 TASK:")
        print(task)

        agents = self.router.route(task)

        print("\\n🤖 AGENTS:")
        print(agents)

        workflow = self.workflow_builder.build(agents)

        print("\\n⚙️ WORKFLOW:")
        for step in workflow:
            print(step)

        results = self.execution_engine.execute(
            workflow=workflow,
            task=task
        )

        final_output = self.collab_manager.merge(results)

        print(final_output)

        print("\\n==============================")
        print(" ORCHESTRATION COMPLETE v7")
        print("==============================")

        return final_output


if __name__ == "__main__":

    orchestrator = OrchestratorV7()

    orchestrator.run(
        "Crear SaaS IA para restaurantes"
    )
'''
}


for filename, content in files.items():

    path = BASE / filename

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✔ Created: {path}")


print("\\n==============================")
print(" ORCHESTRATOR v7 CREATED")
print("==============================")
