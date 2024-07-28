from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt


class AIPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_UI()

    def init_UI(self):
        self.setStyleSheet("background-color: #1E293B;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        text = QLabel("Ask AI Page")
        text.setStyleSheet(
            "color: white; text-transform: uppercase; letter-spacing: 2px;"
        )
        text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(text)
