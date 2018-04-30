#!/usr/bin/env python3
import logging
import os
import sqlite3
import sys
import PyQt5.Qt
from PyQt5 import QtCore
from PyQt5 import QtWidgets
import wbn.gui.main_window
import wbn.wbn_global


if __name__ == "__main__":
    wbn.wbn_global.db_file_exists_at_application_startup_bl = os.path.isfile(wbn.wbn_global.get_database_filename())
    # -settings this variable before the file has been created

    logging.basicConfig(level=logging.DEBUG)  # -by default only warnings and higher are shown

    wbn_qapplication = QtWidgets.QApplication(sys.argv)

    #wbn_qapplication.setQuitOnLastWindowClosed(False)
    wbn_main_window = wbn.gui.main_window.MainWindow()
    wbn_main_window.show()

    sys.exit(wbn_qapplication.exec_())
