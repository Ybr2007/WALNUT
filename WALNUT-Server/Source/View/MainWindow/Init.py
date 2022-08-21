from .MainWindow import MainWindow
from Source.Debug.Log import AutoLogError  # 自动记录错误日志

@AutoLogError
def __init__(self : MainWindow, owner):
    super(MainWindow, self).__init__()
    
    self.owner = owner
    self.resizeEvents = []

    self.InitWindow()
    self.InitUI()
    self.InitConnect()


MainWindow.__init__ = __init__