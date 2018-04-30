import enum
import sys
import logging
import re
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
#import wbn.insights


class EventSource(enum.Enum):
    undefined = -1
    obs_selection_changed = 1
    obs_current_row_changed = 2
    practice_details = 3
    calendar_selection_changed = 4
    tags = 5


quotes = [
    "We are born of love; Love is our mother - Rumi",
    "Let the beauty of what you love be what you do - Rumi",
    """Fear’s born assuming forcefulness—
see how the people fight!
I’ll tell you how I’m deeply moved,
how I have felt so stirred.

Seeing how people flounder
as fish in little water
attacking one the other
its fearfulness appeared.

Once I wished a place to stay,
but all the world is essenceless,
turmoil in every quarter,
I saw no place secure.

Folks’ never-ending enmity
I saw, took no delight,
but then I saw the hard-to-see,
the dart within the heart.

Affected by this dart
one runs in all directions
but with the dart pulled out
one neither runs nor sinks.
"""
]

class InsightsMainCw(QtWidgets.QWidget):
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

        self.active_message_str = "nothing set yet"

        hbox_l2 = QtWidgets.QHBoxLayout()
        self.setLayout(hbox_l2)

        self.left_panel = QtWidgets.QListWidget()
        self.left_panel.currentRowChanged.connect(self._on_left_panel_row_changed)
        hbox_l2.addWidget(self.left_panel, stretch=1)

        self.central_panel = QtWidgets.QLabel()
        hbox_l2.addWidget(self.central_panel, stretch=4)

        for quote_str in quotes:
            self.left_panel.addItem(quote_str[:30])


        #self.diary_panel = wbn.habits.diary_panel.DiaryPanelCw()
        #hbox_l2.addWidget(self.diary_panel)




        #hbox_l2.addStretch(1)

        self.update_gui()

    def update_gui(self, i_event_source=EventSource.undefined):
        self.central_panel.setText(self.active_message_str)

    def _on_left_panel_row_changed(self, i_new_current_row: int):
        self.active_message_str = quotes[i_new_current_row]
        self.update_gui()

