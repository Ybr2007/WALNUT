from PyQt5.QtCore import *
from Source.Debug.Log import AutoLogError  # 自动记录错误日志   

@AutoLogError
def GetFadeInAnim(widget, duration = 1000):
    """
    创建淡入动画
    """
    anim = QPropertyAnimation(widget, b"windowOpacity")
    anim.setDuration(duration)
    anim.setStartValue(0)
    anim.setEndValue(1)
    return anim

@AutoLogError
def GetFadeOutAnim(widget, duration = 1000):
    """
    创建淡出动画
    """
    anim = QPropertyAnimation(widget, b"windowOpacity")
    anim.setDuration(duration)
    anim.setStartValue(1)
    anim.setEndValue(0)
    return anim