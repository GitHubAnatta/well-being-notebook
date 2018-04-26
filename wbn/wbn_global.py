import logging
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets


class Label(QtWidgets.QLabel):
    def __init__(self, i_text="", i_word_wrap:bool=False, i_point_size:int=None, i_italics:bool=False, i_bold:bool=False):
        super().__init__(i_text)

        self.setWordWrap(i_word_wrap)

        new_font = self.font()
        if i_point_size:
            new_font.setPointSize(i_point_size)
        new_font.setItalic(i_italics)
        new_font.setBold(i_bold)
        self.setFont(new_font)


