"""
============================================================
SYNERGIA CONTEXT BUILDER
Builds unified context from memory + knowledge
============================================================
"""

from ai.memory.global_memory import global_memory
from ai.memory.knowledge_graph import knowledge_graph


class ContextBuilder:

    def build(self, input_text: str):

        # -----------------------------
        # MEMORY CONTEXT
        # -----------------------------

        memory_hits = global_memory.search(input_text)

        # -----------------------------
        # GRAPH CONTEXT
        # -----------------------------

        graph_context = []

        for m in memory_hits:

            node = str(m["data"])[:50]

            graph_context.append(
                knowledge_graph.query_related(node)
            )

        return {
            "input": input_text,
            "memory": memory_hits,
            "knowledge": graph_context
        }


context_builder = ContextBuilder()
