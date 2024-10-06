from dataclasses import dataclass
from PySide6.QtGui import QFont

@dataclass
class Data:
    #constants
    TEXTBOLDNESS:int = 500
    TEXTSIZE:int = 10
    TEXTFONT:str = "Comic Sans"
    #vars made of constants
    main_font = QFont(TEXTFONT,TEXTSIZE,TEXTBOLDNESS)
    #data
    text_data:str = ""
    line_data:str = ""#string to put next to main textbox to show line number
    text_chars:int = 0
    text_words:int = 0
    text_lines:int = 0
    #file stuff
    file_path:str = "None"

MAIN_DATA_STORE = Data()
