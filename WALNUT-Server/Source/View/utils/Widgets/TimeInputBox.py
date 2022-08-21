from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class IntInputBox(QLineEdit):
    '''
    只能输入整数的输入框
    '''
    lastValue = ''
    def __init__(self, parent = None, minValue = None, maxValue = None, defaultValue = None):
        super(IntInputBox, self).__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("QLineEdit{border:1px solid #ccc;border-radius:5px;padding:0px 5px;}")

        if minValue is not None:
            self.minValue = minValue
        if maxValue is not None:
            self.maxValue = maxValue
        if defaultValue is not None:
            self.setText(str(defaultValue))
        self.lastValue = self.text()

        self.textChanged.connect(self._textChanged)

    def _textChanged(self, a0: str) -> None:
        try:
            if a0 == '':
                self.lastValue = ''
                return
            value = int(self.text())
            if self.minValue is not None and value < self.minValue:
                self.setText(self.lastValue)
            if self.maxValue is not None and value > self.maxValue:
                self.setText(self.lastValue)
            self.lastValue = self.text()
        except:
            self.setText(self.lastValue)

class TimeInputBox(QWidget):
    def __init__(self, parent = None):
        super(TimeInputBox, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.hLayout = QHBoxLayout()
        self.setLayout(self.hLayout)

        self.hourInputBox = IntInputBox(self, 0, 23, 0)
        self.hLayout.addWidget(self.hourInputBox)
        self.hourText = QLabel('时')
        self.hourText.setFixedSize(QSize(30, 30))
        self.hourText.setStyleSheet('background-color:transparent;color:#333;font-size:20px;')
        self.hLayout.addWidget(self.hourText)

        self.minuteInputBox = IntInputBox(self, 0, 59, 0)
        self.hLayout.addWidget(self.minuteInputBox)
        self.minuteText = QLabel('分')
        self.minuteText.setFixedSize(QSize(30, 30))
        self.minuteText.setStyleSheet('background-color:transparent;color:#333;font-size:20px;')
        self.hLayout.addWidget(self.minuteText)
        
        self.secondInputBox = IntInputBox(self, 0, 59, 0)
        self.hLayout.addWidget(self.secondInputBox)
        self.secondText = QLabel('秒')
        self.secondText.setFixedSize(QSize(30, 30))
        self.secondText.setStyleSheet('background-color:transparent;color:#333;font-size:20px;')
        self.hLayout.addWidget(self.secondText)

        self.setFixedSize(self.hLayout.sizeHint())

    def getSecond(self):
        hour = int(self.hourInputBox.text()) if self.hourInputBox.text() != '' else 0
        minute = int(self.minuteInputBox.text()) if self.minuteInputBox.text() != '' else 0
        second = int(self.secondInputBox.text()) if self.secondInputBox.text() != '' else 0
        return hour * 3600 + minute * 60 + second
