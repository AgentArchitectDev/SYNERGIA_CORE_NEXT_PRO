"""
====================================================================
SYNERGIA OMEGA UI
Navigation Builder V6 Enterprise
====================================================================

Construye dinámicamente la navegación del Control Center.

NO toma decisiones.

NO administra estado.

NO conoce lógica del sistema.

Su única responsabilidad es construir la interfaz de navegación
a partir del Module Registry.

====================================================================
"""

from collections import defaultdict

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
)

from gui.navigation.navigation_manager import navigation_manager


class NavigationBuilder(QWidget):
    """
    Constructor visual de la navegación.
    """

    def __init__(self):

        super().__init__()

        self.layout = QVBoxLayout()

        self.layout.setAlignment(Qt.AlignTop)

        self.layout.setSpacing(4)

        self.layout.setContentsMargins(
            8,
            8,
            8,
            8
        )

        self.buttons = {}

        self.categories = {}

        self.setLayout(self.layout)

    # =====================================================

    def clear(self):

        while self.layout.count():

            item = self.layout.takeAt(0)

            widget = item.widget()

            if widget:

                widget.deleteLater()

        self.buttons.clear()

        self.categories.clear()

    # =====================================================

    def build(self):

        self.clear()

        registry = navigation_manager.registry

        if registry is None:

            return

        grouped = defaultdict(list)

        modules = sorted(

            registry.modules.values(),

            key=lambda m: m.get("order", 999)

        )

        for module in modules:

            if not module.get("enabled", True):

                continue

            if not module.get("visible", True):

                continue

            category = module.get(

                "category",

                "general"

            )

            grouped[category].append(module)

        for category, module_list in grouped.items():

            self.create_category(category)

            for module in module_list:

                self.create_button(module)

        self.layout.addStretch()

    # =====================================================

    def create_category(self, name):

        title = QLabel(name.upper())

        title.setObjectName("navigationCategory")

        self.layout.addWidget(title)

        self.categories[name] = title

    # =====================================================

    def create_button(self, module):

        button = QPushButton(

            module["title"]

        )

        button.setCursor(Qt.PointingHandCursor)

        button.setMinimumHeight(34)

        button.clicked.connect(

            lambda _, mid=module["id"]:

                navigation_manager.open(mid)

        )

        self.layout.addWidget(button)

        self.buttons[module["id"]] = button

    # =====================================================

    def refresh(self):

        self.build()

    # =====================================================

    def enable(self, module_id):

        if module_id in self.buttons:

            self.buttons[module_id].setEnabled(True)

    # =====================================================

    def disable(self, module_id):

        if module_id in self.buttons:

            self.buttons[module_id].setEnabled(False)

    # =====================================================

    def highlight(self, module_id):

        for mid, button in self.buttons.items():

            if mid == module_id:

                button.setProperty(

                    "selected",

                    True

                )

            else:

                button.setProperty(

                    "selected",

                    False

                )

            button.style().unpolish(button)

            button.style().polish(button)

    # =====================================================

    def status(self):

        return {

            "builder": "Navigation Builder V6",

            "buttons": len(self.buttons),

            "categories": len(self.categories)

        }


navigation_builder = NavigationBuilder()
