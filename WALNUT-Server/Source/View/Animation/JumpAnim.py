from PyQt5.QtCore import *
from Source.Debug.Log import AutoLogError  # 自动记录错误日志

@AutoLogError
def GetJumpOutAnim(widget, duration = 500, direction: int = 1):
    """
    创建切出动画
    """
    anim = QPropertyAnimation(widget, b"pos")
    anim.setDuration(duration)
    anim.setStartValue(QPoint(300, 0))
    anim.setEndValue(QPoint(300, widget.height() * direction / abs(direction)))
    anim.setEasingCurve(QEasingCurve.Type.InOutQuint)
    anim.finished.connect(lambda: widget.hide())
    return anim

@AutoLogError
def GetJumpInAnim(widget, duration = 500, direction: int = 1):
    """
    创建切入动画
    """
    anim = QPropertyAnimation(widget, b"pos")
    anim.setDuration(duration)
    anim.setStartValue(QPoint(300, -widget.height() * direction / abs(direction)))
    anim.setEndValue(QPoint(300, 0))
    anim.setEasingCurve(QEasingCurve.Type.InOutQuint)

    return anim