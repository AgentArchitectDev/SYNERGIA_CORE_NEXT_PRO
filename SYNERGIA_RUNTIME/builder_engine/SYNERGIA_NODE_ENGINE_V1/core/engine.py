from core.context import Context
from core.graph import Graph

class Engine:
    def __init__(self, graph):
        self.graph = graph

    def run(self, task):
        context = Context(task)
        return self.graph.run(context)
