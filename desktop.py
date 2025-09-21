import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QUrl, QTimer
from config import Config

class Browser(QMainWindow):
    def __init__(self, url):
        super().__init__()
        self.setWindowTitle("mcps3rtm")
        self.setWindowIcon(QIcon("wwwroot/static/img/logo512.png"))

        screen = QApplication.primaryScreen()
        screen_size = screen.size()
        width = screen_size.width() * 2 // 3 #2/3rds
        height = screen_size.height() * 2 // 3
        self.resize(width, height)

        self.move(
            (screen_size.width() - width) // 2,
            (screen_size.height() - height) // 2
        )

        self.webview = QWebEngineView()
        self.webview.setUrl(QUrl(url))
        self.setCentralWidget(self.webview)

        self.webview.loadFinished.connect(self.on_load_finished)

        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start(5000)

    def on_load_finished(self, success):
        self.timer.stop()

    def on_timeout(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Load Error")
        msg.setText("Page did not load in time.\nPerhaps the port is in use?")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.buttonClicked.connect(lambda _: sys.exit())
        msg.exec()

def run_desktop():
    app = QApplication(sys.argv)
    browser = Browser(f"http://localhost:{Config.get("server.port")}")
    browser.show()
    sys.exit(app.exec())