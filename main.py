
from PyQt6 import uic
from PyQt6.QtCore import Qt, QPointF, QRectF
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtWidgets import QApplication, QWidget


class YellowCircles(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadui()