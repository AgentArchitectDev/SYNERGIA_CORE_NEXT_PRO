
# =========================================================
# SYNERGIA RESULT MERGER
# =========================================================

class ResultMerger:

    def merge(self, results):

        final_output = "\n==============================\n"
        final_output += " SYNERGIA FINAL OUTPUT\n"
        final_output += "==============================\n"

        for agent, content in results.items():

            final_output += f"\n--- {agent.upper()} ---\n\n"

            final_output += str(content)

            final_output += "\n"

        return final_output
