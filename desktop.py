# pyqt6 desktop app for mcps3rtm
# tbwcjw - MIT 2025

import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, QTimer, QProcess
from PyQt6.QtGui import QIcon
from config import Config

port = Config.get("streamlit.port") or 8501
address = Config.get("streamlit.address") or 'localhost'

venv_path = getattr(sys, 'real_prefix', None) or getattr(sys, 'base_prefix', None)
if hasattr(sys, 'base_prefix') and sys.prefix != sys.base_prefix:
    venv_path = sys.prefix
else:
    venv_path = None

py_exec = os.path.join(venv_path, "Scripts" if os.name == "nt" else "bin", "python") if venv_path else sys.executable

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mcps3rtm")
        self.setWindowIcon(QIcon("assets/logo512.png"))
        self.setGeometry(0, 0, 1600, 800)

        self.placeholder = QWidget()
        self.placeholder.setStyleSheet("background-color: rgb(14, 17, 23);")
        self.setCentralWidget(self.placeholder)

        self.browser = QWebEngineView()
        self.browser.loadFinished.connect(self.on_load_finished)

        self.count = 0
        self.max_attempts = 10

        # QProcess for Streamlit
        self.sl_proc = QProcess(self)
        self.sl_proc.readyReadStandardOutput.connect(self.handle_stdout)
        self.sl_proc.readyReadStandardError.connect(self.handle_stderr)
        self.sl_proc.started.connect(lambda: print("streamlit started..."))
        self.sl_proc.finished.connect(lambda code, status: print(f"streamlit exited: code ({code}) {status}"))

        # Start Streamlit
        self.start_streamlit()

    def start_streamlit(self):
        args = [
            "-m", "streamlit", "run", "server.py",
            "--server.headless", "true",
            "--server.address", address,
            "--server.port", str(port)
        ]
        self.sl_proc.start(py_exec, args)
        QTimer.singleShot(500, self.try_load_browser)

    def handle_stdout(self):
        data = self.sl_proc.readAllStandardOutput().data().decode()
        for line in data.splitlines():
            print(line)

    def handle_stderr(self):
        data = self.sl_proc.readAllStandardError().data().decode()
        for line in data.splitlines():
            print("ERR:", line)
            if "Port" in line and "already in use" in line:
                self.show_error_message(
                    title="Error",
                    text="Port in use",
                    informative=f"Port {port} is already in use"
            )

    def try_load_browser(self):
        print("loading browser")
        self.browser.setUrl(QUrl(f"http://{address}:{port}"))

    def on_load_finished(self, ok):
        print("load finished:", ok)
        if not ok and self.count < self.max_attempts:
            self.count += 1
            print(f"Retrying... {self.count}/{self.max_attempts}")
            QTimer.singleShot(500, self.refresh_page)
        elif not ok and self.count >= self.max_attempts:
            self.show_error_message(title="Error", text="Failed to load server",
                                    informative="The server did not respond in time.")
        else:
            self.setCentralWidget(self.browser)

    def refresh_page(self):
        self.browser.reload()

    def show_error_message(self, title, text, informative):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setInformativeText(informative)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
        self.close()

    def closeEvent(self, event):
        print("trminating streamlit...")
        if self.sl_proc.state() != QProcess.ProcessState.NotRunning:
            self.sl_proc.terminate()
            if not self.sl_proc.waitForFinished(3000):
                self.sl_proc.kill()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
