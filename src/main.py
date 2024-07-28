import sys
from PyQt5.QtWidgets import QApplication

from src.views.main_view import MainView


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(
        """
        * {
            margin: 0;
            padding: 0;
            border: 0;
            font-size: 100%;
            font: inherit;
            background-color: transparent;
        }

        /* Set base font */
        QWidget {
            font-size: 14px;
        }

        /* Reset specific widget styles */
        QPushButton {
            border: none;
        }
    """
    )

    main_view = MainView()
    main_view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
