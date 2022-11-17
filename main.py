import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget
import UI


class Application(QWidget, UI.Ui_Form):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.qp = QPainter()
        self.circles = []
        self.circlesButton.clicked.connect(self.newCircles)

    def paintEvent(self, event):
        self.qp.begin(self)

        for c in self.circles:
            self.qp.setBrush(QColor(*(c[0])))
            self.qp.drawEllipse(*(c[1]))

        self.qp.end()

    def newCircles(self, event):
        for i in range(random.randint(3, 15)):
            r = random.randint(0, 256)
            g = random.randint(0, 256)
            b = random.randint(0, 256)

            x = random.randint(0, 500)
            y = random.randint(0, 500)
            size = random.randint(1, 50)

            self.circles.append(
                (
                    (r, g, b),
                    (
                        x - size / 2,
                        y - size / 2,
                        size,
                        size
                    )
                )
            )

        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    ex.show()
    sys.exit(app.exec())
