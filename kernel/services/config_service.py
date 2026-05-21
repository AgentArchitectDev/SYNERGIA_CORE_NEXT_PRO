import json
from pathlib import Path


class ConfigService:

    @staticmethod
    def system_config():

        config_path = Path("config/system/system.json")

        if not config_path.exists():
            return {}

        with open(config_path, "r") as f:
            return json.load(f)
