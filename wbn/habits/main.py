import enum
import sys
import logging
import re
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import wbn.habits.selection_panel
import wbn.habits.central_panel
import wbn.habits.rem_diary_panel


class EventSource(enum.Enum):
    undefined = -1
    obs_selection_changed = 1
    obs_current_row_changed = 2
    practice_details = 3
    calendar_selection_changed = 4
    tags = 5


class HabitsMainCw(QtWidgets.QWidget):
    """
    The main window of the application
    Suffix explanation:
    _w: widget
    _l: layout
    _# (number): The level in the layout stack
    """
    # noinspection PyArgumentList,PyUnresolvedReferences
    def __init__(self):
        super().__init__()

        hbox_l2 = QtWidgets.QHBoxLayout()
        self.setLayout(hbox_l2)

        self.habits_panel = wbn.habits.selection_panel.SelectionPanelCw()
        hbox_l2.addWidget(self.habits_panel)

        self.central_panel = wbn.habits.central_panel.CentralPanelCw()
        hbox_l2.addWidget(self.central_panel)

        #self.diary_panel = wbn.habits.diary_panel.DiaryPanelCw()
        #hbox_l2.addWidget(self.diary_panel)




        #hbox_l2.addStretch(1)

        self.update_gui()

    def update_gui(self, i_event_source=EventSource.undefined):
        pass
