from PyQt5.QtWidgets import QVBoxLayout, QFrame, QWidget
from PyQt5.QtCore import pyqtSignal

from src.utils.view_type import ViewType
from src.widgets.icon_button import IconButton


class Sidebar(QFrame):
    clicked = pyqtSignal(ViewType)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Sidebar")
        self.init_UI()

    def init_UI(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 20, 5, 20)
        layout.setSpacing(15)

        button_styles = (
            "#IconButton {padding: 8px 6px; border-radius: 6px; border: none;}"
            "#IconButton:hover {background-color: #475569;}"
        )

        # Menu button
        menuButton = IconButton("assets/icons/menu.svg", size=(22, 22))
        menuButton.clicked.connect(lambda: self.clicked.emit(ViewType.CHATS))
        menuButton.setStyleSheet(button_styles)

        # Top buttons container
        top_button_widget = QFrame(self)
        top_button_layout = QVBoxLayout(top_button_widget)
        top_button_layout.setContentsMargins(0, 0, 0, 0)
        top_button_layout.setSpacing(5)

        # Chats button
        chats_button = IconButton("assets/icons/message-square-text.svg", size=(20, 20))
        chats_button.clicked.connect(lambda: self.clicked.emit(ViewType.CHATS))
        chats_button.setStyleSheet(button_styles)
        top_button_layout.addWidget(chats_button)

        # Calls button
        calls_button = IconButton("assets/icons/phone.svg", size=(20, 20))
        calls_button.clicked.connect(lambda: self.clicked.emit(ViewType.CALLS))
        calls_button.setStyleSheet(button_styles)
        top_button_layout.addWidget(calls_button)

        # Status button
        status_button = IconButton("assets/icons/circle-equal.svg", size=(20, 20))
        status_button.clicked.connect(lambda: self.clicked.emit(ViewType.STATUS))
        status_button.setStyleSheet(button_styles)
        top_button_layout.addWidget(status_button)

        # Middle buttons container
        middle_button_widget = QWidget(self)
        middle_button_widget.setStyleSheet(
            "border-top: 1px solid white;" "border-bottom: 1px solid white;"
        )
        middle_button_layout = QVBoxLayout(middle_button_widget)
        middle_button_layout.setContentsMargins(0, 10, 0, 10)
        middle_button_layout.setSpacing(5)

        # Ask AI button
        ai_button = IconButton("assets/icons/bot-message-square.svg", size=(20, 20))
        ai_button.clicked.connect(lambda: self.clicked.emit(ViewType.AI))
        ai_button.setStyleSheet(button_styles)
        middle_button_layout.addWidget(ai_button)
        middle_button_layout.addStretch()

        # Starred messages button
        starred_messages_button = IconButton("assets/icons/star.svg", size=(20, 20))
        starred_messages_button.clicked.connect(
            lambda: self.clicked.emit(ViewType.STARRED_MESSAGES)
        )
        starred_messages_button.setStyleSheet(button_styles)
        middle_button_layout.addWidget(starred_messages_button)

        # Archive chats button
        archive_button = IconButton("assets/icons/archive.svg", size=(20, 20))
        archive_button.clicked.connect(lambda: self.clicked.emit(ViewType.ARCHIVE))
        archive_button.setStyleSheet(button_styles)
        middle_button_layout.addWidget(archive_button)

        # End buttons container
        end_buttons_widget = QWidget(self)
        end_buttons_layout = QVBoxLayout(end_buttons_widget)
        end_buttons_layout.setContentsMargins(0, 0, 0, 0)
        end_buttons_layout.setSpacing(5)

        # Settings button
        settings_button = IconButton("assets/icons/settings.svg", size=(20, 20))
        settings_button.clicked.connect(lambda: self.clicked.emit(ViewType.SETTINGS))
        settings_button.setStyleSheet(button_styles)
        end_buttons_layout.addWidget(settings_button)

        # Profile button
        profile_button = IconButton("assets/icons/user-pen.svg", size=(20, 20))
        profile_button.clicked.connect(lambda: self.clicked.emit(ViewType.PROFILE))
        profile_button.setStyleSheet(button_styles)
        end_buttons_layout.addWidget(profile_button)

        layout.addWidget(menuButton)
        layout.addWidget(top_button_widget)
        layout.addWidget(middle_button_widget)
        layout.addWidget(end_buttons_widget)

        self.setStyleSheet(
            """
            #Sidebar {
                background-color: #64748B;
            }
            """
        )
