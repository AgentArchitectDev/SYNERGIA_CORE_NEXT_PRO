import json
import os


# ============================================
# EXPERIENCE ENGINE
# ============================================

class ExperienceEngine:


    def __init__(self):

        self.memory_path = "experiences.json"

        self.experiences = self.load_memory()


    # ========================================
    # LOAD MEMORY
    # ========================================

    def load_memory(self):

        if os.path.exists(self.memory_path):

            with open(self.memory_path, "r") as file:

                return json.load(file)

        return []


    # ========================================
    # SAVE MEMORY
    # ========================================

    def save_memory(self):

        with open(self.memory_path, "w") as file:

            json.dump(

                self.experiences,
                file,
                indent=4
            )


    # ========================================
    # ADD EXPERIENCE
    # ========================================

    def add_experience(

        self,
        task,
        result
    ):

        experience = {

            "task": task,
            "result": result
        }

        self.experiences.append(experience)

        self.save_memory()

        print("\n🧠 EXPERIENCE SAVED")


    # ========================================
    # SHOW EXPERIENCES
    # ========================================

    def show_experiences(self):

        print("\n==============================")
        print(" EXPERIENCES")
        print("==============================\n")

        for exp in self.experiences:

            print(f"🧠 TASK:\n{exp['task']}\n")

            print(f"📄 RESULT:\n{exp['result']}\n")

            print("-------------------------")


# ============================================
# TEST
# ============================================

if __name__ == "__main__":

    engine = ExperienceEngine()

    engine.add_experience(

        "Crear SaaS IA para restaurantes",

        "Arquitectura generada correctamente"
    )

    engine.show_experiences()
