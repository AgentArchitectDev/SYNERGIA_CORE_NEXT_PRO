import json
from pathlib import Path
from datetime import datetime

print("[MODEL PERFORMANCE MEMORY LOADED]")


class ModelPerformanceMemory:

    def __init__(self):

        self.file = Path(
            "storage/ai_business/model_performance.json"
        )

        self.file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.file.exists():

            self.file.write_text(
                "{}",
                encoding="utf-8"
            )


    def load(self):

        return json.loads(
            self.file.read_text(
                encoding="utf-8"
            )
        )


    def save(
        self,
        data
    ):

        self.file.write_text(
            json.dumps(
                data,
                indent=4,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )


    def update_model(
        self,
        model,
        success,
        duration
    ):

        data = self.load()

        if model not in data:

            data[model] = {

                "uses": 0,
                "success": 0,
                "failures": 0,
                "total_time": 0

            }

        item = data[model]

        item["uses"] += 1

        if success:

            item["success"] += 1

        else:

            item["failures"] += 1

        item["total_time"] += duration

        item["average_time"] = round(
            item["total_time"] /
            item["uses"],
            2
        )

        item["last_execution"] = (
            datetime.now().isoformat()
        )

        self.save(data)


