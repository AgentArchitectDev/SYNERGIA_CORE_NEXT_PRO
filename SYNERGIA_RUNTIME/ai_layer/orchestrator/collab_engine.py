
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
