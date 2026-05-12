import os
import json

BASE = "01_TEMPLATES"

def detect_category(name):
    name = name.lower()
    if "arquitectura" in name or "arq" in name:
        return "arquitectura"
    if "gastro" in name:
        return "gastronomia"
    if "real" in name:
        return "real_estate"
    if "tech" in name:
        return "tecnologia"
    return "general"

def create_config(template_name, path):
    config = {
        "name": template_name.replace("_", " ").title(),
        "category": detect_category(template_name),
        "version": "1.0",
        "sections": ["hero","content","gallery","cta","footer"],
        "status": "base_template"
    }
    with open(os.path.join(path, "config.json"), "w") as f:
        json.dump(config, f, indent=2)

def create_doc(template_name, path):
    content = f"# {template_name}\n\nTemplate base generado automáticamente."
    with open(os.path.join(path, "doc.md"), "w") as f:
        f.write(content)

for folder in os.listdir(BASE):
    path = os.path.join(BASE, folder)
    if os.path.isdir(path):
        print(f"Procesando: {folder}")
        create_config(folder, path)
        create_doc(folder, path)

print("OK")
