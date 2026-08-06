import json
import os
from datetime import datetime


# =========================================================
# SYNERGIA MODEL RANKER V2
# STAGE 6.3.3 - MODEL PERFORMANCE SCORE
# =========================================================


class ModelRanker:


    def __init__(self):

        self.file = "ai/brain/model_ranking.json"

        os.makedirs(
            os.path.dirname(self.file),
            exist_ok=True
        )

        if not os.path.exists(self.file):

            with open(
                self.file,
                "w"
            ) as f:

                json.dump(
                    {},
                    f,
                    indent=2
                )


    # =====================================================
    # LOAD
    # =====================================================

    def _load(self):

        with open(
            self.file,
            "r"
        ) as f:

            return json.load(f)



    # =====================================================
    # SAVE
    # =====================================================

    def _save(
        self,
        data
    ):

        with open(
            self.file,
            "w"
        ) as f:

            json.dump(
                data,
                f,
                indent=2
            )


    # =====================================================
    # UPDATE BASIC COMPATIBILITY
    # =====================================================

    def update(
        self,
        model,
        score=1
    ):

        self.register_execution(

            model=model,

            score=score

        )


    # =====================================================
    # REGISTER EXECUTION
    # =====================================================

    def register_execution(
        self,
        model,
        duration=0,
        success=True,
        score=None
    ):

        data = self._load()


        if model not in data:

            data[model] = {

                "score": 0,

                "uses": 0,

                "success": 0,

                "failures": 0,

                "total_time": 0,

                "avg_time": 0,

                "last_execution": None

            }


        item = data[model]


        item["uses"] += 1


        if success:

            item["success"] += 1

        else:

            item["failures"] += 1



        item["total_time"] += duration


        item["avg_time"] = round(

            item["total_time"] /

            item["uses"],

            2

        )


        if score is None:

            score = self.calculate_score(
                item
            )


        item["score"] = score


        item["last_execution"] = (
            datetime.now()
            .isoformat()
        )


        self._save(data)


        return item



    # =====================================================
    # SCORE CALCULATION
    # =====================================================

    def calculate_score(
        self,
        item
    ):

        success_rate = (

            item["success"] /

            item["uses"]

        )


        speed_bonus = 0


        if item["avg_time"]:

            speed_bonus = (

                30 /

                item["avg_time"]

            )


        score = (

            success_rate * 100

            +

            speed_bonus

        )


        return round(
            score,
            2
        )



    # =====================================================
    # BEST MODEL
    # =====================================================

    def best_model(self):

        data = self._load()


        if not data:

            return None


        best = max(

            data.items(),

            key=lambda x:
            x[1]["score"]

        )


        return best[0]



# =========================================================
# SINGLETON
# =========================================================

model_ranker = ModelRanker()
