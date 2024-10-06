#import default necessities for pyside6
from PySide6.QtWidgets import QMainWindow,QApplication

from data import MAIN_DATA_STORE
import sys

#modules
from ui.main_window import Ui_MainWindow#import the ui

from modules.menufunc import *
from modules.scrollbarfunc import *

#the main class for the whole application
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        Ui_MainWindow.setupUi(self,self)
        self.InputText.setPlainText("")#fix this happening on startup
        #setup scrollbars
        self.linenumsb = self.LineNum.verticalScrollBar()
        self.textinputsb = self.InputText.verticalScrollBar()
        self.linenumsb.setVisible(False)

        #other functions
        self.SetupStyling()
        self.SetupMenu()
        self.SetupFunctionality()
    #setup the menu (toolbar,shortcuts,actions,etc)
    def SetupMenu(self):
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave_As.setShortcut("Ctrl+Shift+S")
        self.actionExit.setShortcut("Ctrl+X")
    #setup other signals and slots (other than menubar)
    def SetupFunctionality(self):
        self.InputText.textChanged.connect(lambda: self.UpdateText())
        self.textinputsb.valueChanged.connect(lambda: SyncroniseScrollBars(self.linenumsb,self.textinputsb))
        #menu stuff
        self.actionSave.triggered.connect(lambda:SaveToFile())
        self.actionExit.triggered.connect(lambda:sys.exit())
        self.actionSave_As.triggered.connect(lambda: Save_File_As())
    #setup styling
    def SetupStyling(self):
        self.InputText.setFont(MAIN_DATA_STORE.main_font)
        self.InputTextContainer.layout().setSpacing(0)

        self.LineNum.setDisabled(True)
        self.LineNum.ensureCursorVisible()
        self.LineNum.setFont(MAIN_DATA_STORE.main_font)

    #literally just update the text in main.py to overcome a tiny bug
    def UpdateText(self):
        old_sb_value = self.linenumsb.value()

        MAIN_DATA_STORE.text_data = self.InputText.toPlainText()
        MAIN_DATA_STORE.text_chars = len(MAIN_DATA_STORE.text_data)
        MAIN_DATA_STORE.text_words = len(MAIN_DATA_STORE.text_data.split())
        MAIN_DATA_STORE.text_lines = len(MAIN_DATA_STORE.text_data.splitlines())

        #update label values
        self.chars_label.setText(f"Chars: {str(MAIN_DATA_STORE.text_chars)}")
        self.words_label.setText(f"Words: {str(MAIN_DATA_STORE.text_words)}")
        #update lines
        temp_line_str = ""
        line_arr = list(range(0,MAIN_DATA_STORE.text_lines))
        for i in line_arr:
            temp_line_str += str((i+1)) + "\n"
        self.LineNum.setPlainText(temp_line_str)
        self.linenumsb.setValue(old_sb_value)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
