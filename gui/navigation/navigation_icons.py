"""
====================================================================
SYNERGIA OMEGA UI
Navigation Icons Manager V6 Enterprise
====================================================================

Registro centralizado de iconos.

Responsabilidades:

✔ Administración de iconos
✔ Alias de iconos
✔ Iconos por módulo
✔ Fallback
✔ Preparado para temas OMEGA

Futuro:

✔ SVG Loader
✔ Icon Packs
✔ IA Icon Resolver
✔ Personalización usuario

====================================================================
"""


class NavigationIcons:

    """
    Gestor central de iconografía.
    """

    # ---------------------------------------------------------

    def __init__(self):

        self.icons = {

            # Sistema

            "dashboard":
                "icons/dashboard.svg",

            "home":
                "icons/home.svg",

            "settings":
                "icons/settings.svg",


            # IA

            "ai":
                "icons/ai.svg",

            "ollama":
                "icons/ollama.svg",

            "model":
                "icons/model.svg",


            # Core

            "runtime":
                "icons/runtime.svg",

            "kernel":
                "icons/kernel.svg",

            "memory":
                "icons/memory.svg",

            "knowledge":
                "icons/knowledge.svg",


            # Desarrollo

            "editor":
                "icons/editor.svg",

            "code":
                "icons/code.svg",

            "terminal":
                "icons/terminal.svg",


            # Datos

            "database":
                "icons/database.svg",

            "storage":
                "icons/storage.svg",


            # Empresa

            "users":
                "icons/users.svg",

            "projects":
                "icons/projects.svg",

            "cloud":
                "icons/cloud.svg",


            # Seguridad

            "security":
                "icons/security.svg",

            "lock":
                "icons/lock.svg"

        }


        self.default_icon = (

            "icons/default.svg"

        )


    # ---------------------------------------------------------

    def register(

        self,

        name,

        path

    ):

        """
        Registra un nuevo icono.
        """

        self.icons[name] = path


    # ---------------------------------------------------------

    def remove(

        self,

        name

    ):

        if name in self.icons:

            del self.icons[name]


    # ---------------------------------------------------------

    def icon(

        self,

        name

    ):

        """
        Obtiene ruta del icono.
        """

        return self.icons.get(

            name,

            self.default_icon

        )


    # ---------------------------------------------------------

    def exists(

        self,

        name

    ):

        return name in self.icons


    # ---------------------------------------------------------

    def all(

        self

    ):

        return self.icons


    # ---------------------------------------------------------

    def module_icon(

        self,

        module_id

    ):

        """
        Resolver icono según módulo.
        """

        return self.icon(

            module_id

        )


    # ---------------------------------------------------------

    def status(self):

        return {

            "component":

                "Navigation Icons",

            "icons":

                len(self.icons),

            "default":

                self.default_icon

        }


navigation_icons = NavigationIcons()
