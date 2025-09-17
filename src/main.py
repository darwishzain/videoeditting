from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QHBoxLayout,QLabel,QLineEdit,QMainWindow, QPushButton, QVBoxLayout, QWidget
import json,os,sys
from datetime import datetime


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.loadconfig()
        self.setWindowTitle(self.config['name']+' v'+self.config['version'])
        self.showMaximized()

        self.layout = QVBoxLayout()
        self.newproject = QHBoxLayout()

        self.newproject_input = QLineEdit()
        self.newproject_input.setPlaceholderText("New Project Name")
        self.newproject.addWidget(self.newproject_input)
        self.newproject_button = QPushButton("New")
        self.newproject_button.clicked.connect(self.addproject)
        self.newproject.addWidget(self.newproject_button)
        self.layout.addLayout(self.newproject)

        self.projectlist = QVBoxLayout()
        self.projectlist.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout.addLayout(self.projectlist)
        self.refreshprojectlist()
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def loadconfig(self):
        self.config = {}
        with open('config.json', 'r') as f:
            config = json.load(f)
        self.config = config

    def clearcontent(self,layout):
        if layout is None:
            return

        while layout.count():
            item = layout.takeAt(0)

            # If the item is a widget
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

            # If the item is a layout
            child_layout = item.layout()
            if child_layout is not None:
                self.clearcontent(child_layout)

            # If the item is a spacer
            spacer = item.spacerItem()
            if spacer is not None:
                # No explicit delete needed, just let Python GC handle it
                del spacer

    def refreshprojectlist(self):
        self.clearcontent(self.projectlist)
        for project in os.listdir(self.config['settings']['studio']):
            button = QPushButton(project)
            self.projectlist.addWidget(button)

    def addproject(self):
        name = self.newproject_input.text()
        now = datetime.now()
        today = now.strftime("%d-%m-%Y")
        if name == "":
            return
        path = os.path.join(self.config['settings']['editting'],name+'_'+today)
        os.mkdir(path)
        for folder in self.config['settings']['folders']:
            os.mkdir(os.path.join(path,folder))
        self.newproject_input.setText("")
        self.refreshprojectlist()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()