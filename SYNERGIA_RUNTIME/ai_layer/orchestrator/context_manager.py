
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

            context += f"\n\n=== {agent.upper()} OUTPUT ===\n"

            context += str(output)

        return context
