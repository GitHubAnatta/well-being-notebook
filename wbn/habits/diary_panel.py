import logging
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets


diary_entry_str_list = ["Gratitude", "Difficulty", "-"]


class DiaryPanelCw(QtWidgets.QWidget):
    # noinspection PyArgumentList,PyUnresolvedReferences
    def __init__(self):
        super().__init__()

        self.setMaximumWidth(400)
        self.setMinimumWidth(200)

        vbox_l2 = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_l2)
        vbox_l2.addWidget(QtWidgets.QLabel("<h3>Diary</h3>"))

        for diary_entry_str in diary_entry_str_list:
            diary_entry_qll = QtWidgets.QLabel(diary_entry_str)
            vbox_l2.addWidget(diary_entry_qll)

        vbox_l2.addStretch(1)

        self.update_gui()

    def update_gui(self):
        pass

