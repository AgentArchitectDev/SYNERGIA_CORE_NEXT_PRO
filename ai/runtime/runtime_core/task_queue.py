class TaskQueue:

    def __init__(self):

        self.queue = []

    def push(self, task):

        self.queue.append(task)

    def pop(self):

        if not self.queue:
            return None

        return self.queue.pop(0)

    def size(self):

        return len(self.queue)


task_queue = TaskQueue()
