from pathlib import Path


BASE = Path(
    "/mnt/71392f5d/SYNERGIA_CORE_NEXT_PRO/"
    "SYNERGIA_RUNTIME/ai_layer/orchestrator"
)


files = {

    "experience_engine.py": '''
class ExperienceEngine:

    def __init__(self):

        self.experiences = []

    def add_experience(self, task, result):

        self.experiences.append({
            "task": task,
            "result": result
        })

    def get_experiences(self):

        return self.experiences
''',

    "project_memory.py": '''
class ProjectMemory:

    def __init__(self):

        self.projects = []

    def save_project(self, name, data):

        self.projects.append({
            "name": name,
            "data": data
        })

    def get_projects(self):

        return self.projects
''',

    "task_classifier.py": '''
class TaskClassifier:

    def classify(self, task):

        task = task.lower()

        if "backend" in task:
            return "dev"

        if "landing" in task:
            return "cms"

        if "marketing" in task:
            return "social"

        return "business"
''',

    "agent_router.py": '''
class AgentRouter:

    def route(self, category):

        mapping = {
            "business": ["business"],
            "dev": ["dev"],
            "cms": ["cms"],
            "social": ["social"]
        }

        return mapping.get(category, ["business"])
''',

    "learning_engine.py": '''
class LearningEngine:

    def analyze_patterns(self, task):

        print("\\n🧠 Learning from task:")
        print(task)
''',

    "orchestrator_v6.py": '''
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

        print("\\n==============================")
        print(" SYNERGIA ORCHESTRATOR v6")
        print("==============================")

        print("\\n🧠 TASK:")
        print(task)

        category = self.task_classifier.classify(task)

        print("\\n📂 CATEGORY:")
        print(category)

        agents = self.agent_router.route(category)

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

        self.project_memory.save_project(
            task,
            results
        )

        self.experience_engine.add_experience(
            task,
            results
        )

        self.learning_engine.analyze_patterns(task)

        print("\\n==============================")
        print(" FINAL OUTPUT v6")
        print("==============================")

        print(results)

        return results


if __name__ == "__main__":

    orchestrator = OrchestratorV6()

    orchestrator.run(
        "Crear backend IA para automatización"
    )
'''
}


for filename, content in files.items():

    path = BASE / filename

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✔ Created: {path}")


print("\\n==============================")
print(" ORCHESTRATOR v6 CREATED")
print("==============================")
