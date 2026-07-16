"""
============================================================
SYNERGIA DASHBOARD LAUNCHER
============================================================
"""

from ai.ui.dashboard.control_center import control_center


def run_dashboard():

    control_center.start()

    try:
        while True:
            pass

    except KeyboardInterrupt:

        control_center.stop()


if __name__ == "__main__":
    run_dashboard()
