#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

PIPELINE MEMORY

CORE IA SYSTEMS

ACEA VERSION 1.0

============================================================

Memoria operacional del Pipeline.

Guarda experiencias:

- solicitudes
- categorías
- agentes utilizados
- modelos seleccionados
- resultados


Evolución futura:

Memory Engine
Long Term Memory
Vector Memory
Cognitive Memory


============================================================
"""


import json
import time
from pathlib import Path



class PipelineMemory:


    def __init__(self):

        self.initialized = False

        self.records = []

        self.file = Path(
            "storage/omega_pipeline_memory.json"
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

            "pipeline_memory_ready",


            "records":

            len(self.records)

        }



    # --------------------------------------------------

    def save(
        self,
        request,
        category,
        agents,
        model,
        result
    ):


        memory = {


            "id":

            len(self.records)+1,


            "request":

            request,


            "category":

            category,


            "agents":

            agents,


            "model":

            model,


            "result":

            result,


            "timestamp":

            time.time()

        }



        self.records.append(
            memory
        )


        self._persist()


        return memory



    # --------------------------------------------------

    def search(
        self,
        text
    ):


        results = []


        text = text.lower()


        for item in self.records:


            if text in item["request"].lower():

                results.append(
                    item
                )


        return results



    # --------------------------------------------------

    def stats(self):


        return {


            "component":

            "OMEGA Pipeline Memory",


            "initialized":

            self.initialized,


            "records":

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



# ------------------------------------------------------

pipeline_memory = PipelineMemory()
