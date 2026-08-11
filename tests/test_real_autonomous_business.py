# =========================================================
# SYNERGIA REAL AUTONOMOUS BUSINESS TEST
#
# STAGE 6.3.15.7.8.3
#
# =========================================================


from ai.business.adaptive_model_router import (
    AdaptiveModelRouter
)

from ai.memory.runtime_memory import (
    runtime_memory
)



print("="*60)
print("[REAL AUTONOMOUS BUSINESS TEST]")
print("="*60)



print("\n[CURRENT MEMORY]")
print(
    runtime_memory.status()
)



router = AdaptiveModelRouter()



tasks = [

    {
        "task":
            "WEBSITE",

        "default":
            "llama3.2:1b"
    },


    {
        "task":
            "BRANDING",

        "default":
            "gemma3:4b"
    },


    {
        "task":
            "SOCIAL",

        "default":
            "llama3.2:3b"
    },


    {
        "task":
            "DOCS",

        "default":
            "mistral:latest"
    }

]



print("\n[AUTONOMOUS DECISIONS]")
print("-"*60)



for item in tasks:


    result = router.select_model(

        item["task"],

        item["default"]

    )


    print()

    print(
        "TASK:",
        item["task"]
    )


    print(
        "MODEL:",
        result["model"]
    )


    print(
        "SOURCE:",
        result["source"]
    )


    print(
        "REASON:",
        result["reason"]
    )



print("\n[TEST COMPLETE]")
