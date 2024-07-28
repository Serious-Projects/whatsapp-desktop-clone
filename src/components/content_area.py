from PyQt5.QtWidgets import QStackedWidget

from src.utils.view_type import ViewType
from src.views.ai_view import AIPage
from src.views.archive_view import ArchivePage
from src.views.calls_view import CallsPage
from src.views.chats_view import ChatsPage
from src.views.profile import ProfilePage
from src.views.settings import SettingsPage
from src.views.starred_messages_view import StarredMessagesPage
from src.views.status_view import StatusPage


class ContentArea(QStackedWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.pages = {
            ViewType.AI: AIPage(),
            ViewType.ARCHIVE: ArchivePage(),
            ViewType.CALLS: CallsPage(),
            ViewType.CHATS: ChatsPage(),
            ViewType.PROFILE: ProfilePage(),
            ViewType.SETTINGS: SettingsPage(),
            ViewType.STARRED_MESSAGES: StarredMessagesPage(),
            ViewType.STATUS: StatusPage(),
        }

        self.init_UI()

    def init_UI(self):
        self.setContentsMargins(0, 0, 0, 0)

        for _, view in self.pages.items():
            self.addWidget(view)
