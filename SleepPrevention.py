import sys
import ctypes
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer

class SleepPreventionApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the app UI
        self.initUI()

        # Initialize system-specific settings
        self.prevent_sleeping = False

    def initUI(self):
        # Set up the main window
        self.setWindowTitle('Sleep Prevention App')
        self.setGeometry(300, 300, 300, 150)

        # Create the layout
        layout = QVBoxLayout()

        # Add the status label
        self.status_label = QLabel('Sleep Prevention is OFF', self)
        layout.addWidget(self.status_label)

        # Add the toggle button
        self.toggle_button = QPushButton('Start Sleep Prevention', self)
        self.toggle_button.clicked.connect(self.toggle_sleep_prevention)
        layout.addWidget(self.toggle_button)

        # Set layout to the window
        self.setLayout(layout)

        # System tray icon
        self.tray_icon = QSystemTrayIcon(QIcon('icon.png'), self)
        self.tray_icon.setToolTip('Sleep Prevention App')
        self.tray_icon.activated.connect(self.toggle_sleep_prevention)
        tray_menu = QMenu()
        quit_action = QAction('Quit', self)
        quit_action.triggered.connect(self.quit_app)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def toggle_sleep_prevention(self):
        if self.prevent_sleeping:
            self.prevent_sleeping = False
            self.status_label.setText('Sleep Prevention is OFF')
            self.toggle_button.setText('Start Sleep Prevention')
            self.allow_sleep()
        else:
            self.prevent_sleeping = True
            self.status_label.setText('Sleep Prevention is ON')
            self.toggle_button.setText('Stop Sleep Prevention')
            self.prevent_sleep()

    def prevent_sleep(self):
        if sys.platform.startswith('win'):
            # Windows: Use ctypes to call SetThreadExecutionState
            ctypes.windll.kernel32.SetThreadExecutionState(
                0x80000000 | 0x00000001 | 0x00000002)  # ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
        elif sys.platform == 'darwin':
            # macOS: Use subprocess to call 'caffeinate'
            self.prevent_process = subprocess.Popen(['caffeinate'])
        elif sys.platform.startswith('linux'):
            # Linux: Use subprocess to call 'xdg-screensaver' and 'xset'
            self.prevent_process = subprocess.Popen(['xset', 's', 'off', '-dpms'])

    def allow_sleep(self):
        if sys.platform.startswith('win'):
            # Windows: Revert to default sleep settings
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)  # ES_CONTINUOUS
        elif sys.platform in ('darwin', 'linux'):
            if hasattr(self, 'prevent_process') and self.prevent_process:
                self.prevent_process.terminate()
                self.prevent_process = None

    def quit_app(self):
        self.allow_sleep()
        QApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SleepPreventionApp()
    ex.show()
    sys.exit(app.exec_())
