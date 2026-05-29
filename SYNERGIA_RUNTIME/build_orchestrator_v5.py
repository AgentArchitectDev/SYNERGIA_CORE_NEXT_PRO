# =========================================================
# SYNERGIA ORCHESTRATOR v5 BUILDER
# =========================================================

import os


# =========================================================
# BASE PATH
# =========================================================

BASE_PATH = "/mnt/71392f5d/SYNERGIA_CORE_NEXT_PRO/SYNERGIA_RUNTIME/ai_layer/orchestrator"


# =========================================================
# FILES
# =========================================================

FILES = {

    "context_manager.py": '''
# =========================================================
# SYNERGIA CONTEXT MANAGER
# =========================================================

class ContextManager:

    def __init__(self):

        self.shared_context = {}

    # =====================================================
    # ADD CONTEXT
    # =====================================================

    def add(self, agent, output):

        self.shared_context[agent] = output

    # =====================================================
    # BUILD CONTEXT
    # =====================================================

    def build_context(self):

        context = ""

        for agent, output in self.shared_context.items():

            context += f"\\n\\n=== {agent.upper()} OUTPUT ===\\n"

            context += str(output)

        return context
''',

    "collab_engine.py": '''
# =========================================================
# SYNERGIA COLLAB ENGINE
# =========================================================

class CollabEngine:

    def build_prompt(
        self,
        original_task,
        shared_context
    ):

        final_prompt = f"""
ORIGINAL TASK:

{original_task}

SHARED CONTEXT:

{shared_context}

Continue building the project using all previous context.
"""

        return final_prompt
''',

    "orchestrator_v5.py": '''
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

        print("\\n==============================")
        print(" SYNERGIA ORCHESTRATOR v5")
        print("==============================")

        print("\\n🧠 TASK:")
        print(task)

        memory = self.memory_router.load_context()

        print("\\n📦 MEMORY:")
        print(memory)

        agents = self.decision_engine.analyze(task)

        print("\\n🤖 SELECTED AGENTS:")
        print(agents)

        workflow = self.workflow_builder.build(agents)

        print("\\n⚙️ WORKFLOW:")

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

            print(f"\\n🚀 Running contextual agent: {agent}")

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

        print("\\n==============================")
        print(" ORCHESTRATION COMPLETE v5")
        print("==============================\\n")


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":

    orchestrator = OrchestratorV5()

    orchestrator.run(
        "Crear plataforma IA SaaS para automatizar negocios"
    )
'''
}


# =========================================================
# CREATE FILES
# =========================================================

for filename, content in FILES.items():

    filepath = os.path.join(BASE_PATH, filename)

    with open(filepath, "w", encoding="utf-8") as f:

        f.write(content)

    print(f"✔ Created: {filepath}")


# =========================================================
# FINAL
# =========================================================

print("\\n==============================")
print(" ORCHESTRATOR v5 CREATED")
print("==============================")
