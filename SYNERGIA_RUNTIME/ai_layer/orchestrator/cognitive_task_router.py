# ============================================
# SYNERGIA COGNITIVE TASK ROUTER
# ============================================


class CognitiveTaskRouter:


    # ========================================
    # ANALYZE TASK
    # ========================================

    def analyze_task(self, task):

        task = task.lower()

        analysis = {

            "business": False,
            "backend": False,
            "frontend": False,
            "mobile": False,
            "marketing": False,
            "automation": False,
            "ai": False
        }

        # ------------------------------------

        if "saas" in task or "crm" in task:

            analysis["business"] = True

        if "backend" in task or "api" in task:

            analysis["backend"] = True

        if "frontend" in task or "dashboard" in task:

            analysis["frontend"] = True

        if "mobile" in task or "app" in task:

            analysis["mobile"] = True

        if "marketing" in task or "ventas" in task:

            analysis["marketing"] = True

        if "automatizar" in task:

            analysis["automation"] = True

        if "ia" in task or "inteligencia artificial" in task:

            analysis["ai"] = True

        return analysis


    # ========================================
    # SELECT AGENTS
    # ========================================

    def select_agents(self, analysis):

        agents = []

        if analysis["business"]:

            agents.append("business")

        if analysis["backend"] or analysis["ai"]:

            agents.append("dev")

        if analysis["frontend"]:

            agents.append("cms")

        if analysis["mobile"]:

            agents.append("mobile")

        if analysis["marketing"]:

            agents.append("social")

        if analysis["automation"]:

            agents.append("automation")

        return agents


    # ========================================
    # CREATE WORKFLOW
    # ========================================

    def create_workflow(self, agents):

        workflow = []

        step = 1

        for agent in agents:

            workflow.append({

                "step": step,
                "agent": agent
            })

            step += 1

        return workflow


# ============================================
# TEST
# ============================================

if __name__ == "__main__":

    router = CognitiveTaskRouter()

    task = """
    Crear SaaS IA para gimnasios
    con app móvil y automatización
    de marketing
    """

    print("\n==============================")
    print(" SYNERGIA COGNITIVE ROUTER")
    print("==============================\n")

    analysis = router.analyze_task(task)

    print("🧠 ANALYSIS:")
    print(analysis)

    agents = router.select_agents(analysis)

    print("\n🤖 AGENTS:")
    print(agents)

    workflow = router.create_workflow(agents)

    print("\n⚙️ WORKFLOW:")

    for step in workflow:

        print(step)

    print("\n==============================")
    print(" ROUTING COMPLETE")
    print("==============================\n")
