# =========================================================
# SYNERGIA OS v3
# NODE MAPPER
# =========================================================

class NodeMapper:

    def __init__(self):

        print("🧠 NODE MAPPER ONLINE")

    # =====================================================
    # DETECT NODES
    # =====================================================

    def detect_nodes(self, task):

        task_lower = task.lower()

        nodes = []

        # =================================================
        # BUSINESS
        # =================================================

        if any(word in task_lower for word in [

            "business",
            "empresa",
            "saas",
            "crm",
            "startup",
            "negocio",
            "clientes",
            "ventas"

        ]):

            nodes.append("business")

        # =================================================
        # DEV
        # =================================================

        if any(word in task_lower for word in [

            "web",
            "app",
            "api",
            "backend",
            "frontend",
            "codigo",
            "python",
            "sistema",
            "software"

        ]):

            nodes.append("dev")

        # =================================================
        # SOCIAL MEDIA
        # =================================================

        if any(word in task_lower for word in [

            "instagram",
            "facebook",
            "marketing",
            "social",
            "contenido",
            "publicidad"

        ]):

            nodes.append("social_media")

        # =================================================
        # CMS
        # =================================================

        if any(word in task_lower for word in [

            "cms",
            "wordpress",
            "editor",
            "landing",
            "pagina"

        ]):

            nodes.append("cms")

        # =================================================
        # DEFAULT
        # =================================================

        if len(nodes) == 0:

            nodes.append("general")

        return list(set(nodes))
