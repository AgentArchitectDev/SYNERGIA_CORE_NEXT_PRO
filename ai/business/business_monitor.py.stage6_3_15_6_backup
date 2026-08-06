from datetime import datetime


print("[BUSINESS MONITOR LOADED]")


class BusinessMonitor:

    def __init__(self):

        self.start_time = None
        self.end_time = None
        self.events = []
        self.current_percent = 0


    def start(self):

        self.start_time = datetime.now()

        self.events.append(
            {
                "percent": 0,
                "message": "INITIALIZING",
                "time": self.start_time.isoformat()
            }
        )


    def update(
        self,
        percent,
        message,
        model="system"
    ):

        now = datetime.now()

        self.current_percent = percent

        elapsed = None
        eta = None

        if self.start_time:

            elapsed = (
                now - self.start_time
            ).total_seconds()


            if percent > 0:

                total_estimated = (
                    elapsed * 100
                ) / percent

                eta = (
                    total_estimated - elapsed
                )


        print()

        print(
            "[MONITOR]"
        )

        print(
            f"TIME: {self.format_time(elapsed)}"
        )

        print(
            f"PROGRESS: {percent}%"
        )

        print(
            f"EVENT: {message}"
        )

        print(
            f"MODEL: {model}"
        )

        print(
            f"ETA: {self.format_time(eta)}"
        )


        self.events.append(
            {
                "percent": percent,
                "message": message,
                "model": model,
                "elapsed": elapsed,
                "eta": eta,
                "time": now.isoformat()
            }
        )


    def complete(self):

        self.end_time = datetime.now()

        self.update(
            100,
            "PROJECT COMPLETED",
            "system"
        )


    def report(self):

        elapsed = None

        if self.start_time and self.end_time:

            elapsed = (
                self.end_time - self.start_time
            ).total_seconds()


        return {

            "events": self.events,

            "elapsed_seconds": elapsed

        }


    def format_time(
        self,
        seconds
    ):

        if seconds is None:

            return "--:--"


        seconds = int(seconds)

        minutes = seconds // 60

        seconds = seconds % 60

        return (
            f"{minutes:02d}:{seconds:02d}"
        )
