from PyQt5.QtWidgets import QMainWindow, QPushButton


class MakeUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.setFixedSize(550, 550)
        self.parent.setWindowTitle("окружности")

        self.parent.create_circle = QPushButton("Добавить круг", self.parent)
        self.parent.create_circle.setGeometry(250, 460, 91, 31)