from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class ClockWidget(QWidget):
    def __init__(self, parent=None,
                 color1=QColor(0, 0, 0, 255), color2=QColor(255, 255, 255, 255),
                 armWidth=0.03, armLength=0.4,
                 pointNum=4, pointWidth=0.005,
                 centerWidth=0.05,
                 ):
        '''
        注意：参数中的宽度和长度都是相对于圆的直径的比例
        '''
        super(ClockWidget, self).__init__(parent)
        # 设置无边框和背景透明
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.resize(150, 150)
        self.color1 = color1
        self.color2 = color2

        # 比例
        self.__ratio = 0

        # 指针宽度
        self.armWidth = armWidth
        # 指针长度
        self.armLength = armLength

        # 刻度数量
        self.pointNum = pointNum
        # 刻度宽度
        self.pointWidth = pointWidth

        # 圆心宽度
        self.centerWidth = centerWidth

    def setRatio(self, ratio):
        self.__ratio = ratio
        self.update()

    def currentRatio(self):
        return self.__ratio

    def paintEvent(self, a0: QPaintEvent) -> None:
        super().paintEvent(a0)

        # 创建Painter并设置抗锯齿和图片平滑缩放
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing |
                               QPainter.SmoothPixmapTransform)

        if self.width() != self.height():
            _min = min(self.width(), self.height())
            self.resize(_min, _min)

        d = self.width()

        # 绘制圆形背景
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.color1)
        painter.drawEllipse(0, 0, d, d)

        # 绘制指针
        painter.setPen(QPen(self.color2, d * self.armWidth))
        painter.setBrush(Qt.NoBrush)
        painter.save()
        painter.translate(d / 2, d / 2)
        painter.rotate(self.__ratio * 360)
        painter.drawLine(0, 0, 0, int(-d * self.armLength))
        painter.restore()

        # 圆心
        painter.setPen(QPen(self.color2, d * self.centerWidth))
        painter.setBrush(Qt.NoBrush)
        painter.drawPoint(d // 2, d // 2)

        # 绘制刻度(在圆周上平均分割pointNum份)
        painter.setPen(QPen(self.color2, d * self.pointWidth))
        painter.setBrush(Qt.NoBrush)
        painter.save()
        painter.translate(d / 2, d / 2)
        for i in range(self.pointNum):
            painter.rotate(360 / self.pointNum)
            painter.drawLine(int(d * 0.4), 0, int(d * 0.45), 0)
        painter.restore()
