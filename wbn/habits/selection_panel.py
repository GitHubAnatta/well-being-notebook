import logging
import datetime
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import wbn.wbn_global


class SelectionPanelCw(QtWidgets.QWidget):
    # noinspection PyArgumentList,PyUnresolvedReferences
    def __init__(self):
        super().__init__()

        vbox_l2 = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_l2)
        ###vbox_l2.addWidget(QtWidgets.QLabel("<h2>Habits</h2>"))

        situation_subpanel = SituationSubpanelCw()
        vbox_l2.addWidget(situation_subpanel)

        self.schedule_subpanel = ScheduleSubpanelCw()
        vbox_l2.addWidget(self.schedule_subpanel)

        self.habits_subpanel = HabitsSubpanelCw()
        vbox_l2.addWidget(self.habits_subpanel)

        self.update_gui()

    def update_gui(self):
        pass


class SituationSubpanelCw(QtWidgets.QWidget):
    # noinspection PyArgumentList,PyUnresolvedReferences
    def __init__(self):
        super().__init__()

        day_of_week_int = datetime.datetime.today().weekday()

        vbox_l2 = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_l2)
        vbox_l2.addWidget(QtWidgets.QLabel("<h3>Situation</h3>"))

        hbox_days_of_week_l3 = QtWidgets.QHBoxLayout()
        vbox_l2.addLayout(hbox_days_of_week_l3)
        hbox_days_of_week_l3.addWidget(QtWidgets.QCheckBox("Mo"))
        hbox_days_of_week_l3.addWidget(QtWidgets.QCheckBox("Tu"))
        hbox_days_of_week_l3.addWidget(QtWidgets.QCheckBox("We"))
        hbox_days_of_week_l3.addWidget(QtWidgets.QCheckBox("Th"))
        hbox_days_of_week_l3.addWidget(QtWidgets.QCheckBox("Fr"))
        hbox_days_of_week_l3.addWidget(QtWidgets.QCheckBox("Sa"))
        hbox_days_of_week_l3.addWidget(QtWidgets.QCheckBox("Su"))
        #if day_of_week_int == 0:

        hbox_personal_state_l3 = QtWidgets.QHBoxLayout()
        vbox_l2.addLayout(hbox_personal_state_l3)
        self.body_state_qcb = QtWidgets.QComboBox()
        self.body_state_qcb.addItem("Body")
        self.body_state_qcb.addItem("Sick")
        self.body_state_qcb.addItem("Fast-moving")
        hbox_personal_state_l3.addWidget(self.body_state_qcb)
        self.mind_state_qcb = QtWidgets.QComboBox()
        self.mind_state_qcb.addItem("Mind")
        self.mind_state_qcb.addItem("Anxious")
        self.mind_state_qcb.addItem("Loving")
        self.mind_state_qcb.addItem("Overwhelmed")
        hbox_personal_state_l3.addWidget(self.mind_state_qcb)

        vbox_l2.addWidget(wbn.wbn_global.Label(
            "Please select your situation, the schedule and habits will be updated",
            i_word_wrap=True,
            i_italics=True
        ))


        vbox_l2.addStretch(1)

        self.update_gui()

    def update_gui(self):
        pass


schedule_item_str_list = ["Meditation", "Lunch", "Programming", "Dinner", "Social media"]


class ScheduleSubpanelCw(QtWidgets.QWidget):
    # noinspection PyArgumentList,PyUnresolvedReferences
    def __init__(self):
        super().__init__()

        vbox_l2 = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_l2)
        vbox_l2.addWidget(QtWidgets.QLabel("<h3>Schedule</h3>"))

        for schedule_item_str in schedule_item_str_list:
            habit_structured_qll = QtWidgets.QLabel(schedule_item_str)
            vbox_l2.addWidget(habit_structured_qll)

        vbox_l2.addStretch(1)

        self.update_gui()

    def update_gui(self):
        pass


habit_str_list = ["Stretching", "Self-hug", "Mindful walking indoors"]


class HabitsSubpanelCw(QtWidgets.QWidget):
    # noinspection PyArgumentList,PyUnresolvedReferences
    def __init__(self):
        super().__init__()

        vbox_l2 = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_l2)
        vbox_l2.addWidget(QtWidgets.QLabel("<h3>Habits</h3>"))

        for habit_str in habit_str_list:
            habit_structured_qll = QtWidgets.QLabel(habit_str)
            vbox_l2.addWidget(habit_structured_qll)

        vbox_l2.addStretch(1)

        self.update_gui()

    def update_gui(self):
        pass



####class CustomLabel(QtWidgets.QLabel):
#clickable, selectable


