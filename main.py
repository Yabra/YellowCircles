import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.qp = QPainter()
        self.circles = []
        uic.loadUi('UI.ui', self)
        self.circlesButton.clicked.connect(self.newCircles)

    def paintEvent(self, event):
        self.qp.begin(self)
        self.qp.setBrush(QColor(255, 255, 0))

        for c in self.circles:
            self.qp.drawEllipse(*c)

        self.qp.end()

    def newCircles(self, event):
        for i in range(random.randint(3, 15)):
            x = random.randint(0, 500)
            y = random.randint(0, 500)
            size = random.randint(1, 50)

            self.circles.append(
                (
                    x - size / 2,
                    y - size / 2,
                    size,
                    size
                )
            )

        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    ex.show()
    sys.exit(app.exec())
