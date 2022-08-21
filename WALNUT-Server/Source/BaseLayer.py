from Source.Debug.Log import LogHelper, LogType, AutoLogError  # 导入日志记录类

class BaseLayer:
    '''
    层基类
    '''
    owner : 'BaseLayer'  # 层所有者

    @AutoLogError
    def __init__(self, owner = None):
        self.owner = owner