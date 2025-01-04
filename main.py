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
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        back_button = QPushButton("Back")
        forward_button = QPushButton("Forward")
        refresh_button = QPushButton("Refresh")

        back_button.clicked.connect(self.browser.back)
        forward_button.clicked.connect(self.browser.forward)
        refresh_button.clicked.connect(self.browser.reload)
        self.browser.urlChanged.connect(self.update_url)

        #add widgets to the toolbar
        navbar.addWidget(back_button)
        navbar.addWidget(forward_button)
        navbar.addWidget(refresh_button)
        navbar.addWidget(self.url_bar)

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self):
        self.url_bar.setText(self.browser.url().toString())

def main():
    app = QApplication(sys.argv)
    QApplication.setApplicationName("Lil Vinny Web Browser")
    window = LilVinnyBrowser()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
