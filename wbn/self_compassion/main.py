import enum
import sys
import logging
import re
import random
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import wbn.self_compassion_model
import wbn.wbn_global


class SelfCompassionMainCw(QtWidgets.QWidget):
    # noinspection PyArgumentList,PyUnresolvedReferences
    def __init__(self):

        super().__init__()

        self.active_message_str = ""
        self.seconds_passed_int = 0

        hbox_l2 = QtWidgets.QHBoxLayout()
        self.setLayout(hbox_l2)

        vbox_l3 = QtWidgets.QVBoxLayout()
        hbox_l2.addLayout(vbox_l3, stretch=1)

        self.encouragement_qlw = QtWidgets.QListWidget()
        self.encouragement_qlw.currentRowChanged.connect(self._on_encouragement_row_changed)
        #for compassion_reminder in compassion_reminder_str_list:
        #self.encouragement_qlw.addItems(compassion_reminder_str_list)
        vbox_l3.addWidget(self.encouragement_qlw)
        self.update_support_list()

        self.new_random_message_qpb = QtWidgets.QPushButton("Random Message")
        self.new_random_message_qpb.clicked.connect(self.on_new_random_message_clicked)
        vbox_l3.addWidget(self.new_random_message_qpb)

        hbox_l4 = QtWidgets.QHBoxLayout()
        vbox_l3.addLayout(hbox_l4)
        self.new_support_phrase_qle = QtWidgets.QLineEdit()
        hbox_l4.addWidget(self.new_support_phrase_qle)

        self.add_new_support_phrase_qpb = QtWidgets.QPushButton("Add")
        self.add_new_support_phrase_qpb.clicked.connect(self.add_new_support_phrase_clicked)
        hbox_l4.addWidget(self.add_new_support_phrase_qpb)

        # Main area

        vbox_l3 = QtWidgets.QVBoxLayout()
        hbox_l2.addLayout(vbox_l3, stretch=3)

        support_hbox_l4 = QtWidgets.QHBoxLayout()
        vbox_l3.addLayout(support_hbox_l4, stretch=3)

        self.support_phrase_qll = wbn.wbn_global.Label(
            i_point_size=16,
            i_word_wrap=True
        )
        support_hbox_l4.addWidget(self.support_phrase_qll)
        self._show_new_random_inspiring_message()

        self.image_qll = QtWidgets.QLabel()
        #self.image_qll.setScaledContents(True)
        self.image_qll.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        #self.image_qll.setMaximumWidth(100)
        pixmap = QtGui.QPixmap("thailand-1571416_640.jpg")
        self.image_qll.setPixmap(pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio))
        # -TODO: also needs to be added to the resize event for the widget that contains the label
        # -more info here: https://stackoverflow.com/a/8212120/2525237
        support_hbox_l4.addWidget(self.image_qll)
        # IDEA: Moving this image closer to the support phrase/question
        # >>>>>IDEA: Having an image for every question/support phrase<<<<<

        hbox_l4 = QtWidgets.QHBoxLayout()
        vbox_l3.addLayout(hbox_l4)


        self.text_input_cte = PlainTextEdit()
        self.text_input_cte.return_key_released_signal.connect(self.on_text_input_return_key_released)
        self.text_input_cte.setPlaceholderText("Please look at yourself with the eyes of compassion")
        new_font = self.text_input_cte.font()
        new_font.setPointSize(14)
        self.text_input_cte.setFont(new_font)
        hbox_l4.addWidget(self.text_input_cte, stretch=3)

        vbox_l5 = QtWidgets.QVBoxLayout()
        hbox_l4.addLayout(vbox_l5, stretch=1)

        feelings_list = ["Body - pleasant", "Body - unpleasant", "Body - neutral", "Mind - pleasant", "Mind - unpleasant", "Mind - neutral"]
        self.feelings_qlw = QtWidgets.QListWidget()
        self.feelings_qlw.addItems(feelings_list)
        vbox_l5.addWidget(self.feelings_qlw, stretch=3)
        # self.feelings_qlw.resize

        mind_list = ["Lust", "Without lust", "Hatred", "Without hatred", "Delusion", "Without delusion", "Contracted", "Distracted", "Exalted", "Unexalted", "Surpassable", "Unsurpassable", "Concentrated", "Unconcentrated", "Liberated", "Unliberated"]
        self.mind_qlw = QtWidgets.QListWidget()
        self.mind_qlw.addItems(mind_list)
        vbox_l5.addWidget(self.mind_qlw, stretch=5)

        hbox_l4 = QtWidgets.QHBoxLayout()
        vbox_l3.addLayout(hbox_l4)

        self.time_passed_qll = QtWidgets.QLabel("Timer not started yet")
        hbox_l4.addWidget(self.time_passed_qll)

        self.next_phrase_qcb = QtWidgets.QComboBox()
        self.next_phrase_qcb.addItems(["Random", "Next", "Prev"])
        # self.next_phrase_qcb.clicked.connect(self.on_next_phrase_activated)
        hbox_l4.addWidget(self.next_phrase_qcb)

        self.letting_go_qpb = QtWidgets.QPushButton("I let go of my thinking and my suffering")
        self.letting_go_qpb.clicked.connect(self.on_letting_go_clicked)
        hbox_l4.addWidget(self.letting_go_qpb)

        self.writing_qelapsedtimer = QtCore.QTimer(self)
        self.writing_qelapsedtimer.timeout.connect(self._writing_timer_timeout)
        self.writing_qelapsedtimer.start(1000)  # -one second # 60 *


        # Right side: Image
        # Design: Alternatively this could be placed on the left side


        self.update_gui()

    def update_support_list(self):
        self.encouragement_qlw.clear()
        for support_phrase in wbn.self_compassion_model.SelfCompassionM.get_all():
            self.encouragement_qlw.addItem(support_phrase.support_phrase[:25])

    def add_new_support_phrase_clicked(self):
        wbn.self_compassion_model.SelfCompassionM.add(
            self.new_support_phrase_qle.text()
        )
        self.update_support_list()

    # noinspection PyAttributeOutsideInit
    def _writing_timer_timeout(self):
        self.seconds_passed_int += 1
        # updating the timer label:
        seconds_int = str(self.seconds_passed_int % 60).zfill(2)
        minutes_int = str(self.seconds_passed_int // 60)
        time_passed_str = minutes_int + ":" + seconds_int
        self.time_passed_qll.setText(time_passed_str)

    def _on_encouragement_row_changed(self, i_new_current_row: int):
        sc_support_phrase = wbn.self_compassion_model.SelfCompassionM.get_all()[i_new_current_row]
        self.active_message_str = sc_support_phrase.support_phrase
        self.update_gui()

    def on_new_random_message_clicked(self):
        self._show_new_random_inspiring_message()

    def on_text_input_return_key_released(self):
        pass
        #self._show_new_random_inspiring_message()

    def _show_new_random_inspiring_message(self):
        if self.encouragement_qlw.count() < 1:
            logging.warning("_show_new_random_inspiring_message: count() < 1")
            return
        while True:
            random_number_from_list_int = random.choice(range(0, self.encouragement_qlw.count()))
            #sc_support_phrase = random.choice(wbn.self_compassion_model.SelfCompassionM.get_all())
            self.encouragement_qlw.setCurrentRow(random_number_from_list_int)

            random_support_phrase = self.get_phrase_for_row_number(random_number_from_list_int)

            # check the vertical sort order

            new_message_str = random_support_phrase.support_phrase
            if new_message_str != self.active_message_str:
                break
        self.active_message_str = new_message_str
        self.update_gui()

    def on_letting_go_clicked(self):
        self.text_input_cte.clear()
        #self.update_db_sort_order_for_all_rows()

        # TODO: Move to top --- self.encouragement_qlw.move

        self._show_new_random_inspiring_message()

    def get_phrase_for_row_number(self, i_row_number: int):
        ret_support_phrase = None
        for support_phrase in wbn.self_compassion_model.SelfCompassionM.get_all():
            if i_row_number == support_phrase.vert_order:
                ret_support_phrase = support_phrase
                break
        return ret_support_phrase


    def update_db_sort_order_for_all_rows(self):
        logging.debug("update_db_sort_order_for_all_rows")
        count = 0
        while count < self.list_widget.count():
            q_list_item_widget = self.list_widget.item(count)
            custom_label = self.list_widget.itemWidget(q_list_item_widget)
            id_int = custom_label.entry_id
            row_int = self.list_widget.row(q_list_item_widget)
            wbn.self_compassion_model.SelfCompassionM.update_sort_order(
                id_int,
                row_int
            )
            logging.debug("id_int = " + str(id_int) + ", row_int = " + str(row_int))
            count += 1

        #self.update_gui()
        #self.update_selected()

    def update_gui(self):
        self.support_phrase_qll.setText(self.active_message_str)


class PlainTextEdit(QtWidgets.QPlainTextEdit):
    return_key_released_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

    # overridden
    def keyReleaseEvent(self, i_QKeyEvent):
        if i_QKeyEvent.key() == QtCore.Qt.Key_Enter or i_QKeyEvent.key() == QtCore.Qt.Key_Return:
            self.return_key_released_signal.emit()


