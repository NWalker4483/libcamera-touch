from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import QRect

class RoundButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(100, 100)
        self.setObjectName("RoundButton")
        self.pressed.connect(self.playSound)

    def paintEvent(self, event):
        painter = QPainter(self)

        if self.isDown():
            painter.setPen(QColor(255, 0, 0, 255))
            painter.setBrush(QBrush(QColor(255, 0, 0, 255)))
        else:
            painter.setPen(QColor(255, 255, 255, 128))
            painter.setBrush(QBrush(QColor(255, 255, 255, 128)))

        painter.drawEllipse(QRect(0, 0, self.width(), self.height()))

        inner_radius = 20
        inner_rect = QRect(self.width() // 2 - inner_radius, self.height() // 2 - inner_radius,
                           inner_radius * 2, inner_radius * 2)
        painter.drawEllipse(inner_rect)

    def playSound(self):
        print("Play shutter sound")