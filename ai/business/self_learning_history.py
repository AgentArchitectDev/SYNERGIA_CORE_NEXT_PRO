from pathlib import Path
import json
from datetime import datetime


HISTORY_FILE = Path(
    "storage/ai_learning/self_learning_history.json"
)


class SelfLearningHistory:


    def __init__(self):

        HISTORY_FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not HISTORY_FILE.exists():

            HISTORY_FILE.write_text(
                "[]",
                encoding="utf-8"
            )



    def save_analysis(
        self,
        analysis
    ):


        data = self.load()


        entry = {

            "timestamp":
                datetime.now().isoformat(),

            "success_rate":
                analysis.get(
                    "success_rate",
                    0
                ),

            "recommendation":
                analysis.get(
                    "recommendation",
                    ""
                ),

            "action":
                "KEEP_STRATEGY"

        }


        data.append(entry)


        HISTORY_FILE.write_text(

            json.dumps(
                data,
                indent=4
            ),

            encoding="utf-8"

        )


        return entry



    def load(self):

        try:

            return json.loads(

                HISTORY_FILE.read_text(
                    encoding="utf-8"
                )

            )


        except Exception:

            return []



self_learning_history = SelfLearningHistory()


print(
    "[SELF LEARNING HISTORY LOADED]"
)
