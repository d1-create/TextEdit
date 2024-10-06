from PySide6.QtWidgets import QScrollBar

def SyncroniseScrollBars(ScrollBarA:QScrollBar,ScrollBarB:QScrollBar):
    ScrollBarA.setValue(ScrollBarB.value())
