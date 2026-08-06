#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

EXECUTION HISTORY MANAGER

CORE IA SYSTEMS

ACEA VERSION 1.0

============================================================

Historial operacional del Runtime.

Registra:

- ejecuciones
- tareas
- agentes
- modelos
- resultados
- tiempos


Evolución futura:

Execution Analytics
Learning System
Cognitive Feedback
Distributed History


============================================================
"""


import time
import json
from pathlib import Path



class ExecutionHistory:


    def __init__(self):


        self.initialized = False


        self.records = []


        self.file = Path(
            "storage/omega_execution_history.json"
        )



    # --------------------------------------------------

    def initialize(self):


        self.file.parent.mkdir(
            exist_ok=True
        )


        if self.file.exists():

            try:

                self.records = json.loads(

                    self.file.read_text(
                        encoding="utf-8"
                    )

                )

            except:

                self.records = []



        self.initialized = True



        return {


            "status":

            "execution_history_ready",


            "records":

            len(self.records)

        }



    # --------------------------------------------------

    def register(

        self,
        task,
        node="MAQ2",
        agent=None,
        model=None,
        result="completed"

    ):


        record = {


            "id":

            len(self.records)+1,


            "task":

            task,


            "node":

            node,


            "agent":

            agent,


            "model":

            model,


            "result":

            result,


            "timestamp":

            time.time()

        }



        self.records.append(
            record
        )


        self._persist()



        return record




    # --------------------------------------------------

    def search(
        self,
        text
    ):


        text = text.lower()


        results = []



        for item in self.records:


            if text in item["task"].lower():

                results.append(
                    item
                )



        return results




    # --------------------------------------------------

    def latest(self):


        if not self.records:

            return None


        return self.records[-1]




    # --------------------------------------------------

    def stats(self):


        return {


            "component":

            "OMEGA Execution History",


            "initialized":

            self.initialized,


            "executions":

            len(self.records)

        }




    # --------------------------------------------------

    def _persist(self):


        self.file.write_text(

            json.dumps(

                self.records,

                indent=4,

                ensure_ascii=False

            ),

            encoding="utf-8"

        )





execution_history = ExecutionHistory()
