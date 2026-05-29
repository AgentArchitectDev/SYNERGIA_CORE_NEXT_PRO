from agents.agent_collab_v2 import AgentCollabV2

system = AgentCollabV2()

result = system.run_project(
    "Plataforma IA para automatizar negocios digitales"
)

print("\n==============================")
print(" FINAL OUTPUT v2")
print("==============================\n")

for k, v in result.items():
    print("\n---", k.upper(), "---\n")
    print(v)
