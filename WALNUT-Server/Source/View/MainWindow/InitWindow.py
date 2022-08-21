from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PIL import ImageQt

from .MainWindow import MainWindow
from Source.Debug.Log import AutoLogError  # 导入日志记录类
import Source.Data.Setting as Setting  # 导入设置
import Source.Data.Asset as Asset  # 导入资源
import Source.Data.Info as Info  # 导入信息
from Source.View.Animation.FadeAnim import GetFadeInAnim, GetFadeOutAnim  # 导入渐入动画


@AutoLogError
def InitWindow(self : MainWindow):
    self.setMinimumSize(600, 400)
    self.setGeometry(*Setting.setting.windowGeometry)  # 设置窗口大小和位置（与上次退出时一致）
    self.setWindowTitle(Info.AppName)
    self.setWindowIcon(QIcon(ImageQt.toqpixmap(Asset.assetDict['Icon.png'])))

    self.fadeAnim = GetFadeInAnim(self)  # 创建渐入动画
    self.fadeAnim.start()  # 启动动画


    @AutoLogError
    def __resizeEvent(event):
        super(MainWindow, self).resizeEvent(event)

    @AutoLogError
    def __closeEvent(event):
        # 不记录最大化窗口的位置和尺寸
        if not self.isMaximized():
            Setting.setting.windowGeometry = (
                self.x(), self.y(), self.width(), self.height())
            Setting.setting.Save()

        event.ignore()  # 忽略事件

        self.fadeAnim = GetFadeOutAnim(self)  # 创建渐出动画
        self.fadeAnim.start()  # 启动动画
        self.fadeAnim.finished.connect( self.owner.owner.app.quit)  # 结束后退出应用程序

    self.resizeEvents.append(__resizeEvent)
    self.closeEvent = __closeEvent

    

MainWindow.InitWindow = InitWindow