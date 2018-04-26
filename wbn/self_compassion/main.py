import enum
import sys
import logging
import re
import random
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets


compassion_reminder_str_list = [
    "Please be kind to yourself",
    "Look at your mind with compassionate eyes",
    "Is there more you want to say to feel better?",
    "What can i do to feel better?",
    "Is there someone that i can contact to get support?",
    "What can i do long-term to deal with the causes of suffering?",
    "May i hold my suffering with mindfulness and compassion",
    "What other people have had experiences similar to yours?",
    "How would i like to feel today?",
    "What's one small thing i can do to feel better?",
    "How would i like to feel today? What's one small thing i can do go toward this?",
    "What are my needs right now?",
    "Which people in my life are nonjudgemental, compassionate and caring and truly have my well-being in mind?",
    "Which people in my life are nonjudgemental, compassionate and caring and truly have my well-being in mind? How can i spend more time with them?",
    "What's one thing i can do to support myself when i feel anxious, sad or depressed?",
    "What are some physical activities that i enjoy?",
    "Which stories are often playing in my head?",
    "Which stories are often playing in my head? What's one story that i can interpret in a different way?",
    'Which stories are often playing in my head? Can i "translate to giraffe language"? In other words can i see my needs in this situation?',
    "How can i externalize a persistent problem in my life, to reduce blaming?",
    "How can i internalize a persistent problem in my life so that i can do something positive for myself?",
    "What is one feeling that i have had a hard time with?",
    "What's one habit/practice that i can start that can bring more joy/peace into my life",
    "What would i say to someone (that i care about) who is also struggling with the same feelings and problems that i am?",
    "How can i be a caring friend to myself?",
    "What is stopping me from being more kind to myself?",
    "What is stopping me from being more kind to myself? What's one small thing that i can do to start removing this obstacle?",
    "What's one kind thing that i can say to myself when i'm in need of emotional support?",
    "If i loved myself whole heartedly, how would i treat myself each day?",
    "If i loved myself whole heartedly, how would i treat myself each day? What's one small thing i can do like this today?",
    "What can i learn from a recent mistake?",
    "What are my best qualities?",
    "What was the most painful thing that happened to me today?"
]

"""
https://psychcentral.com/blog/25-questions-for-cultivating-self-compassion/
"""


class SelfCompassionMainCw(QtWidgets.QWidget):
    # noinspection PyArgumentList,PyUnresolvedReferences
    def __init__(self):
        super().__init__()

        self.active_message_str = ""

        hbox_l2 = QtWidgets.QHBoxLayout()
        self.setLayout(hbox_l2)

        vbox_l3 = QtWidgets.QVBoxLayout()
        hbox_l2.addLayout(vbox_l3, stretch=1)

        self.encouragement_qlw = QtWidgets.QListWidget()
        self.encouragement_qlw.currentRowChanged.connect(self._on_encouragement_row_changed)
        #for compassion_reminder in compassion_reminder_str_list:
        self.encouragement_qlw.addItems(compassion_reminder_str_list)
        vbox_l3.addWidget(self.encouragement_qlw)
        self.new_random_message_qpb = QtWidgets.QPushButton("Random Message")
        self.new_random_message_qpb.clicked.connect(self.on_new_random_message_clicked)
        vbox_l3.addWidget(self.new_random_message_qpb)


        vbox_l3 = QtWidgets.QVBoxLayout()
        hbox_l2.addLayout(vbox_l3, stretch=3)

        self.inspiring_message_qll = QtWidgets.QLabel()
        self.inspiring_message_qll.setWordWrap(True)
        vbox_l3.addWidget(self.inspiring_message_qll)
        self._show_new_random_inspiring_message()

        self.text_input_cte = PlainTextEdit()
        self.text_input_cte.return_key_released_signal.connect(self.on_text_input_return_key_released)
        vbox_l3.addWidget(self.text_input_cte)

        self.letting_go_qpb = QtWidgets.QPushButton("I let go of my thinking and my suffering")
        self.letting_go_qpb.clicked.connect(self.on_letting_go_clicked)
        vbox_l3.addWidget(self.letting_go_qpb)


        self.update_gui()

    def _on_encouragement_row_changed(self, i_new_current_row: int):
        self.active_message_str = compassion_reminder_str_list[i_new_current_row]
        self.update_gui()

    def on_new_random_message_clicked(self):
        self._show_new_random_inspiring_message()

    def on_text_input_return_key_released(self):
        pass
        #self._show_new_random_inspiring_message()

    def _show_new_random_inspiring_message(self):
        while True:
            new_message_str = random.choice(compassion_reminder_str_list)
            if new_message_str != self.active_message_str:
                break
        self.active_message_str = new_message_str
        self.update_gui()

    def on_letting_go_clicked(self):
        self.text_input_cte.clear()
        self._show_new_random_inspiring_message()

    def update_gui(self):
        self.inspiring_message_qll.setText(self.active_message_str)


class PlainTextEdit(QtWidgets.QPlainTextEdit):
    return_key_released_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

    # overridden
    def keyReleaseEvent(self, i_QKeyEvent):
        if i_QKeyEvent.key() == QtCore.Qt.Key_Enter or i_QKeyEvent.key() == QtCore.Qt.Key_Return:
            self.return_key_released_signal.emit()


