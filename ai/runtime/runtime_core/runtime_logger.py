import time


class RuntimeLogger:

    def __init__(self):

        self.logs = []

    def log(self, level, message):

        self.logs.append({

            "time": time.time(),

            "level": level,

            "message": message

        })

    def info(self, msg):

        self.log("INFO", msg)

    def warning(self, msg):

        self.log("WARNING", msg)

    def error(self, msg):

        self.log("ERROR", msg)

    def last(self, n=20):

        return self.logs[-n:]


runtime_logger = RuntimeLogger()
