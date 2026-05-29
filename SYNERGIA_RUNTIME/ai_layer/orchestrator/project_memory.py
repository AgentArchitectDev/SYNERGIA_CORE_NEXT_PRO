
class ProjectMemory:

    def __init__(self):

        self.projects = []

    def save_project(self, name, data):

        self.projects.append({
            "name": name,
            "data": data
        })

    def get_projects(self):

        return self.projects
