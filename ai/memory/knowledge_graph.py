class KnowledgeGraph:
    """
    SYNERGIA KNOWLEDGE GRAPH (CORE LIGHT)
    -------------------------------------
    - Representación simple de relaciones
    - Sin dependencias externas
    - Seguro para runtime / orchestrator
    """

    def __init__(self):
        self.nodes = {}
        self.edges = []

    # -----------------------------
    # NODES
    # -----------------------------

    def add_node(self, node_id: str, data=None):
        self.nodes[node_id] = {
            "data": data or {},
            "created_at": __import__("time").time()
        }

        return self.nodes[node_id]

    def get_node(self, node_id: str):
        return self.nodes.get(node_id)

    # -----------------------------
    # EDGES (RELATIONS)
    # -----------------------------

    def add_edge(self, source: str, target: str, relation: str):
        edge = {
            "from": source,
            "to": target,
            "relation": relation,
            "timestamp": __import__("time").time()
        }

        self.edges.append(edge)
        return edge

    def get_edges(self, node_id: str = None):
        if node_id is None:
            return self.edges

        return [
            e for e in self.edges
            if e["from"] == node_id or e["to"] == node_id
        ]

    # -----------------------------
    # ANALYTICS BÁSICOS
    # -----------------------------

    def neighbors(self, node_id: str):
        return [
            e["to"] for e in self.edges if e["from"] == node_id
        ]

    def status(self):
        return {
            "nodes": len(self.nodes),
            "edges": len(self.edges)
        }


# -----------------------------
# SINGLETON EXPORT (IMPORT SEGURO)
# -----------------------------

knowledge_graph = KnowledgeGraph()
