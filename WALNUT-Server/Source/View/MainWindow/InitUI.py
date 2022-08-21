from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .MainWindow import MainWindow
import Source.Data.Asset as Asset  # 导入资源
from Source.Debug.Log import AutoLogError  # 自动记录错误日志
from Source.View.utils.Widgets import *  # 导入自定义控件
from Source.Data.Setting import setting  # 导入设置
import Source.Data.Info as Info  # 导入应用信息

@AutoLogError
def InitUI(self: MainWindow):
    self.menuWidget = QWidget()
    self.menuWidget.setFixedSize(300, 400)
    self.scrollMenu = ScrollArea(self)
    self.scrollMenu.setWidget(self.menuWidget)

    # =============================================================================
    # 菜单UI

    self.menuTitleLabel = QLabel(self.menuWidget)
    self.menuTitleLabel.setText(f'<p style="font-size:16pt;font-family:Microsoft Yahei;font-weight:bold;">{Info.AppName}</p>')
    self.menuTitleLabel.setGeometry(55, 30, 240, 40)

    self.commandMenuBtn = Button(
        self.menuWidget,
        '<p style="font-size:12pt;font-family:Microsoft Yahei;">命令</p>',
        Asset.assetDict['Connect.png']
    )
    self.commandMenuBtn.setObjectName('menuBtn')
    self.commandMenuBtn.setGeometry(30, 140, 240, 40)

    self.settingMenuBtn = Button(
        self.menuWidget,
        '<p style="font-size:12pt;font-family:Microsoft Yahei;">设置</p>',
        Asset.assetDict['Setting.png']
    )
    self.settingMenuBtn.setObjectName('menuBtn')
    self.settingMenuBtn.setGeometry(30, 190, 240, 40)
    # =============================================================================

    self.curMainWidgetIndex = 0
    self.mainMainWidgets = [
        SubWidget(self), # connectWidget
        SubWidget(self), # settingWidget
    ]

    for w in self.mainMainWidgets:
        w.getOut()

    self.mainMainWidgets[0].getIn()

    # =============================================================================
    # 主界面UI

    # 命令界面
    self.mainMainWidgets[0].vLayout.addSpacing(30)

    self.connectionsTitle = QLabel('<p style="font-size:12pt;font-family:Microsoft Yahei;">当前连接</p>')
    self.mainMainWidgets[0].vLayout.addWidget(self.connectionsTitle)

    self.connectionsList = QTreeWidget()
    self.connectionsList.setColumnCount(1)
    self.mainMainWidgets[0].vLayout.addWidget(self.connectionsList)
    # 隐藏行标题
    self.connectionsList.setHeaderHidden(True)
    # 取消滚动条
    self.connectionsList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.connectionsList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    self.msgTypecomboBox = QComboBox()
    self.msgTypecomboBox.setView(QListView())
    self.msgTypecomboBox.addItem('命令')
    self.msgTypecomboBox.addItem('消息')
    self.msgTypecomboBox.addItem('获取')
    self.msgTypecomboBox.addItem('退出')
    self.mainMainWidgets[0].vLayout.addWidget(self.msgTypecomboBox)

    self.commandInputBox = QLineEdit()
    self.commandInputBox.setVisible(False)
    self.mainMainWidgets[0].vLayout.addWidget(self.commandInputBox)

    self.mainMainWidgets[0].vLayout.addStretch()

    # 设置界面
    self.mainMainWidgets[1].vLayout.addSpacing(30)

    self.isDarkModeSwitch = Switch()
    self.isDarkModeSwitch.setClicked(setting.isDarkMode)
    self.isDarkModeSwitch.setFixedSize(60, 30)
    self.isDarkModeWidget = DescribeWidget(
        text='深色模式', widget=self.isDarkModeSwitch)
    self.mainMainWidgets[1].vLayout.addWidget(self.isDarkModeWidget)

    self.mainMainWidgets[1].vLayout.addStretch()
    
    # =============================================================================

    @AutoLogError
    def __resizeWidget(event):
        self.scrollMenu.setGeometry(0, 0, 300, self.height())
        
        if len(self.mainMainWidgets) > self.curMainWidgetIndex:
            self.mainMainWidgets[self.curMainWidgetIndex].setGeometry(
                300, 0, self.width() - 300, self.height())
        for w in self.mainMainWidgets:
            w.resize(self.width() - 300, self.height())

    self.resizeEvents.append(__resizeWidget)

    self.titleBar.raise_()  # 置顶标题栏


MainWindow.InitUI = InitUI
