from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout

from src.components.content_area import ContentArea
from src.components.sidebar import Sidebar
from src.utils.view_type import ViewType


class MainView(QMainWindow):
    def __init__(self):
        super(MainView, self).__init__()
        self.setWindowTitle("WhatsApp Desktop Clone")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        central_widget.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        sidebar = Sidebar(central_widget)
        sidebar.clicked.connect(self.handle_page_change)

        self.pages_widget = ContentArea(self)

        layout.addWidget(sidebar)
        layout.addWidget(self.pages_widget)

    def handle_page_change(self, page_type: ViewType):
        pages = self.pages_widget.pages
        current_view = pages.get(page_type)

        if current_view is not None:
            view_index = self.pages_widget.indexOf(current_view)
            print(f"Changing to view: {page_type.name}, index: {view_index}")
            self.pages_widget.setCurrentIndex(view_index)
        else:
            print(f"View not implemented: {page_type.name}")
