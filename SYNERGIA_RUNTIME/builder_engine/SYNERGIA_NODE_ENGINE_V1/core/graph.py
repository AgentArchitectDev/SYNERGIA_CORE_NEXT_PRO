class Graph:
    def __init__(self, start_node):
        self.start_node = start_node

    def run(self, context):
        current = self.start_node

        while current:
            current.run(context)
            current = current.next_nodes[0] if current.next_nodes else None

        return context
