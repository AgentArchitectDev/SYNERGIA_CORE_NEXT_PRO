"""
====================================================================
SYNERGIA OMEGA UI
Navigation Button V6 Enterprise
====================================================================

Widget nativo del Navigation Framework.

Reemplaza QPushButton dentro del Sidebar/Navigation.

Preparado para:

✔ Iconos SVG
✔ Badges
✔ Favoritos
✔ Temas
✔ Hover
✔ Selección
✔ IA
✔ Plugins
✔ Notificaciones

Versión:
    V6 Enterprise

====================================================================
"""

from PySide6.QtCore import Qt, Signal

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QSizePolicy,
)


class NavigationButton(QWidget):
    """
    Botón inteligente del Navigation Framework.
    """

    clicked = Signal(str)

    # ---------------------------------------------------------

    def __init__(
        self,
        module_id: str,
        title: str,
        icon: str = "",
        tooltip: str = "",
        category: str = "general"
    ):

        super().__init__()

        self.module_id = module_id

        self.title = title

        self.icon = icon

        self.tooltip = tooltip

        self.category = category

        self.enabled = True

        self.selected = False

        self.favorite = False

        self.badge = ""

        self.build_ui()

    # ---------------------------------------------------------

    def build_ui(self):

        self.setCursor(Qt.PointingHandCursor)

        self.setMinimumHeight(38)

        self.setMaximumHeight(38)

        self.setSizePolicy(

            QSizePolicy.Expanding,

            QSizePolicy.Fixed

        )

        self.layout = QHBoxLayout()

        self.layout.setContentsMargins(

            10,

            0,

            10,

            0

        )

        self.layout.setSpacing(10)

        # -------------------------------------------------

        self.icon_label = QLabel()

        self.icon_label.setFixedWidth(24)

        self.icon_label.setAlignment(

            Qt.AlignCenter

        )

        self.icon_label.setText("•")

        # -------------------------------------------------

        self.title_label = QLabel(

            self.title

        )

        self.title_label.setAlignment(

            Qt.AlignVCenter

        )

        # -------------------------------------------------

        self.badge_label = QLabel()

        self.badge_label.hide()

        self.badge_label.setAlignment(

            Qt.AlignCenter

        )

        self.badge_label.setMinimumWidth(22)

        self.badge_label.setMaximumWidth(30)

        # -------------------------------------------------

        self.layout.addWidget(

            self.icon_label

        )

        self.layout.addWidget(

            self.title_label

        )

        self.layout.addStretch()

        self.layout.addWidget(

            self.badge_label

        )

        self.setLayout(

            self.layout

        )

        if self.tooltip:

            self.setToolTip(

                self.tooltip

            )

    # ---------------------------------------------------------

    def mousePressEvent(self, event):

        if self.enabled:

            self.clicked.emit(

                self.module_id

            )

        super().mousePressEvent(event)

    # ---------------------------------------------------------

    def set_selected(self, value: bool):

        self.selected = value

        self.refresh_style()

    # ---------------------------------------------------------

    def set_enabled(self, value: bool):

        self.enabled = value

        self.setEnabled(value)

        self.refresh_style()

    # ---------------------------------------------------------

    def set_badge(self, value):

        if value in ("", None, 0):

            self.badge = ""

            self.badge_label.hide()

            return

        self.badge = str(value)

        self.badge_label.setText(

            self.badge

        )

        self.badge_label.show()

    # ---------------------------------------------------------

    def set_favorite(self, value: bool):

        self.favorite = value

    # ---------------------------------------------------------

    def refresh_style(self):

        state = []

        if self.selected:

            state.append("selected")

        if not self.enabled:

            state.append("disabled")

        if self.favorite:

            state.append("favorite")

        self.setProperty(

            "state",

            " ".join(state)

        )

        self.style().unpolish(self)

        self.style().polish(self)

    # ---------------------------------------------------------

    def info(self):

        return {

            "id": self.module_id,

            "title": self.title,

            "icon": self.icon,

            "category": self.category,

            "selected": self.selected,

            "favorite": self.favorite,

            "enabled": self.enabled,

            "badge": self.badge

        }

    # ---------------------------------------------------------

    def status(self):

        return self.info()
