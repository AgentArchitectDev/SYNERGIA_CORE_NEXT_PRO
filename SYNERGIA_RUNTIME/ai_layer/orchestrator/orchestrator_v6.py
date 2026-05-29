
from execution_engine import ExecutionEngine
from workflow_builder import WorkflowBuilder

from experience_engine import ExperienceEngine
from project_memory import ProjectMemory
from task_classifier import TaskClassifier
from agent_router import AgentRouter
from learning_engine import LearningEngine


class OrchestratorV6:

    def __init__(self):

        self.execution_engine = ExecutionEngine()

        self.workflow_builder = WorkflowBuilder()

        self.experience_engine = ExperienceEngine()

        self.project_memory = ProjectMemory()

        self.task_classifier = TaskClassifier()

        self.agent_router = AgentRouter()

        self.learning_engine = LearningEngine()

    def run(self, task):

        print("\n==============================")
        print(" SYNERGIA ORCHESTRATOR v6")
        print("==============================")

        print("\n🧠 TASK:")
        print(task)

        category = self.task_classifier.classify(task)

        print("\n📂 CATEGORY:")
        print(category)

        agents = self.agent_router.route(category)

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

        self.project_memory.save_project(
            task,
            results
        )

        self.experience_engine.add_experience(
            task,
            results
        )

        self.learning_engine.analyze_patterns(task)

        print("\n==============================")
        print(" FINAL OUTPUT v6")
        print("==============================")

        print(results)

        return results


if __name__ == "__main__":

    orchestrator = OrchestratorV6()

    orchestrator.run(
        "Crear backend IA para automatización"
    )
