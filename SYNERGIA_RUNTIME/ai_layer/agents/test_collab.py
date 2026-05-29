from agents.agent_collab import AgentCollab

system = AgentCollab()

project = system.run_project(
    "SaaS de automatización de redes sociales con IA"
)

print("\n==============================")
print(" FINAL OUTPUT")
print("==============================\n")

for k, v in project.items():
    print("\n---", k.upper(), "---\n")
    print(v)
