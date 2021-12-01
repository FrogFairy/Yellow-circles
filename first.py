import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class MyPillow(QMainWindow):
    def __init__(self):
        try:
            super().__init__()
            uic.loadUi('желтые круги.ui', self)
            self.setFixedSize(497, 376)
            self.button.clicked.connect(self.run)
            self.do_paint = False
        except Exception as e:
            print(e)

    def run(self):
        self.paint()

    def paintEvent(self, event):
        try:
            if self.do_paint:
                qp = QPainter()
                qp.begin(self)
                self.draw(qp)
                qp.end()
        except Exception as e:
            print(e)

    def paint(self):
        try:
            self.do_paint = True
            self.repaint()
        except Exception as e:
            print(e)

    def draw(self, qp):
        try:
            qp.setBrush(QColor('yellow'))
            a = randint(1, 376)
            qp.drawEllipse(randint(0, 497), randint(0, 376), a, a)
        except Exception as e:
            print(e)


def main():
    app = QApplication(sys.argv)
    win = MyPillow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()