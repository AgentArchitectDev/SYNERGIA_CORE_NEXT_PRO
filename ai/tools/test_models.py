from ai.core.model_manager import model_manager
from ai.kernel.kernel import kernel


print("\n=== MODELOS OLLAMA ===\n")
print(model_manager.list_raw())

print("\n=== MODELOS PARSEADOS ===\n")
print(model_manager.list_parsed())

print("\n=== KERNEL STATUS ===\n")
kernel.boot()
print(kernel.status())
