from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath
from PyQt5.QtCore import Qt


def create_rounded_image(label: QLabel, pixmap: QPixmap):
    size = label.size()

    rounded_pixmap = QPixmap(size)
    rounded_pixmap.fill(Qt.GlobalColor.transparent)

    painter = QPainter(rounded_pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)

    path = QPainterPath()
    path.addEllipse(0, 0, size.width(), size.height())

    painter.setClipPath(path)

    scaled_pixmap = pixmap.scaled(
        size,
        Qt.AspectRatioMode.KeepAspectRatio,
        Qt.TransformationMode.SmoothTransformation,
    )

    paint_x = (size.width() - scaled_pixmap.width()) // 2
    paint_y = (size.height() - scaled_pixmap.height()) // 2

    painter.drawPixmap(paint_x, paint_y, scaled_pixmap)
    painter.end()

    label.setPixmap(rounded_pixmap)

    return label
