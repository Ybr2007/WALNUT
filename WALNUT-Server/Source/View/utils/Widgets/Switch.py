from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtGui import *


class Switch(QWidget):
    clicked = pyqtSignal(bool)

    def __init__(self, parent=None, size=QSize(140, 60)):
        super(Switch, self).__init__(parent)

        self.__isCicked = False
        self.__circlePos = int(self.height() * 0.2)
        self.anim = QPropertyAnimation(self, b"circlePos", self)
        self.anim.setDuration(500)
        self.anim.setEasingCurve(QEasingCurve.OutCubic)

        self.__backgroundColor = QColor(255, 255, 255, 255)
        self.__fontColor = QColor(0, 0, 0, 255)

    def resizeEvent(self, a0: QResizeEvent) -> None:
        super().resizeEvent(a0)
        if self.__isCicked:
            self.__circlePos = self.width() - self.height()
        else:
            self.__circlePos = int(self.height() * 0.2)

    def getCirclePos(self):
        return self.__circlePos

    def setCirclePos(self, pos):
        self.__circlePos = pos

    circlePos = pyqtProperty(int, getCirclePos, setCirclePos)

    def getIsClicked(self):
        return self.__isCicked

    def setIsClicked(self, b):
        self.__isCicked = b

    isClicked = pyqtProperty(bool, getIsClicked, setIsClicked)

    def getBgColor(self):
        return self.__backgroundColor

    def setBgColor(self, color):
        self.__backgroundColor = color

    backgroundColor = pyqtProperty(QColor, getBgColor, setBgColor)

    def getFontColor(self):
        return self.__fontColor

    def setFontColor(self, color):
        self.__fontColor = color

    fontColor = pyqtProperty(QColor, getFontColor, setFontColor)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        self.__isCicked = not self.__isCicked

        self.clicked.emit(self.__isCicked)

        if self.anim.state() == QPropertyAnimation.Running:
            self.anim.stop()

        if self.__isCicked:
            self.anim.setStartValue(self.__circlePos)
            self.anim.setEndValue(self.width() - self.height())
        else:
            self.anim.setStartValue(self.__circlePos)
            self.anim.setEndValue(self.height() * 0.2)

        self.anim.setDirection(QAbstractAnimation.Forward)
        self.anim.valueChanged.connect(self.update)
        self.anim.start()

    def setClicked(self, b: bool):
        self.__isCicked = b

        self.clicked.emit(self.__isCicked)

        if self.anim.state() == QPropertyAnimation.Running:
            self.anim.stop()

        if self.__isCicked:
            self.anim.setStartValue(self.__circlePos)
            self.anim.setEndValue(self.width() - self.height())
        else:
            self.anim.setStartValue(self.__circlePos)
            self.anim.setEndValue(self.height() * 0.2)

        self.anim.setDirection(QAbstractAnimation.Forward)
        self.anim.valueChanged.connect(self.update)
        self.anim.start()

    def paintEvent(self, a0: QPaintEvent) -> None:
        super(Switch, self).paintEvent(a0)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setBrush(QBrush(self.__backgroundColor))
        painter.setPen(QPen(self.__backgroundColor, 0))
        painter.drawRoundedRect(
            1, 1, 
            self.width() - 2, self.height() - 2,
            self.height() / 2, self.height() / 2
        )

        painter.setBrush(QBrush(self.__fontColor))
        painter.setPen(QPen(self.__fontColor, 0))
        painter.drawEllipse(
            self.circlePos, int(self.height() * 0.1) + 1, 
            int(self.height() * 0.8) - 1, int(self.height() * 0.8 - 1)
        )
