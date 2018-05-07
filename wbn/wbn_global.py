import logging
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets


DATABASE_FILE_STR = "wbn_db_file.db"


class Label(QtWidgets.QLabel):
    def __init__(self, i_id: int=-1, i_text: str="", i_word_wrap: bool=False, i_point_size: int=None, i_italics: bool=False, i_bold: bool=False):
        super().__init__(i_text)

        self.id_int = i_id

        self.setWordWrap(i_word_wrap)

        new_font = self.font()
        if i_point_size:
            new_font.setPointSize(i_point_size)
        new_font.setItalic(i_italics)
        new_font.setBold(i_bold)
        self.setFont(new_font)


db_file_exists_at_application_startup_bl = False


NO_PHRASE_SELECTED_INT = -1


class CustomQLabel(QtWidgets.QLabel):
    entry_id = NO_PHRASE_SELECTED_INT  # -"static"

    def __init__(self, i_text_sg, i_entry_id=NO_PHRASE_SELECTED_INT):
        super().__init__(i_text_sg)
        self.entry_id = i_entry_id


def get_database_filename():
    return DATABASE_FILE_STR


