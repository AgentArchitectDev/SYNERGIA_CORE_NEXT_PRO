
class TaskClassifier:

    def classify(self, task):

        task = task.lower()

        if "backend" in task:
            return "dev"

        if "landing" in task:
            return "cms"

        if "marketing" in task:
            return "social"

        return "business"
