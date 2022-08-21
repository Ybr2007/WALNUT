from PyQt5.QtCore import QObject, pyqtSignal  # 只有继承QObject才能使用信号槽
import threading
from .Utils import *
from Source.BaseLayer import BaseLayer  # 导入基类
from Source.Debug.Log import AutoLogError, LogInfo  # 导入日志记录类
from Source.Data.Setting import setting


class Logic(QObject, BaseLayer):
    clientConnectSignal = pyqtSignal(str, bool)
    clientRecvSignal = pyqtSignal(str, str)

    @AutoLogError
    def __init__(self, owner):
        super().__init__(owner=owner)

        from Source.View.View import View  # 导入视图层

        self.owner: View

        self.connectionDict: dict[str, socket.socket] = {}

        self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_.bind(('本机内网穿透IP', '本机内网穿透端口'))
        self.socket_.listen(5)

    @AutoLogError
    def __DealConnect(self, connection: socket.socket):
        msg = GetMsg(connection)
        if msg == 'Client':
            SendMsg(connection, 'Server')
            name = str(len(self.connectionDict))
            self.clientConnectSignal.emit(name, True)
            self.connectionDict[name] = connection

            getMode = False

            while True:
                msg = connection.recv(1024)

                if msg == b'':
                    self.clientConnectSignal.emit(name, False)
                    del self.connectionDict[name]
                    break
                elif msg == b'CMDERR':
                    self.clientRecvSignal.emit(name, '命令执行错误')
                elif msg == b'GETERR':
                    self.clientRecvSignal.emit(name, '获取文件错误')
                elif msg == b'GETSTART':
                    getMode = True
                elif msg == b'GETEND':
                    getMode = False
                elif getMode:
                    with open(r'./Data/file.get', 'ab') as f:
                        f.write(msg)


    @AutoLogError
    def __DealConnectLoop(self):
        while True:
            conn, addr = self.socket_.accept()
            LogInfo(f'{addr} 接入连接')

            threading.Thread(target=self.__DealConnect, args=(conn,)).start()

    @AutoLogError
    def StartDealConnect(self):
        threading.Thread(target=self.__DealConnectLoop).start()

    @AutoLogError
    def Send(self, connectionNames: list[str], cmd: str):
        for connectionName in connectionNames:
            self.connectionDict[connectionName].send(cmd.encode('GB2312'))
