from PyQt5.QtCore import QObject, pyqtSignal  # 只有继承QObject才能使用信号槽
import time  # 记录Log时间
import traceback  # 记录错误
from enum import Enum  # 定义日志类型

logFilePath = './Log.log'


class LogType(Enum):
    Info = 'Info'
    Warning = 'Warning'
    Error = 'Error'


class __Log(QObject):
    '''
    记录日志
    '''
    logSignal = pyqtSignal(tuple)

    def Log(self, message: tuple[LogType, str]) -> None:
        '''
        记录日志
        message : tuple[LogType, str]  日志信息
        '''
        message = (message[0].value, message[1])
        localTime = time.localtime()  # 获取本地时间
        # 格式化时间(yyyy-mm-dd hh:mm:ss)
        logTime = time.strftime('%Y-%m-%d %H:%M:%S', localTime)

        with open(logFilePath, 'a', encoding='utf-8') as f:  # 写入日志文件
            f.write(logTime + ',' + message[0] + '\n' + message[1] + '\n\n')

        if message[0] == LogType.Error.value:
            self.logSignal.emit(message)  # 发送信号


LogHelper = __Log()


def AutoLogError(f):
    '''
    自动捕获并记录·
    '''
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            msg = str(traceback.format_exc())
            LogHelper.Log(
                (LogType.Error, msg)
            )
    return wrapper


def LogInfo(msg: str):
    LogHelper.Log(
        (LogType.Info, msg)
    )
