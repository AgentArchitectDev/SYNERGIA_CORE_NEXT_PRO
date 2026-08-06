from datetime import datetime


# =========================================================
# SYNERGIA BUSINESS PROGRESS
# STAGE 6.3.15
#
# Progress tracking for autonomous business pipelines
# =========================================================


print("[BUSINESS PROGRESS LOADED]")


class BusinessProgress:


    def __init__(self):

        self.started_at = (
            datetime.now()
        )

        self.current_percent = 0

        self.current_stage = (
            "INITIALIZING"
        )

        self.history = []


        self.update(
            0,
            "INITIALIZING"
        )


    # =====================================================
    # UPDATE PROGRESS
    # =====================================================


    def update(

        self,

        percent,

        stage

    ):


        percent = max(
            0,
            min(
                100,
                int(percent)
            )
        )


        self.current_percent = (
            percent
        )


        self.current_stage = (
            str(stage)
        )


        event = {

            "percent":
                percent,

            "stage":
                str(stage),

            "timestamp":
                datetime.now()
                .isoformat()

        }


        self.history.append(
            event
        )


        print()

        print(
            f"[PROGRESS] "
            f"{percent:3d}% "
            f"→ {stage}"
        )


        return event


    # =====================================================
    # ELAPSED TIME
    # =====================================================


    def get_elapsed_seconds(self):


        elapsed = (

            datetime.now()

            - self.started_at

        )


        return round(

            elapsed.total_seconds(),

            2

        )


    # =====================================================
    # STATUS
    # =====================================================


    def get_status(self):


        return {

            "percent":
                self.current_percent,

            "stage":
                self.current_stage,

            "started_at":
                self.started_at
                .isoformat(),

            "elapsed_seconds":
                self
                .get_elapsed_seconds(),

            "events":
                len(
                    self.history
                ),

            "history":
                self.history

        }


    # =====================================================
    # COMPLETE
    # =====================================================


    def complete(

        self,

        stage="PROJECT COMPLETED"

    ):


        return self.update(

            100,

            stage

        )
