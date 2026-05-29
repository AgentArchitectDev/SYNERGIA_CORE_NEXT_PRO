# =====================================================
# NODE MAPPER
# =====================================================

class NodeMapper:

    def __init__(self):

        self.keywords = {

            "business": [

                "saas",
                "startup",
                "crm",
                "empresa",
                "negocio",
                "ventas",
                "monetización",
                "clientes",
                "analytics",
                "dashboard",
                "plataforma"
            ],

            "dev": [

                "backend",
                "api",
                "fastapi",
                "docker",
                "cloud",
                "jwt",
                "postgresql",
                "frontend",
                "fullstack",
                "desarrollo",
                "sistema"
            ],

            "social_media": [

                "instagram",
                "tiktok",
                "youtube",
                "marketing",
                "contenido",
                "redes",
                "social",
                "automation",
                "automatización"
            ],

            "cms": [

                "contenido",
                "blog",
                "cms",
                "wordpress",
                "artículos"
            ]
        }

    # =================================================
    # DETECT NODES
    # =================================================

    def detect_nodes(self, task):

        task = task.lower()

        detected = []

        # =============================================
        # SEARCH
        # =============================================

        for node, words in self.keywords.items():

            for word in words:

                if word in task:

                    detected.append(node)

                    break

        # =============================================
        # FALLBACK
        # =============================================

        if not detected:

            detected.append("business")

        return list(set(detected))
