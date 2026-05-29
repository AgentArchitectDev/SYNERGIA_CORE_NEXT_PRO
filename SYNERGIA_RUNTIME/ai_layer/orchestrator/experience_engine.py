
class ExperienceEngine:

    def __init__(self):

        self.experiences = []

    def add_experience(self, task, result):

        self.experiences.append({
            "task": task,
            "result": result
        })

    def get_experiences(self):

        return self.experiences
