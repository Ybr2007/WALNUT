from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Source.View.Animation.JumpAnim import GetJumpInAnim, GetJumpOutAnim

class SubWidget(QWidget):
    def __init__(self, parent=None, hLayout=None, vLayout=None, jumpInAnim=None, jumpOutAnim=None):
        super(SubWidget, self).__init__(parent)

        self.jumpInAnim = GetJumpInAnim(self) if jumpInAnim is None else jumpInAnim
        self.jumpOutAnim = GetJumpOutAnim(self) if jumpOutAnim is None else jumpOutAnim

        self.hLayout = hLayout if hLayout is not None else QHBoxLayout()
        self.vLayout = vLayout if vLayout is not None else QVBoxLayout()

        self.setLayout(self.vLayout)
        self.vLayout.addLayout(self.hLayout)

    def resizeEvent(self, a0: QResizeEvent) -> None:
        super().resizeEvent(a0)

        self.jumpInAnim = GetJumpInAnim(self, self.jumpInAnim.duration())
        self.jumpOutAnim = GetJumpOutAnim(self, self.jumpOutAnim.duration())

    def jumpIn(self, direction: int = 1):
        self.setVisible(True)
        self.jumpInAnim = GetJumpInAnim(self, self.jumpInAnim.duration(), direction)
        self.jumpInAnim.start()

    def jumpOut(self, direction: int = 1):
        self.jumpOutAnim = GetJumpOutAnim(self, self.jumpOutAnim.duration(), direction)
        self.jumpOutAnim.start()
        self.jumpOutAnim.finished.connect(lambda: self.setVisible(False))

    def getIn(self):
        self.move(self.jumpInAnim.endValue())
        self.setVisible(True)


    def getOut(self):
        self.move(self.jumpOutAnim.endValue())
        self.setVisible(False)
