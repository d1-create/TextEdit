from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

import pathlib
import os 
#save a string to a file if it is allowed to save and a file is open
def SaveStrToFile(current_path:str,text_to_write:str,is_file_open:bool,can_save:bool):
    if((is_file_open==True) and (can_save==True)):
        file = open(current_path,"w")
        file.write(text_to_write)
        file.close()
    else:
        Show_Basic_Error_Dialog("A file must be open to save it!")

#save file as new one as long as text data is not empty
def Save_File_As(text_to_write:str,current_file_path:str,current_file_name:str,is_file_open:bool):
    print(text_to_write)
    file = None
    filedialogresult = QFileDialog.getSaveFileName(None,'Save File As',str(pathlib.Path.home()))
    
    current_file_path = filedialogresult[0]
    
    file = open(current_file_path,'w')
    print(text_to_write)
    file.write(text_to_write)
    
    is_file_open = True
    current_file_name = os.path.basename(current_file_path)
    
    file.close()

#show error
def Show_Basic_Error_Dialog(message:str):
    error_dialog = QErrorMessage()
    error_dialog.showMessage(message)
    error_dialog.exec()