# =========================================================
# SYNERGIA OS v3
# LIVE GRAPH ENGINE
# =========================================================


class LiveGraphEngine:

    def __init__(self):

        print("🎮 LIVE GRAPH ENGINE ONLINE")

    # =====================================================
    # BUILD GRAPH
    # =====================================================

    def build_graph(self, nodes):

        graph = {}

        for node in nodes:

            graph[node] = {

                "status": "ACTIVE",

                "connections": []
            }

        # =================================================
        # AUTO CONNECTIONS
        # =================================================

        if "business" in graph and "dev" in graph:

            graph["business"]["connections"].append("dev")

            graph["dev"]["connections"].append("business")

        if "social_media" in graph and "business" in graph:

            graph["social_media"]["connections"].append(
                "business"
            )

        if "cms" in graph and "dev" in graph:

            graph["cms"]["connections"].append(
                "dev"
            )

        return graph
