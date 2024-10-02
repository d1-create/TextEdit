from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

#all functions to update the text or do something about the qtextbox's
def UpdateText(MainTextBox:QPlainTextEdit,LineNumTextBox:QPlainTextEdit,text_data:str,text_chars:int,text_words:int,text_lines:int,char_label:QLabel,word_label:QLabel):
    
    def UpdateLineCount(LineNumTextBox:QPlainTextEdit,text_data:str):
        temp_line_str = ""
        line_arr = list(range(0,text_lines))
        for i in line_arr:
            temp_line_str += str(i) + "\n"
            
        LineNumTextBox.setPlainText(temp_line_str)
        
    text_data = MainTextBox.toPlainText()
    text_chars = len(text_data)
    text_words = len(text_data.split())
    text_lines = len(text_data.splitlines())
    
    #update label values
    char_label.setText(str(text_chars))
    word_label.setText(str(text_words))
    #update lines
    
    UpdateLineCount(LineNumTextBox,text_data)
            
