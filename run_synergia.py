# =========================================================
# SYNERGIA CORE NEXT PRO
# MAIN SYSTEM BOOT
# =========================================================

import os
import platform
from datetime import datetime

from kernel.bootstrap.bootstrap import Bootstrap


# =========================================================
# COLORS
# =========================================================

class Colors:

    RESET = "\033[0m"

    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

    BOLD = "\033[1m"


# =========================================================
# CLEAR TERMINAL
# =========================================================

def clear_terminal():

    os.system("cls" if os.name == "nt" else "clear")


# =========================================================
# HEADER
# =========================================================

def show_header():

    print(f"{Colors.CYAN}")

    print("==========================================================")
    print("            🚀 SYNERGIA CORE NEXT PRO 🚀")
    print("==========================================================")

    print(f"{Colors.YELLOW}")
    print("        AI OPERATING SYSTEM — V6 EVOLUTION")
    print("==========================================================")

    print(f"{Colors.GREEN}")
    print(f"🖥️  SYSTEM : {platform.system()} {platform.release()}")
    print(f"🐍 PYTHON : {platform.python_version()}")
    print(f"📅 DATE   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    print(f"{Colors.MAGENTA}")
    print("==========================================================")

    print(f"{Colors.WHITE}")
    print("⚡ Initializing Kernel...")
    print("⚡ Loading Runtime...")
    print("⚡ Preparing AI Services...")

    print(f"{Colors.CYAN}")
    print("==========================================================")

    print(f"{Colors.RESET}")


# =========================================================
# MAIN
# =========================================================

def main():

    clear_terminal()

    show_header()

    try:

        bootstrap = Bootstrap()

        bootstrap.start()

        print(f"{Colors.GREEN}")
        print("==========================================================")
        print("✅ SYNERGIA SYSTEM ONLINE")
        print("==========================================================")
        print(f"{Colors.RESET}")

    except Exception as e:

        print(f"{Colors.RED}")

        print("==========================================================")
        print("❌ SYSTEM ERROR")
        print("==========================================================")

        print(f"\nERROR: {e}\n")

        print("==========================================================")

        print(f"{Colors.RESET}")


# =========================================================
# START
# =========================================================

if __name__ == "__main__":

    main()
