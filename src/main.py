from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import json,sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.loadconfig()
        self.setWindowTitle(self.config['name']+' v'+self.config['version'])

        layout = QVBoxLayout()


        self.button = QPushButton("Click Me")
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    def loadconfig(self):
        self.config = {}
        with open('config.json', 'r') as f:
            config = json.load(f)
        self.config = config
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()