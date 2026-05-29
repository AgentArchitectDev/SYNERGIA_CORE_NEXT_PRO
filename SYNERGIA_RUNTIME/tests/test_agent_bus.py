from core.runtime.live_agent_bus import LiveAgentBus


bus = LiveAgentBus()

bus.register("business")
bus.register("dev")
bus.register("social_media")


bus.send_event(
    sender="business",
    target="dev",
    event_type="REQUEST",
    content="build backend api"
)


bus.send_event(
    sender="dev",
    target="business",
    event_type="RESPONSE",
    content="backend ready"
)


print()

print(bus.get_all_events())
