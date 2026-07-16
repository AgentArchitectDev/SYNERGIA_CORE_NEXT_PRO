"""
======================================================
SYNERGIA CORE NEXT_PRO

Cognitive Router Rules V5

Sistema de intención cognitiva.

======================================================
"""


DEFAULT_RULES = {


    # -----------------------------------
    # MEMORY SYSTEM
    # -----------------------------------

    "memory": {

        "keywords": [

            "memoria",
            "guardar",
            "recordar",
            "knowledge",
            "contexto",
            "historial"

        ],

        "priority": 100

    },


    # -----------------------------------
    # EVOLUTION ENGINE
    # -----------------------------------

    "evolution": {

        "keywords": [

            "evolucion",
            "evolución",
            "mejorar",
            "optimizar",
            "adaptar",
            "auto",
            "self"

        ],

        "priority": 95

    },


    # -----------------------------------
    # RUNTIME SYSTEM
    # -----------------------------------

    "runtime": {

        "keywords": [

            "runtime",
            "ejecutar",
            "ejecucion",
            "ejecución",
            "proceso",
            "sistema",
            "servicio"

        ],

        "priority": 90

    },


    # -----------------------------------
    # COGNITIVE ENGINE
    # -----------------------------------

    "cognitive": {

        "keywords": [

            "cognitivo",
            "cognitive",
            "analizar",
            "pensar",
            "decidir",
            "razonar"

        ],

        "priority": 85

    },


    # -----------------------------------
    # MODEL ENGINE
    # -----------------------------------

    "ollama": {

        "keywords": [

            "modelo",
            "ollama",
            "llm",
            "ia",
            "inteligencia"

        ],

        "priority": 70

    },


    # -----------------------------------
    # RESEARCH
    # -----------------------------------

    "research": {

        "keywords": [

            "buscar",
            "internet",
            "investigar",
            "google",
            "web"

        ],

        "priority": 60

    },


    # -----------------------------------
    # EXPORT
    # -----------------------------------

    "export": {

        "keywords": [

            "exportar",
            "archivo",
            "pdf",
            "word",
            "documento"

        ],

        "priority": 50

    }

}
