from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtSvg import QSvgRenderer


class ImageWidget(QLabel):
    def __init__(
        self,
        image_path: str,
        size: tuple[int, int] = (24, 24),
        color: str = "white",
        parent=None,
    ):
        super().__init__(parent)
        self.image_path = image_path
        self.image_size = size
        self.color = color
        self.init_UI()

    def init_UI(self):
        width, height = self.image_size

        self.setFixedSize(width, height)
        self.setPixmap(QPixmap(self.image_path))
        self.setStyleSheet("padding: 0;")

        if self.image_path.lower().endswith(".svg"):
            self.set_svg_image()
        else:
            self.setPixmap(
                QPixmap(self.image_path).scaled(
                    width,
                    height,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )

    def set_svg_image(self):
        renderer = QSvgRenderer(self.image_path)
        pixmap = QPixmap(self.size())
        pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()

        qcolor = QColor(self.color)
        mask = pixmap.createMaskFromColor(
            Qt.GlobalColor.black, Qt.MaskMode.MaskOutColor
        )
        pixmap.fill(qcolor)
        pixmap.setMask(mask)

        self.setPixmap(pixmap)
