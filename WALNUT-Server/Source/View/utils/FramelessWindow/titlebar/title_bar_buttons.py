# coding:utf-8
from PyQt5.QtCore import QSize, Qt, QSize
from PyQt5.QtGui import QColor, QIcon, QPainter, QPen, QPixmap
from PyQt5.QtWidgets import QToolButton

class TitleBarButton(QToolButton):
    """ Title bar button """

    def __init__(self, style: dict = None, parent=None):
        """
        Parameters
        ----------
        style: dict
            button style of `normal`,`hover`, and `pressed`. Each state has
            `color` and `background` attributes.

        parent:
            parent widget
        """
        super().__init__(parent=parent)
        self.setCursor(Qt.ArrowCursor)
        self.setFixedSize(46, 32)
        self.isDarkMode = False

        self._state = 'normal'
        
        self._style = {
            "normal": {
                'color':{
                    'light': (0, 0, 0),
                    'dark': (255, 255, 255)
                },
                'background': (0, 0, 0, 0)
            },
            "hover": {
                "color": (255, 255, 255),
                'background': (0, 100, 182)
            },
            "pressed": {
                "color": (255, 255, 255),
                'background': (54, 57, 65)
            },
        }
        self._style.update(style or {})
        self.setStyleSheet("""
            QToolButton{
                background-color: transparent;
                border: none;
                margin: 0px;
            }
        """)

    def enterEvent(self, e):
        self._state = 'hover'
        self.update()

    def leaveEvent(self, e):
        self._state = 'normal'
        self.update()

    def mousePressEvent(self, e):
        if e.button() != Qt.LeftButton:
            return

        self._state = 'pressed'
        self.update()
        super().mousePressEvent(e)

class MinimizeButton(TitleBarButton):
    """ Minimize button """

    def paintEvent(self, e):
        painter = QPainter(self)

        # draw background
        style = self._style[self._state]
        painter.setBrush(QColor(*style['background']))
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())

        # draw icon
        painter.setBrush(Qt.NoBrush)
        if self._state != 'normal':
            pen = QPen(QColor(*style['color']), 1)
        else:
            pen = QPen(QColor(*style['color']['dark'] if self.isDarkMode else style['color']['light']), 1)
        pen.setCosmetic(True)
        painter.setPen(pen)
        painter.drawLine(18, 16, 28, 16)


class MaximizeButton(TitleBarButton):
    """ Maximize button """

    def __init__(self, style: dict = None, parent=None):
        super().__init__(style, parent)
        self.__isMax = False

    def setMaxState(self, isMax: bool):
        """ update the maximized state and icon """
        if self.__isMax == isMax:
            return

        self.__isMax = isMax
        self.update()

    def paintEvent(self, e):
        painter = QPainter(self)

        # draw background
        style = self._style[self._state]
        painter.setBrush(QColor(*style['background']))
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())

        # draw icon
        painter.setBrush(Qt.NoBrush)
        if self._state != 'normal':
            pen = QPen(QColor(*style['color']), 1)
        else:
            pen = QPen(QColor(*style['color']['dark'] if self.isDarkMode else style['color']['light']), 1)
        pen.setCosmetic(True)
        painter.setPen(pen)

        if not self.__isMax:
            painter.drawRect(18, 11, 10, 10)
        else:
            painter.drawRect(18, 13, 8, 8)
            painter.drawLine(20, 11, 20, 12)
            painter.drawLine(21, 11, 28, 11)
            painter.drawLine(28, 11, 28, 18)
            painter.drawLine(27, 18, 28, 18)


class CloseButton(TitleBarButton):
    """ Close button """

    def __init__(self, style: dict = None, parent=None):
        defaultStyle = {
            "normal": {
                'color':{
                    'light': (0, 0, 0),
                    'dark': (255, 255, 255)
                },
                'background': (0, 0, 0, 0)
            },
            "hover": {
                'color': (255, 255, 255),
                'background': (232, 17, 35)
            },
            "pressed": {
                'color': (255, 255, 255),
                'background': (241, 112, 122)
            },
        }
        defaultStyle.update(style or {})
        super().__init__(defaultStyle, parent)
     
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # draw background
        style = self._style[self._state]
        painter.setBrush(QColor(*style['background']))
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())

        # draw icon
        if self._state != 'normal':
            pen = QPen(QColor(*style['color']), 1)
        else:
            pen = QPen(QColor(*style['color']['dark'] if self.isDarkMode else style['color']['light']), 1)
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawLine(0.4 * self.rect().width(),
                         0.35 * self.rect().height(),
                         0.6 * self.rect().width(),
                         0.65 * self.rect().height(),
                        )
        painter.drawLine(0.6 * self.rect().width(),
                         0.35 * self.rect().height(),
                         0.4 * self.rect().width(),
                         0.65 * self.rect().height(),
                        )
        painter.end()