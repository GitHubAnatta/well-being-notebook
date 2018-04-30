import enum
import sys
import logging
import re
import random
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import wbn.self_compassion.main
import wbn.habits.main
import wbn.insights.main


class MainWindow(QtWidgets.QMainWindow):
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
        self.setGeometry(40, 30, 1100, 600)

        central_w1 = QtWidgets.QWidget()
        self.setCentralWidget(central_w1)
        hbox_l2 = QtWidgets.QHBoxLayout()
        central_w1.setLayout(hbox_l2)

        self.stacked_widget = QtWidgets.QStackedWidget()
        hbox_l2.addWidget(self.stacked_widget, stretch=5)

        right_panel_vbox_l3 = QtWidgets.QVBoxLayout()
        hbox_l2.addLayout(right_panel_vbox_l3, stretch=1)

        button_row_vbox_l4 = QtWidgets.QVBoxLayout()
        right_panel_vbox_l3.addLayout(button_row_vbox_l4)

        # Adding the individual parts of the notebook

        button_row_vbox_l4.addStretch(1)

        self.self_compassion_journal = wbn.self_compassion.main.SelfCompassionMainCw()
        self.stacked_widget.addWidget(self.self_compassion_journal)
        self.self_compassion_journal_qpb = QtWidgets.QPushButton("Self-compassion")
        self.self_compassion_journal_qpb.clicked.connect(self._on_self_compassion_clicked)
        button_row_vbox_l4.addWidget(self.self_compassion_journal_qpb)

        self.schedule = wbn.habits.main.HabitsMainCw()
        self.stacked_widget.addWidget(self.schedule)
        self.schedule_qpb = QtWidgets.QPushButton("Schedule")
        self.schedule_qpb.clicked.connect(self._on_schedule_clicked)
        button_row_vbox_l4.addWidget(self.schedule_qpb)

        self.insights = wbn.insights.main.InsightsMainCw()
        self.stacked_widget.addWidget(self.insights)
        self.insights_qpb = QtWidgets.QPushButton("Insights")
        self.insights_qpb.clicked.connect(self._on_insights_clicked)
        button_row_vbox_l4.addWidget(self.insights_qpb)

        self.gratitude = wbn.insights.main.InsightsMainCw()
        self.stacked_widget.addWidget(self.gratitude)
        self.gratitude_qpb = QtWidgets.QPushButton("Gratitude")
        self.gratitude_qpb.clicked.connect(self._on_gratitude_clicked)
        button_row_vbox_l4.addWidget(self.gratitude_qpb)

        #TODO: If something has been done for one of the tabs, show it in bold face, or some other difference


        #gratitude
        #quotes and insights

        self.shared_text_box_qpte = QtWidgets.QPlainTextEdit()
        self.shared_text_box_qpte.setPlaceholderText("Text notes")
        right_panel_vbox_l3.addWidget(self.shared_text_box_qpte)
        # buttons: copy, clear

        hbox_l4 = QtWidgets.QHBoxLayout()
        right_panel_vbox_l3.addLayout(hbox_l4)
        self.copy_qpb = QtWidgets.QPushButton("Copy")
        hbox_l4.addWidget(self.copy_qpb)
        self.clear_qpb = QtWidgets.QPushButton("Clear")
        hbox_l4.addWidget(self.clear_qpb)

        self.search_qle = QtWidgets.QLineEdit()
        # self.search_qle.textChanged.connect(self.on_search_text_changed)  # textEdited
        self.search_qle.setPlaceholderText("Search")
        right_panel_vbox_l3.addWidget(self.search_qle)

        self.hashtags_composite = QtWidgets.QListWidget()
        self.hashtags_composite.addItems(["Item 1", "List item 2", "3"])
        right_panel_vbox_l3.addWidget(self.hashtags_composite)

        button_row_vbox_l4.addStretch(1)

    def _on_self_compassion_clicked(self):
        self.stacked_widget.setCurrentIndex(0)

    def _on_schedule_clicked(self):
        self.stacked_widget.setCurrentIndex(1)

    def _on_insights_clicked(self):
        self.stacked_widget.setCurrentIndex(2)

    def _on_gratitude_clicked(self):
        self.stacked_widget.setCurrentIndex(3)

    def update_gui(self):
        pass
