import logging
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets


class CentralPanelCw(QtWidgets.QWidget):
    # noinspection PyArgumentList,PyUnresolvedReferences
    def __init__(self):
        super().__init__()

        self.saved_text_str = (
"""
<h3>How does this contribute to my well-being?</h3>
<h3>How does this contribute to the well-being of others?</h3>
<h3>Joyful about this activity</h3>
<h3>Difficult about this activity</h3>
<h3>Boost for getting started with this activity</h3>
Examples: Sugar
<h3>Support during this activity</h3>

Examples: Music, snacks
Sharing this activity with others

<hr>

saved text <font color="gray">Text in another color (for ingrained habits)</font> back to black!
More text here, we can add templates with headers and so on.
"""
        )

        vbox_l2 = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_l2)

        self.habit_qte = QtWidgets.QTextEdit()
        self.habit_qte.setReadOnly(True)
        self.habit_qte.zoomIn(4)
        self.habit_qte.copyAvailable.connect(self.on_habit_copy_available)
        vbox_l2.addWidget(self.habit_qte, stretch=5)

        self.edit_habit_qpb = QtWidgets.QPushButton("Edit text")
        self.edit_habit_qpb.clicked.connect(self.on_edit_rich_text_clicked)
        vbox_l2.addWidget(self.edit_habit_qpb)

        self.diary_entry_qpte = QtWidgets.QPlainTextEdit()
        #self.diary_entry_qpte.
        vbox_l2.addWidget(self.diary_entry_qpte, stretch=1)
        # TODO: Alternatively this can be inside a dialog window

        self.update_gui()

    def on_habit_copy_available(self, i_available:bool):
        if i_available:
            self.habit_qte.copy()
            self.diary_entry_qpte.paste()

    def on_edit_rich_text_clicked(self):
        self.input_text_editor = InputTextEditorDialog(self.saved_text_str)
        self.input_text_editor.finished.connect(self.on_input_text_editor_finished)
        self.input_text_editor.show()
        """
        result_tuple = QtWidgets.QInputDialog.getMultiLineText(
            self,
            "title",
            "label",
            self.saved_text_str
        )
        # http://doc.qt.io/qt-5/qinputdialog.html#getMultiLineText

        if result_tuple[1] == True:
            self.saved_text_str = result_tuple[0]
            self.habit_qte.setHtml(self.saved_text_str)
        """

    def on_input_text_editor_finished(self, i_result: int):
        if i_result == QtWidgets.QDialog.Accepted:
            self.saved_text_str = self.input_text_editor.plain_text_edit_qpte.toPlainText()
        self.update_gui()

    def update_gui(self):
        self.habit_qte.setHtml(self.saved_text_str)


class InputTextEditorDialog(QtWidgets.QDialog):
    def __init__(self, i_start_text:str, i_parent=None):
        super(InputTextEditorDialog, self).__init__(i_parent)

        self.setModal(True)

        vbox_l2 = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_l2)

        hbox_button_row_l3 = QtWidgets.QHBoxLayout()
        vbox_l2.addLayout(hbox_button_row_l3)

        self.ingrained_qpb = QtWidgets.QPushButton("Ingrained")
        self.ingrained_qpb.clicked.connect(self.on_ingrained_clicked)
        hbox_button_row_l3.addWidget(self.ingrained_qpb)

        self.header_qpb = QtWidgets.QComboBox()
        self.header_qpb.addItems(["h1", "h2", "h3", "h4", "h5", "h6"])
        self.header_qpb.activated.connect(self.on_header_activated)
        hbox_button_row_l3.addWidget(self.header_qpb)

        self.plain_text_edit_qpte = QtWidgets.QPlainTextEdit()
        self.plain_text_edit_qpte.setPlainText(i_start_text)
        vbox_l2.addWidget(self.plain_text_edit_qpte)

        self.button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal,
            self
        )
        vbox_l2.addWidget(self.button_box)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

    def on_header_activated(self, i_index: int):
        self.plain_text_edit_qpte.cut()
        self.plain_text_edit_qpte.insertPlainText("<h" + str(i_index+1) + ">")
        self.plain_text_edit_qpte.paste()
        self.plain_text_edit_qpte.insertPlainText("</h" + str(i_index+1) + ">")

    def on_ingrained_clicked(self):
        self.plain_text_edit_qpte.cut()
        self.plain_text_edit_qpte.insertPlainText('<font color="gray">')
        self.plain_text_edit_qpte.paste()
        self.plain_text_edit_qpte.insertPlainText('</font>')

        # get marked/selected text
        # adding <font color="gray">___________</font>
