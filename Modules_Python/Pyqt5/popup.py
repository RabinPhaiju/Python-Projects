# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.popup = QtWidgets.QPushButton(self.centralwidget)
        self.popup.setGeometry(QtCore.QRect(202, 177, 361, 81))
        self.popup.setObjectName("popup")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.popup.clicked.connect(self.show_popup)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.popup.setText(_translate("MainWindow", "Click"))


    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle('Hello')
        msg.setWindowIcon(QtGui.QIcon("../../../../xampp/htdocs/Food-For-Needy/files/5-1.jpg"))
        msg.setText("This is the main text!")

        msg.setIcon(QMessageBox.Warning)
        # msg.setIcon(QMessageBox.Information)
        # msg.setIcon(QMessageBox.Question)

        # buttions
        # ok, open, save, cancel, close, yes, no, abort, retry, ignore
        msg.setStandardButtons(QMessageBox.Open | QMessageBox.Close)
        msg.setDefaultButton(QMessageBox.Close)

        # information
        msg.setInformativeText("infromation")

        # Show detail
        msg.setDetailedText("details")

        #
        msg.buttonClicked.connect(self.popup_button)

        x = msg.exec_()


    def popup_button(self, i):
        print(i.text())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
