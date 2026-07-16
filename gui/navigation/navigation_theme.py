"""
====================================================================
SYNERGIA OMEGA UI
Navigation Theme Manager V6 Enterprise
====================================================================

Gestor central de estilos del Navigation Framework.

Responsabilidades:

✔ Colores globales
✔ Estilos de botones
✔ Estilos de categorías
✔ Sidebar
✔ Estados:
    - normal
    - hover
    - activo
    - deshabilitado

Preparado para:

✔ OMEGA Themes
✔ JSON Themes
✔ Dark / Light Mode
✔ Personalización usuario
✔ IA adaptativa

====================================================================
"""


class NavigationTheme:

    """
    Motor de temas del Navigation Framework.
    """

    # ---------------------------------------------------------

    def __init__(self):

        self.current_theme = "omega_dark"

        self.themes = {

            "omega_dark": {

                "background": "#121212",

                "sidebar": "#181818",

                "category": "#202020",

                "button": "#252525",

                "button_hover": "#303030",

                "button_active": "#0057ff",

                "text": "#ffffff",

                "text_secondary": "#aaaaaa",

                "border": "#333333"

            },


            "omega_light": {

                "background": "#ffffff",

                "sidebar": "#f4f4f4",

                "category": "#e8e8e8",

                "button": "#ffffff",

                "button_hover": "#dddddd",

                "button_active": "#1976d2",

                "text": "#111111",

                "text_secondary": "#555555",

                "border": "#cccccc"

            }

        }


    # ---------------------------------------------------------

    def set_theme(self, name):

        if name in self.themes:

            self.current_theme = name

            return {

                "status": "changed",

                "theme": name

            }


        return {

            "status": "error",

            "message": "Theme not found"

        }


    # ---------------------------------------------------------

    def get_theme(self):

        return self.themes.get(

            self.current_theme

        )


    # ---------------------------------------------------------

    def get(self, key):

        theme = self.get_theme()

        return theme.get(key)


    # ---------------------------------------------------------

    def sidebar_style(self):

        return f"""

        QWidget {{

            background-color:

            {self.get('sidebar')};

            color:

            {self.get('text')};

        }}

        """


    # ---------------------------------------------------------

    def button_style(self):

        return f"""

        QPushButton {{

            background-color:

            {self.get('button')};

            color:

            {self.get('text')};

            border:

            1px solid {self.get('border')};

            padding:

            6px;

            border-radius:

            5px;

        }}


        QPushButton:hover {{

            background-color:

            {self.get('button_hover')};

        }}


        QPushButton:checked {{

            background-color:

            {self.get('button_active')};

        }}

        """


    # ---------------------------------------------------------

    def category_style(self):

        return f"""

        QWidget {{

            background-color:

            {self.get('category')};

            color:

            {self.get('text')};

        }}

        """


    # ---------------------------------------------------------

    def colors(self):

        return self.get_theme()


    # ---------------------------------------------------------

    def available_themes(self):

        return list(

            self.themes.keys()

        )


    # ---------------------------------------------------------

    def status(self):

        return {

            "component":

                "Navigation Theme",

            "active":

                self.current_theme,

            "available":

                self.available_themes()

        }


navigation_theme = NavigationTheme()
