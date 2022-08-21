import tkinter as tk
import tkinter.messagebox as messagebox
import os

from PyQt5.QtWidgets import QApplication  # 导入QApplication类
from PyQt5.QtCore import Qt

from Source.BaseLayer import BaseLayer  # 导入基类
from Source.Debug.Log import AutoLogError, LogHelper, LogType  # 导入日志记录类
import Source.Data.Asset as Asset  # 导入资源
import Source.Data.Setting as Setting  # 导入设置


class Controller(BaseLayer):
    '''
    控制层
    '''
    @AutoLogError
    def __init__(self):
        super().__init__()

        tk_ = tk.Tk()
        tk_.withdraw()

        def LogErrMsgBox(msg):
            messagebox.showerror(
                msg[0], msg[1] + '\n具体错误信息已经记录在Log.log中，请联系作者解决')
            #os._exit(-1)

        LogHelper.logSignal.connect(LogErrMsgBox)  # 连接错误日志信号

        QApplication.setHighDpiScaleFactorRoundingPolicy(
            Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # 确保标题栏的图片显示正常

        Asset.Init()  # 加载资源
        Setting.Init()  # 加载设置

        from Source.View.View import View  # 导入视图层

        self.app = QApplication([])  # 创建QApplication实例

        self.view = View(self)

        exitValue = self.app.exec_()  # 运行QApplication实例

        Setting.setting.Save()

        os._exit(exitValue)  # 退出程序
