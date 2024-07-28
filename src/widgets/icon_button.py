from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon, QPainter, QColor, QPixmap
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtSvg import QSvgRenderer


class IconButton(QPushButton):
    def __init__(
        self,
        icon_path: str,
        size: tuple[int, int] = (24, 24),
        color: str = "white",
        parent=None,
    ):
        super().__init__(parent)
        self.setObjectName("IconButton")
        self.icon_path = icon_path
        self.icon_size = size
        self.color = color
        self.init_UI()

    def init_UI(self):
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                border: none;
            }
        """
        )
        self.update_icon()

    def update_icon(self):
        if self.icon_path.lower().endswith("svg"):
            self.setIcon(self.color_svg_icon())
        else:
            self.setIcon(QIcon(self.icon_path))
        self.setIconSize(QSize(*self.icon_size))

    def color_svg_icon(self):
        renderer = QSvgRenderer(self.icon_path)
        pixmap = QPixmap(*self.icon_size)
        pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), QColor(self.color))
        painter.end()

        return QIcon(pixmap)
