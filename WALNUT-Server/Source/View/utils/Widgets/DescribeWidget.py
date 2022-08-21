from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class DescribeWidget(QWidget):
    def __init__(self, parent = None, text = '', widget = None, spacing = 200):
        super(DescribeWidget, self).__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.hLayout = QHBoxLayout()
        self.setLayout(self.hLayout)

        self.describeText = QLabel(text)
        self.describeText.setStyleSheet('font-size:20px;font-family:"Microsoft Yahei"')
        self.hLayout.addWidget(self.describeText, alignment=Qt.AlignLeft)

        self.hLayout.addSpacing(spacing)

        self.widget = widget
        if self.widget is not None:
            self.hLayout.addWidget(self.widget, alignment=Qt.AlignRight)
