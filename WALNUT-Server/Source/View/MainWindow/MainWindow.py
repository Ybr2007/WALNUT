from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Source.View.utils.FramelessWindow import FramelessWindow
from Source.View.utils.Widgets import *  # 导入自定义控件

class MainWindow(FramelessWindow):
    owner = None
    fadeAnim : QPropertyAnimation

    resizeEvents: list[callable]

    menuWidget: QWidget
    scrollMenu: ScrollArea

    curMainWidgetIndex: int
    mainMainWidgets: list[SubWidget]

    menuTitleLabel: QLabel
    commandMenuBtn: Button
    settingMenuBtn: Button
    
    connectionsList: QTreeWidget
    connectionsTitle: QLabel
    msgTypecomboBox: QComboBox
    commandInputBox: QLineEdit

    isDarkModeSwitch: Switch
    isDarkModeWidget: DescribeWidget

    def __init__(self, owner):...

    def InitWindow(self):...

    def InitUI(self):...

    def InitConnect(self):...
    