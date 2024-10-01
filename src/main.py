#import default necessities for pyside6
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from PySide6.QtUiTools import *
import sys

from ui.main_window import Ui_MainWindow#import the ui

#other libs
import pathlib
#the main class for the whole application
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        Ui_MainWindow.setupUi(self,self)

        self.SetupVariables()
        self.SetupStyling()
        self.SetupMenu()
        self.SetupFunctionality()

    #setup the menu (toolbar,shortcuts,actions,ect)
    def SetupMenu(self):
        self.actionSave.setShortcut("Ctrl+Shift+S")
        self.actionSave_As.setShortcut("Ctrl+S")
        self.actionExit.setShortcut("Ctrl+X")

        self.actionExit.triggered.connect(lambda: self.ActionMethods.ExitApplication(app))
        self.actionExit.triggered.connect(lambda: app.exit())
        self.actionSave_As.triggered.connect(lambda: self.SaveAsFunction())

    #setup other signals and slots (other than menubar)
    def SetupFunctionality(self):
        #yes an extra-long function for no reason
        self.TextInput.textChanged.connect(lambda: self.UpdateText())
    #setup all variables     
        self.InputText.textChanged.connect(lambda: self.UpdateText())
    #setup all variables(comments for non-self explanator stuff)
    def SetupVariables(self):
        #constants
        self.TEXTBOLDNESS:int = 500
        self.TEXTSIZE:int = 10
        self.TEXTFONT:str = "Comic Sans"

        #vars made of constants
        self.main_font = QFont(self.TEXTFONT,self.TEXTSIZE,self.TEXTBOLDNESS)
        #data
        self.text_data:str = ""
        self.line_data:str = ""#string to put next to main textbox to show line number

        self.text_chars:int = 0
        self.text_words:int = 0
        self.text_lines:int = 0

        #file stuff
        self.file_open:bool = False
        
        self.file_path:str = ""
        
    #setup styling
    def SetupStyling(self):
        self.TextInput.setFont(self.main_font)
        self.TextInput.setStyleSheet("""margin:0px;padding:0px;""")
        self.InputText.setFont(self.main_font)
        self.InputTextContainer.layout().setSpacing(0)

        self.LineNum.setDisabled(True)
        self.LineNum.ensureCursorVisible()
        self.LineNum.setFont(self.main_font)
    #############SIGNALS AND SLOTS HERE(No need for any actual seperation of code so its a system of comments)#############
    
    class ActionMethods:
        def ExitApplication(app:QApplication):
            app.exit()

    ##UpdateText##
    ##UpdateText(anything to do with updating text)##
    def UpdateText(self):
        self.text_data = self.TextInput.toPlainText()
        self.text_data = self.InputText.toPlainText()
        self.text_lines = len(self.text_data.splitlines())
        self.UpdateLineCount()
        self.GetCharWord()
        self.SetCharWord()
    #GetAndSetCharDetails - ##UpdateText     
    def GetCharWord(self):
        self.text_chars = len(self.text_data)
        self.text_words = len(self.text_data.split())
    def SetCharWord(self):
        self.chars_label.setText(f"Charachters: {str(self.text_chars)}")
        self.words_label.setText(f"Words: {str(self.text_words)}")
    #Update Line Count
    def UpdateLineCount(self):
        self.line_data = ""
        line_arr = list(range(0,int(self.text_lines)))
        for i in line_arr:
            self.line_data += str(i) + "\n"
            
        self.LineNum.setPlainText(self.line_data)

    
        newsb = self.LineNum.verticalScrollBar()
        newsb.setValue(newsb.maximum())
    ##UpdateTextEND##

    ##SAVEBUTTONS START(anything to do with menu)##
    def SaveAsFunction(self):
        pass

    def SaveToFile(self):
        File = open(self.file_path,"w")
        File.write(self.text_data)
        File.close()
    ##SAVEBUTTONS END##
  
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
