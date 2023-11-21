import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPolygon

from make_ui import MakeUI


class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        self.modif = False
        MakeUI(self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 550)
        self.setWindowTitle('Круги')

        self.create_circle.clicked.connect(self.update_draw)

    def update_draw(self):
        self.modif = True
        self.update()

    def paintEvent(self, event):
        if self.modif:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        a = randint(10, 230)
        qp.drawEllipse(290 - a, 240 - a, a * 2, a * 2)
        self.modif = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())

