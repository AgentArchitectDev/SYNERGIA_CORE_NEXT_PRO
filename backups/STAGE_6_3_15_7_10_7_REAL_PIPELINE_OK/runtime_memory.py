# =========================================================
# SYNERGIA CORE NEXT PRO
# AI RUNTIME MEMORY BRIDGE
#
# STAGE 6.3.15.7.7.3
#
# RUNTIME EXPERIENCE MEMORY
# + ADAPTIVE LEARNING SUPPORT
#
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


        self.memory = self.load()



    # =====================================================
    # LOAD
    # =====================================================

    def load(self):

        if not self.memory_file.exists():

            return {

                "experiences": [],

                "total_executions": 0,

                "successful": 0,

                "failed": 0,

                "created_at":
                    datetime.now().isoformat()

            }


        return json.loads(
            self.memory_file.read_text(
                encoding="utf-8"
            )
        )



    # =====================================================
    # SAVE
    # =====================================================

    def save(self):

        self.memory_file.write_text(

            json.dumps(
                self.memory,
                indent=4,
                ensure_ascii=False
            ),

            encoding="utf-8"
        )



    # =====================================================
    # CORE MEMORY METHOD
    #
    # Legacy compatible
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
                datetime.now().isoformat()

        }



        self.memory["experiences"].append(
            experience
        )


        self.memory["total_executions"] += 1



        if status == "SUCCESS":

            self.memory["successful"] += 1

        else:

            self.memory["failed"] += 1



        self.save()


        return experience



    # =====================================================
    # MODERN MEMORY API
    #
    # Used by:
    # TaskEngine
    # Adaptive Router
    # Learning Loop
    #
    # =====================================================

    def add_experience(
        self,
        task,
        model,
        status,
        duration_seconds,
        metadata=None
    ):


        return self.remember(

            task=task,

            model=model,

            status=status,

            duration=duration_seconds,

            metadata=metadata

        )



    # =====================================================
    # STATUS
    # =====================================================

    def status(self):

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

                self.memory["experiences"][-1]

                if self.memory["experiences"]

                else None

        }



    # =====================================================
    # GET EXPERIENCES
    # =====================================================

    def get_experiences(self):

        return self.memory["experiences"]



    # =====================================================
    # SEARCH BY TASK
    # =====================================================

    def get_by_task(
        self,
        task
    ):

        return [

            item

            for item in self.memory["experiences"]

            if item["task"] == task

        ]



    # =====================================================
    # MODEL PERFORMANCE MEMORY
    # =====================================================

    def model_stats(
        self,
        model
    ):


        items = [

            x

            for x in self.memory["experiences"]

            if x["model"] == model

        ]


        return {


            "model": model,

            "uses": len(items),

            "success":
                sum(
                    1
                    for x in items
                    if x["status"] == "SUCCESS"
                ),

            "average_time":

                sum(
                    x["duration_seconds"]
                    for x in items
                )
                /
                len(items)

                if items

                else 0

        }



# =========================================================
# GLOBAL INSTANCE
# =========================================================

runtime_memory = RuntimeMemory()
