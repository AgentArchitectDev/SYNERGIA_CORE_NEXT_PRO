class Context:
    def __init__(self, task):
        self.task = task
        self.data = {}
        self.history = []

    def update(self, key, value):
        self.data[key] = value
        self.history.append((key, value))
