"""
====================================================================
SYNERGIA OMEGA UI
Navigation Category V6 Enterprise
====================================================================

Widget de categoría para el Navigation Framework.

Responsabilidades:

✔ Agrupar módulos
✔ Expandir / Colapsar
✔ Gestionar botones
✔ Mostrar cantidad de módulos
✔ Preparado para IA
✔ Preparado para Plugins
✔ Preparado para Temas

Versión:
    V6 Enterprise

====================================================================
"""

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)

from gui.navigation.navigation_button import NavigationButton


class NavigationCategory(QWidget):
    """
    Categoría del Navigation Framework.
    """

    # -----------------------------------------------------

    def __init__(self, title: str):

        super().__init__()

        self.title = title

        self.expanded = True

        self.buttons = []

        self.build_ui()

    # -----------------------------------------------------

    def build_ui(self):

        self.main_layout = QVBoxLayout()

        self.main_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        self.main_layout.setSpacing(2)

        # -------------------------------------------------
        # Header
        # -------------------------------------------------

        self.header = QWidget()

        header_layout = QHBoxLayout()

        header_layout.setContentsMargins(
            8,
            6,
            8,
            6
        )

        self.arrow = QLabel("▼")

        self.arrow.setFixedWidth(18)

        self.title_label = QLabel(
            self.title.upper()
        )

        self.count_label = QLabel("(0)")

        header_layout.addWidget(self.arrow)

        header_layout.addWidget(self.title_label)

        header_layout.addStretch()

        header_layout.addWidget(self.count_label)

        self.header.setLayout(header_layout)

        # -------------------------------------------------
        # Container
        # -------------------------------------------------

        self.container = QWidget()

        self.container_layout = QVBoxLayout()

        self.container_layout.setContentsMargins(
            18,
            0,
            0,
            0
        )

        self.container_layout.setSpacing(2)

        self.container.setLayout(
            self.container_layout
        )

        # -------------------------------------------------

        self.main_layout.addWidget(self.header)

        self.main_layout.addWidget(self.container)

        self.setLayout(self.main_layout)

    # -----------------------------------------------------

    def mousePressEvent(self, event):

        self.toggle()

        super().mousePressEvent(event)

    # -----------------------------------------------------

    def add_button(self, button: NavigationButton):

        self.buttons.append(button)

        self.container_layout.addWidget(button)

        self.update_counter()

    # -----------------------------------------------------

    def remove_button(self, module_id):

        for button in self.buttons[:]:

            if button.module_id == module_id:

                self.buttons.remove(button)

                button.setParent(None)

                button.deleteLater()

        self.update_counter()

    # -----------------------------------------------------

    def clear(self):

        for button in self.buttons:

            button.setParent(None)

            button.deleteLater()

        self.buttons.clear()

        self.update_counter()

    # -----------------------------------------------------

    def update_counter(self):

        self.count_label.setText(

            f"({len(self.buttons)})"

        )

    # -----------------------------------------------------

    def toggle(self):

        self.expanded = not self.expanded

        self.container.setVisible(

            self.expanded

        )

        self.arrow.setText(

            "▼" if self.expanded else "▶"

        )

    # -----------------------------------------------------

    def expand(self):

        if not self.expanded:

            self.toggle()

    # -----------------------------------------------------

    def collapse(self):

        if self.expanded:

            self.toggle()

    # -----------------------------------------------------

    def button_count(self):

        return len(self.buttons)

    # -----------------------------------------------------

    def status(self):

        return {

            "title": self.title,

            "expanded": self.expanded,

            "buttons": len(self.buttons)

        }

    # -----------------------------------------------------

    def info(self):

        return self.status()
