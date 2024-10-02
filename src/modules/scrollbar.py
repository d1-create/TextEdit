from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


def SyncroniseScrollBars(ScrollBarA:QScrollBar,ScrollBarB:QScrollBar):
    ScrollBarA.setValue(ScrollBarB.value())