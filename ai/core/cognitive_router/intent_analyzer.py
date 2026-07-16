"""
======================================================
SYNERGIA CORE NEXT_PRO

Intent Analyzer V5

Analizador de intención cognitiva.

Responsabilidades:

- Detectar intención del usuario
- Evitar falsos positivos
- Trabajar con Cognitive Router V5
- Generar señales para Priority Engine

======================================================
"""


import re

from .rules import DEFAULT_RULES



class IntentAnalyzer:


    def __init__(self):

        self.executions = 0

        self.history = []



    # -------------------------------------------------
    # TOKENIZER
    # -------------------------------------------------

    def tokenize(self, text: str):

        """
        Convierte texto en palabras reales.

        Ejemplo:

        "SYNERGIA usa IA"

        devuelve:

        [
          "synergia",
          "usa",
          "ia"
        ]
        """

        return re.findall(
            r"\b[\wáéíóúñ]+\b",
            text.lower()
        )



    # -------------------------------------------------
    # INTENT ANALYSIS
    # -------------------------------------------------

    def analyze(self, text: str):


        self.executions += 1


        tokens = self.tokenize(
            text
        )


        intents = []



        for module, info in DEFAULT_RULES.items():


            for keyword in info["keywords"]:


                keyword = keyword.lower()


                # ---------------------------------
                # coincidencia exacta
                # ---------------------------------

                if keyword in tokens:


                    intents.append({

                        "module": module,

                        "priority":
                            info["priority"],

                        "keyword":
                            keyword

                    })


                    break



        # Guardar histórico

        self.history.append({

            "input": text,

            "tokens": tokens,

            "intents": intents

        })


        return intents



    # -------------------------------------------------
    # STATUS
    # -------------------------------------------------

    def status(self):


        return {


            "component":
                "Intent Analyzer V5",


            "executions":
                self.executions,


            "history":
                len(
                    self.history
                )

        }





intent_analyzer = IntentAnalyzer()
