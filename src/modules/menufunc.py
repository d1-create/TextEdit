from PySide6.QtWidgets import QErrorMessage,QFileDialog

import pathlib
import os

from data import MAIN_DATA_STORE as Data
#save a string to a file if it is allowed to save and a file is open
def SaveToFile():
    print(Data.file_path)
    print(Data.text_data)
    if(Data.file_path!="None" and Data.text_data!=""):
        with open(Data.file_path,"w") as file:
            file.write(Data.text_data)
    else:
        Show_Basic_Error_Dialog("A file must be open to save it!")

#save file as new one as long as text data is not empty
def Save_File_As():
    filedialogresult = QFileDialog.getSaveFileName(None,'Save File As',str(pathlib.Path.home()))

    Data.file_path = filedialogresult[0]

    with open(Data.file_path,'w') as file:
        file.write(Data.text_data)

    is_file_open = True

#show error
def Show_Basic_Error_Dialog(message:str):
    error_dialog = QErrorMessage()
    error_dialog.showMessage(message)
    error_dialog.exec()
