# =========================================================
# SYNERGIA CORE NEXT PRO
# AI RUNTIME MEMORY BRIDGE
# STAGE 6.3.15.7.7
# EXPERIENCE MEMORY LAYER
# =========================================================


import json

from pathlib import Path
from datetime import datetime


print("[RUNTIME MEMORY LOADED]")



class RuntimeMemory:


    def __init__(self):

        self.storage = Path(
            "storage/ai_memory"
        )


        self.storage.mkdir(
            parents=True,
            exist_ok=True
        )


        self.memory_file = (
            self.storage /
            "runtime_experience.json"
        )


        self.memory = (
            self.load()
        )



    # =====================================================
    # LOAD MEMORY
    # =====================================================

    def load(
        self
    ):


        if not self.memory_file.exists():

            return {
                "experiences": [],
                "total_executions": 0,
                "successful": 0,
                "failed": 0,
                "created_at":
                    datetime.now()
                    .isoformat()
            }


        return json.loads(
            self.memory_file.read_text(
                encoding="utf-8"
            )
        )



    # =====================================================
    # SAVE MEMORY
    # =====================================================

    def save(
        self
    ):


        self.memory_file.write_text(
            json.dumps(
                self.memory,
                indent=4,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )



    # =====================================================
    # REGISTER EXPERIENCE
    # =====================================================

    def remember(
        self,
        task,
        model,
        status,
        duration,
        metadata=None
    ):


        experience = {


            "id":
                len(
                    self.memory["experiences"]
                ) + 1,


            "task":
                task,


            "model":
                model,


            "status":
                status,


            "duration_seconds":
                duration,


            "metadata":
                metadata
                if metadata
                else {},


            "timestamp":
                datetime.now()
                .isoformat()

        }



        self.memory[
            "experiences"
        ].append(
            experience
        )


        self.memory[
            "total_executions"
        ] += 1



        if status == "SUCCESS":

            self.memory[
                "successful"
            ] += 1


        else:

            self.memory[
                "failed"
            ] += 1



        self.save()


        return experience



    # =====================================================
    # GET MEMORY STATUS
    # =====================================================

    def status(
        self
    ):


        return {


            "total_executions":
                self.memory[
                    "total_executions"
                ],


            "successful":
                self.memory[
                    "successful"
                ],


            "failed":
                self.memory[
                    "failed"
                ],


            "experiences":

                len(
                    self.memory[
                        "experiences"
                    ]
                ),


            "last_experience":

                self.memory[
                    "experiences"
                ][-1]
                if self.memory[
                    "experiences"
                ]
                else None

        }



    # =====================================================
    # GET ALL EXPERIENCES
    # =====================================================

    def get_experiences(
        self
    ):

        return (
            self.memory[
                "experiences"
            ]
        )
