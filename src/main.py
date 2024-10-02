#import default necessities for pyside6
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from PySide6.QtUiTools import *
import sys

#modules
from ui.main_window import Ui_MainWindow#import the ui

from modules.consts import *

from modules.textupdates import *

from modules.menufunc import *
from modules.scrollbarfunc import *

#the main class for the whole application
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        Ui_MainWindow.setupUi(self,self)

        #setup scrollbars
        self.linenumsb = self.LineNum.verticalScrollBar()
        self.textinputsb = self.InputText.verticalScrollBar()
        self.linenumsb.setVisible(False)

        #other functions
        self.SetupVariables()
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
        self.InputText.textChanged.connect(lambda: UpdateText(self.InputText,self.LineNum,self.text_data,self.text_chars,self.text_words,self.text_lines,self.chars_label,self.words_label))
        self.textinputsb.valueChanged.connect(lambda: SyncroniseScrollBars(self.linenumsb,self.textinputsb))
        
        #menu stuff
        self.actionSave.triggered.connect(lambda:SaveStrToFile(self.file_path,self.text_data,self.file_open,self.can_save_normal))
        self.actionExit.triggered.connect(lambda:sys.exit())
        self.actionSave_As.triggered.connect(lambda: Save_File_As(str(self.text_data),self.file_path,self.current_file_name,self.file_open))
    #setup all variables(comments for non-self explanator stuff)
    def SetupVariables(self):

        #vars made of constants
        self.main_font = QFont(TEXTFONT,TEXTSIZE,TEXTBOLDNESS)
        #data
        self.text_data:str = ""
        self.line_data:str = ""#string to put next to main textbox to show line number

        self.text_chars:int = 0
        self.text_words:int = 0
        self.text_lines:int = 0

        #file stuff
        self.can_save_normal:bool = False
        self.file_open:bool = False
        
        self.file_path:str = ""
        self.current_file_name:str = ""
    #setup styling
    def SetupStyling(self):
        self.InputText.setFont(self.main_font)
        self.InputTextContainer.layout().setSpacing(0)

        self.LineNum.setDisabled(True)
        self.LineNum.ensureCursorVisible()
        self.LineNum.setFont(self.main_font)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    app.exec()
