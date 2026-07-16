"""
============================================================
SYNERGIA COGNITIVE OS
Task Queue
============================================================
"""


class TaskQueue:

    def __init__(self):

        self.queue = []

    # -------------------------------------------------

    def push(self, task):

        self.queue.append(task)

    # -------------------------------------------------

    def pop(self):

        if len(self.queue) == 0:
            return None

        return self.queue.pop(0)

    # -------------------------------------------------

    def size(self):

        return len(self.queue)

    # -------------------------------------------------

    def dump(self):

        return self.queue
