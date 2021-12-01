import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic

class Design(QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.setGeometry(300, 300, 497, 376)
        self.setFixedSize(497, 376)
        self.button = QPushButton(self)
        self.button.setText('Нарисовать круги')
        self.button.setGeometry(170, 140, 141, 41)


class MyPillow(Design):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.button.clicked.connect(self.run)
        self.do_paint = False

    def run(self):
        self.paint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        a = randint(1, 376)
        qp.drawEllipse(randint(0, 497), randint(0, 376), a, a)


def main():
    app = QApplication(sys.argv)
    win = MyPillow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()