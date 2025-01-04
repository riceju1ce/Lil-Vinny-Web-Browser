import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui

class LilVinnyBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100,100, 1000, 1000)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))
        self.setCentralWidget(self.browser)

        navbar = QToolBar()
        self.addToolBar(navbar)

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Insert URL here for mommy...")
        navbar.addWidget(self.url_bar)


        back_button = QPushButton("Back")
        forward_button = QPushButton("Forward")
        refresh_button = QPushButton("Refresh")

        back_button.clicked.connect(self.browser.back)
        forward_button.clicked.connect(self.browser.forward)
        refresh_button.clicked.connect(self.browser.reload)

        navbar.addWidget(self.url_bar)
        navbar.addWidget(back_button)
        navbar.addWidget(forward_button)
        navbar.addWidget(refresh_button)

def main():
    app = QApplication(sys.argv)
    QApplication.setApplicationName("Lil Vinny Web Browser")
    window = LilVinnyBrowser()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()