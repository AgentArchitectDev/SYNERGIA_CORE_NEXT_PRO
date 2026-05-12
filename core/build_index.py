import os
import json

BASE = "01_TEMPLATES"
OUTPUT = "00_CONTROL/index_templates.json"

index = {
    "system": "SYNERGIA_MASTER",
    "version": "1.0",
    "templates": []
}

for folder in os.listdir(BASE):
    path = os.path.join(BASE, folder)

    if os.path.isdir(path):
        config_path = os.path.join(path, "config.json")

        if os.path.exists(config_path):
            with open(config_path, "r") as f:
                data = json.load(f)

            index["templates"].append({
                "name": data.get("name"),
                "category": data.get("category"),
                "path": path
            })

with open(OUTPUT, "w") as f:
    json.dump(index, f, indent=2)

print("INDEX GENERADO OK")
