
class CollabManager:

    def merge(self, results):

        final = "\n==============================\n"
        final += " SYNERGIA COLLAB OUTPUT\n"
        final += "==============================\n"

        for agent, output in results.items():

            final += f"\n\n--- {agent.upper()} ---\n\n"
            final += str(output)

        return final
