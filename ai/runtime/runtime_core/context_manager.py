class ContextManager:

    def __init__(self):

        self.context = {}

    def set(self, key, value):

        self.context[key] = value

    def get(self, key, default=None):

        return self.context.get(key, default)

    def all(self):

        return self.context


context_manager = ContextManager()
