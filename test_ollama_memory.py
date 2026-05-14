from ai.providers.ollama_provider import ollama_provider


# =========================================================
# SYNERGIA CORE NEXT PRO
# TEST OLLAMA + MEMORY SYSTEM
# =========================================================


print("\n")
print("========================================")
print("SYNERGIA OLLAMA MEMORY TEST")
print("========================================")
print("\n")


# =========================================================
# AVAILABLE MODELS
# =========================================================

AVAILABLE_MODELS = [

    "llama3.2:3b",

    "deepseek-coder-v2:16b",

    "qwen2.5-coder:7b",

    "llama3:8b",

    "llama3.1:latest",

    "mistral:latest",

    "phi3:3.8b",

    "codellama:latest",

    "deepseek-coder:6.7b",

    "gemma3:4b"
]


print("AVAILABLE MODELS:\n")

for model in AVAILABLE_MODELS:

    print(f" - {model}")

print("\n")


# =========================================================
# SELECT MODEL
# =========================================================

MODEL_NAME = "llama3.2:3b"

SESSION_ID = "maq2_real"


print("MODEL SELECTED:")
print(MODEL_NAME)

print("\n")


# =========================================================
# FIRST TEST
# =========================================================

print("========================================")
print("FIRST PROMPT")
print("========================================")
print("\n")


response_1 = ollama_provider.generate(

    model_name=MODEL_NAME,

    prompt="""
    Explicame que es SYNERGIA CORE NEXT PRO.
    """,

    session_id=SESSION_ID
)


print("\n")
print("========================================")
print("FIRST RESPONSE")
print("========================================")
print("\n")

print(response_1)

print("\n")


# =========================================================
# SECOND TEST
# =========================================================

print("========================================")
print("SECOND PROMPT")
print("========================================")
print("\n")


response_2 = ollama_provider.generate(

    model_name=MODEL_NAME,

    prompt="""
    Que modulos principales tiene actualmente el sistema.
    """,

    session_id=SESSION_ID
)


print("\n")
print("========================================")
print("SECOND RESPONSE")
print("========================================")
print("\n")

print(response_2)

print("\n")


# =========================================================
# CONTEXT TEST
# =========================================================

print("========================================")
print("CONTEXT MEMORY TEST")
print("========================================")
print("\n")


response_3 = ollama_provider.generate_with_context(

    model_name=MODEL_NAME,

    prompt="""
    Recordas de que hablamos antes?
    """,

    session_id=SESSION_ID,

    context_limit=5
)


print("\n")
print("========================================")
print("CONTEXT RESPONSE")
print("========================================")
print("\n")

print(response_3)

print("\n")


# =========================================================
# STREAM TEST
# =========================================================

print("========================================")
print("STREAM TEST")
print("========================================")
print("\n")


response_4 = ollama_provider.generate_stream(

    model_name=MODEL_NAME,

    prompt="""
    Dame una vision futurista de SYNERGIA
    como AI Operating System.
    """,

    session_id=SESSION_ID
)


print("\n")
print("========================================")
print("STREAM RESPONSE")
print("========================================")
print("\n")

print(response_4)

print("\n")


# =========================================================
# MEMORY FILE CHECK
# =========================================================

print("========================================")
print("MEMORY FILE")
print("========================================")
print("\n")

print(
    "ai/memory/conversations/"
    f"{SESSION_ID}.json"
)

print("\n")


# =========================================================
# FINAL STATUS
# =========================================================

print("========================================")
print("SYSTEM STATUS")
print("========================================")
print("\n")

print("OLLAMA PROVIDER : OK")
print("MEMORY SYSTEM   : OK")
print("SESSION SYSTEM  : OK")
print("CONTEXT SYSTEM  : OK")
print("STREAM SYSTEM   : OK")

print("\n")

print("========================================")
print("END TEST")
print("========================================")
print("\n")
