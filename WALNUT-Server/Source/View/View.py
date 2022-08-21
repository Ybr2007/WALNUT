from Source.BaseLayer import BaseLayer  # 导入基类
from Source.Debug.Log import AutoLogError  # 导入日志记录类
from Source.Controller.Controller import Controller  # 导入控制层
from .MainWindow import MainWindow  # 导入主窗口类
import Source.Data.Asset as Asset  # 导入资源
from Source.Data.Setting import setting  # 导入设置

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class View(BaseLayer):
    @AutoLogError
    def __init__(self, owner):
        super().__init__(owner)

        self.owner: Controller

        from Source.Logic.Logic import Logic  # 导入逻辑层

        self.logic = Logic(self)  # 初始化逻辑层
        self.mainWindow = MainWindow(self)  # 创建主窗口

        self.isDarkMode = setting.isDarkMode
        self.owner.app.setStyleSheet(
            Asset.assetDict['Dark.qss' if self.isDarkMode else 'Light.qss'])
        self.mainWindow.SetDarkModeTitleBar(self.isDarkMode)

        self.mainWindow.show()

    @AutoLogError
    def setDarkMode(self, b: bool):
        self.isDarkMode = b
        self.owner.app.setStyleSheet(
            Asset.assetDict['Dark.qss' if self.isDarkMode else 'Light.qss'])
        self.mainWindow.SetDarkModeTitleBar(self.isDarkMode)
