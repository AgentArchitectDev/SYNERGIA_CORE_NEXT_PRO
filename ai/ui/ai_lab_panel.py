from ai.runtime.orchestrator import Orchestrator

orch = Orchestrator()


def send_request(user_input):
    result = orch.handle(user_input)
    print("\n[UI RESPONSE]", result)
    return result


def start_ui():
    print("\n=== SYNERGIA CONTROL CENTER V2 ===")

    while True:
        msg = input("SYNERGIA> ")

        if msg.lower() == "exit":
            break

        send_request(msg)


if __name__ == "__main__":
    start_ui()
