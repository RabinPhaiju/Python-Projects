# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'catdog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(968, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 951, 551))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../../../../xampp/htdocs/Food-For-Needy/files/5-1.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.cat = QtWidgets.QPushButton(self.centralwidget)
        self.cat.setGeometry(QtCore.QRect(330, 570, 93, 28))
        self.cat.setObjectName("cat")
        self.dog = QtWidgets.QPushButton(self.centralwidget)
        self.dog.setGeometry(QtCore.QRect(560, 570, 93, 28))
        self.dog.setObjectName("dog")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 968, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.dog.clicked.connect(self.show_dog)
        self.cat.clicked.connect(self.show_cat)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cat.setText(_translate("MainWindow", "Cat"))
        self.dog.setText(_translate("MainWindow", "Dog"))

    def show_dog(self):
        self.photo.setPixmap(QtGui.QPixmap("../../../../xampp/htdocs/Food-For-Needy/files/5-1.jpg"))


    def show_cat(self):
        self.photo.setPixmap(QtGui.QPixmap("../../../../xampp/htdocs/Food-For-Needy/files/objective2.jpg"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
