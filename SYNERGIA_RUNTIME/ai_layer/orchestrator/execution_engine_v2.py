# ============================================
# SYNERGIA AUTONOMOUS EXECUTION ENGINE v2
# ============================================

from builder_engine.autonomous_builder import build_project
from cognitive_task_router import CognitiveTaskRouter
from agent_debate_engine import AgentDebateEngine
from self_correction_engine import SelfCorrectionEngine


class AutonomousExecutionEngine:


    # ========================================
    # INIT
    # ========================================

    def __init__(self):

        self.router = CognitiveTaskRouter()
        self.debate = AgentDebateEngine()
        self.correction = SelfCorrectionEngine()


    # ========================================
    # RUN PIPELINE
    # ========================================

    def run(self, task):

        print("\n==============================")
        print(" SYNERGIA EXECUTION ENGINE v2")
        print("==============================\n")

        # ------------------------------------
        # 1. ANALYZE TASK
        # ------------------------------------

        analysis = self.router.analyze_task(task)

        agents = self.router.select_agents(analysis)

        workflow = self.router.create_workflow(agents)

        print("🧠 ANALYSIS:", analysis)
        print("🤖 AGENTS:", agents)

        # ------------------------------------
        # 2. DEBATE PHASE
        # ------------------------------------

        opinions = self.debate.generate_opinions(task)

        self.debate.analyze_opinions(opinions)

        # ------------------------------------
        # 3. BUILD PROJECT
        # ------------------------------------

        build_project(task)

        # ------------------------------------
        # 4. FINAL VALIDATION
        # ------------------------------------

        fake_output = "OK SYSTEM GENERATED"

        self.correction.analyze_output(fake_output)

        print("\n==============================")
        print(" EXECUTION COMPLETE")
        print("==============================\n")


# ============================================
# TEST
# ============================================

if __name__ == "__main__":

    engine = AutonomousExecutionEngine()

    task = "Crear SaaS IA para clínicas médicas"

    engine.run(task)
