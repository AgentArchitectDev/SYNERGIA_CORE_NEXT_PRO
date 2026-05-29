# ============================================
# SYNERGIA BOOT LOADER v1 - FIXED VERSION
# ============================================

from ai_layer.orchestrator.cognitive_task_router import CognitiveTaskRouter
from ai_layer.orchestrator.agent_debate_engine import AgentDebateEngine
from ai_layer.memory.experience_engine import ExperienceEngine
from builder_engine.autonomous_builder import build_project


class SynergiaBoot:

    # ========================================
    # INIT SYSTEM
    # ========================================
    def __init__(self):

        print("\n==============================")
        print("🚀 SYNERGIA BOOT LOADER v1")
        print("==============================\n")

        self.router = CognitiveTaskRouter()
        self.debate = AgentDebateEngine()
        self.memory = ExperienceEngine()

    # ========================================
    # START SYSTEM
    # ========================================
    def start(self, task):

        print("🧠 TASK RECEIVED:", task)

        # 1. ROUTER
        analysis = self.router.analyze_task(task)
        agents = self.router.select_agents(analysis)

        print("\n🤖 AGENTS SELECTED:")
        print(agents)

        # 2. DEBATE ENGINE
        opinions = self.debate.generate_opinions(task)
        self.debate.analyze_opinions(opinions)

        # 3. MEMORY (FIX IMPORTANTE)
        self.memory.add_experience(
            task=task,
            result="BOOT EXECUTION COMPLETED"
        )

        # 4. BUILDER
        build_project(task)

        print("\n==============================")
        print("✅ BOOT EXECUTION FINISHED")
        print("==============================\n")


# ============================================
# MAIN ENTRY POINT
# ============================================

if __name__ == "__main__":

    system = SynergiaBoot()

    task = input("🧠 Task: ")

    system.start(task)
