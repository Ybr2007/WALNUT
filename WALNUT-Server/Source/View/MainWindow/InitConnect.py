from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .MainWindow import MainWindow
from Source.Debug.Log import AutoLogError  # 导入日志记录类
from Source.Data.Setting import setting  # 导入设置


@AutoLogError
def InitConnect(self: MainWindow):
    @AutoLogError
    def __resizeEvent(event):
        for func in self.resizeEvents:
            func(event)

    self.resizeEvent = __resizeEvent

    @AutoLogError
    def __jumpTo(index: int):
        if index == self.curMainWidgetIndex:
            return

        if self.curMainWidgetIndex > index:
            self.mainMainWidgets[self.curMainWidgetIndex].jumpOut()
            self.mainMainWidgets[index].jumpIn()
        else:
            self.mainMainWidgets[self.curMainWidgetIndex].jumpOut(-1)
            self.mainMainWidgets[index].jumpIn(-1)

        self.curMainWidgetIndex = index

    self.commandMenuBtn.pressed.connect(lambda: __jumpTo(0))
    self.settingMenuBtn.pressed.connect(lambda: __jumpTo(1))

    @AutoLogError
    def __AddConnectionName(name: str, b: bool):
        if b:
            item = QTreeWidgetItem(self.connectionsList)
            item.setText(0, name)
        else:
            for i in range(self.connectionsList.topLevelItemCount()):
                child = self.connectionsList.topLevelItem(i)

                if child.text(0) == name:
                    self.connectionsList.takeTopLevelItem(i)

    self.owner.logic.StartDealConnect()
    self.owner.logic.clientConnectSignal.connect(__AddConnectionName)

    @AutoLogError
    def __OnUnitViewItemClicked():
        if len(self.connectionsList.selectedItems()) == 0:
            self.commandInputBox.setVisible(False)
        else:
            self.commandInputBox.setVisible(True)

    self.connectionsList.itemSelectionChanged.connect(__OnUnitViewItemClicked)

    @AutoLogError
    def __OnCmdInputBoxReturnPressed():
        connectionNames = [item.text(0) for item in self.connectionsList.selectedItems()]


        cmdTypeStrDict = {'命令': 'CMD ', '消息': 'MSG ','获取': 'GET ', '退出': 'EXIT'}
        cmdTypeStr = cmdTypeStrDict[self.msgTypecomboBox.currentText()]

        self.owner.logic.Send(connectionNames, cmdTypeStr + self.commandInputBox.text())
        self.commandInputBox.clear()

    self.commandInputBox.returnPressed.connect(__OnCmdInputBoxReturnPressed)


    @AutoLogError
    def __OnIsDarkModeSwitchClicked(b):
        self.owner.setDarkMode(b)
        setting.isDarkMode = b


    self.isDarkModeSwitch.clicked.connect(__OnIsDarkModeSwitchClicked)

    @AutoLogError
    def __ClientRecv(name: str, msg: str):
        QMessageBox.information(self, name, msg)


    self.owner.logic.clientRecvSignal.connect(__ClientRecv)


MainWindow.InitConnect = InitConnect
