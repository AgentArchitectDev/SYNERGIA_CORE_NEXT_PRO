class MemoryKnowledgeLayer:
    """
    ULTRA SAFE MEMORY LAYER
    (sin imports externos, sin IO automático)
    """

    def __init__(self):
        self.memory = []

    def store(self, input_text, plan=None, results=None):
        record = {
            "input": input_text,
            "plan": plan or [],
            "results": results or []
        }

        self.memory.append(record)
        return record

    def search(self, keyword: str):
        return [
            m for m in self.memory
            if keyword.lower() in m["input"].lower()
        ]

    def status(self):
        return {
            "records": len(self.memory)
        }


# 🔥 EXPORT FORZADO (SIN POSIBILIDAD DE FALLA)
memory_knowledge_layer = MemoryKnowledgeLayer()
