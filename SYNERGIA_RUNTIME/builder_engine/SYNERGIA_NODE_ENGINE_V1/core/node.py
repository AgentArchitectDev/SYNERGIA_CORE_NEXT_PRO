class Node:
    def __init__(self, name):
        self.name = name
        self.next_nodes = []

    def connect(self, node):
        self.next_nodes.append(node)

    def run(self, context):
        raise NotImplementedError
