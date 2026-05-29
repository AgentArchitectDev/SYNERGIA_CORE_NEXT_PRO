# =========================================================
# SYNERGIA AGENT CORE v4
# =========================================================

import sys
import os

# =========================================================
# PATH FIX
# =========================================================

CURRENT_DIR = os.path.dirname(__file__)

AI_LAYER_PATH = os.path.abspath(
    os.path.join(CURRENT_DIR, "..")
)

sys.path.append(AI_LAYER_PATH)

# =========================================================
# IMPORTS
# =========================================================

from ai_engine import AIEngine


# =========================================================
# AGENT CORE
# =========================================================

class AgentCore:

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self):

        self.engine = AIEngine()

        self.roles = {

            "business": """
Business AI Strategist

Especialista en:
- modelos SaaS
- monetización
- automatización
- startups IA
- negocios digitales
- escalabilidad
- funnels
- revenue
""",

            "dev": """
Backend & System Architect

Especialista en:
- arquitectura backend
- APIs
- microservicios
- Python
- Node.js
- bases de datos
- automatización
- infraestructura
- AI systems
""",

            "cms": """
CMS & UX Architect

Especialista en:
- diseño UX/UI
- landing pages
- frontend
- CMS
- experiencia de usuario
- branding
- estructura web
- diseño SaaS
""",

            "social": """
Marketing & Social AI

Especialista en:
- marketing digital
- SEO
- campañas
- redes sociales
- branding
- contenido viral
- growth marketing
- estrategia LATAM
"""
        }

    # =====================================================
    # RUN AGENT
    # =====================================================

    def run_agent(
        self,
        agent_name,
        task
    ):

        print("\n==============================")
        print(" SYNERGIA AGENT CORE v4")
        print("==============================")

        print(f"\n🤖 Agent: {agent_name}")

        role = self.roles.get(
            agent_name,
            "General AI Assistant"
        )

        # =================================================
        # SYSTEM PROMPT
        # =================================================

        prompt = f"""
SOS un agente IA profesional de SYNERGIA CORE NEXT PRO.

RESPONDÉ SIEMPRE:

- en español latinoamericano
- con estilo profesional moderno
- orientado a Argentina y LATAM
- usando markdown ordenado
- evitando inglés innecesario
- explicando de forma clara
- pensando como una startup tecnológica
- actuando como un sistema operativo IA

Tu rol actual es:

{role}

TAREA:

{task}
"""

        # =================================================
        # EXECUTION
        # =================================================

        response = self.engine.generate(
            prompt
        )

        return response


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    agent = AgentCore()

    result = agent.run_agent(
        "business",
        "Crear SaaS IA para automatizar negocios"
    )

    print(result)
