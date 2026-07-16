import time
from ai.memory.knowledge_layer import memory_knowledge_layer
from ai.memory.knowledge_graph import knowledge_graph


class CognitiveLayer:
    """
    SYNERGIA COGNITIVE LAYER
    ------------------------
    - Fusiona memoria + conocimiento estructurado
    - Genera contexto útil para el runtime
    - Base del "mini cerebro operativo"
    """

    def __init__(self):
        self.last_context = None

    # -----------------------------
    # CONTEXT BUILDER
    # -----------------------------

    def build_context(self, input_text: str):

        memory_hits = memory_knowledge_layer.search(input_text)

        related_nodes = [
            node for node in knowledge_graph.nodes.keys()
            if input_text.lower() in node.lower()
        ]

        graph_summary = {
            "nodes": list(related_nodes),
            "edges": knowledge_graph.get_edges()
        }

        context = {
            "timestamp": time.time(),
            "input": input_text,
            "memory": memory_hits,
            "graph": graph_summary
        }

        self.last_context = context
        return context

    # -----------------------------
    # SIMPLE DECISION ENGINE
    # -----------------------------

    def decide(self, input_text: str):

        context = self.build_context(input_text)

        score_memory = len(context["memory"])
        score_graph = len(context["graph"]["edges"])

        if "guardar" in input_text or "memoria" in input_text:
            action = "memory_store"
        elif "buscar" in input_text:
            action = "research"
        elif score_graph > score_memory:
            action = "graph_reasoning"
        else:
            action = "default_processing"

        return {
            "action": action,
            "context": context
        }

    def status(self):
        return {
            "active": True,
            "last_context": self.last_context is not None
        }


# -----------------------------
# SINGLETON
# -----------------------------

cognitive_layer = CognitiveLayer()
