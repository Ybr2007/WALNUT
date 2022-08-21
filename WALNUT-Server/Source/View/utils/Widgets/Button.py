from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PIL import ImageQt, Image

class Button(QPushButton):
    def __init__(self, parent: QWidget = None, 
                       text: str = '<p style="font-size:12pt;font-family:Microsoft Yahei;">MenuBtn</p>',
                       icon:Image.Image = None,
                       iconSize: QSize = QSize(20, 20)
                    ):
        super().__init__(parent)
        self.imgLabel = QLabel()
        self.imgLabel.setPixmap(ImageQt.toqpixmap(icon)) if icon is not None else ...
        self.imgLabel.setScaledContents(True)
        self.imgLabel.setFixedSize(iconSize)
        self.textLabel = QLabel(text)
        self.textLabel.setWordWrap(True)
        l = QHBoxLayout()
        l.addWidget(self.imgLabel)
        l.addSpacing(10)
        l.addWidget(self.textLabel)
        l.addSpacing(30)
        self.setLayout(l)