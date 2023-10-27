from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QMessageBox
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setMaximumSize(QtCore.QSize(900, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(405, 30, 480, 500))
        self.listWidget.setMinimumSize(QtCore.QSize(480, 500))
        self.listWidget.setMaximumSize(QtCore.QSize(480, 500))
        self.listWidget.setObjectName("listWidget")
        self.label_information = QtWidgets.QLabel(self.centralwidget)
        self.label_information.setGeometry(QtCore.QRect(410, 10, 471, 16))
        self.label_information.setObjectName("label_information")
        self.lineEdit_title = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_title.setGeometry(QtCore.QRect(130, 50, 211, 31))
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(70, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_author = QtWidgets.QLabel(self.centralwidget)
        self.label_author.setGeometry(QtCore.QRect(50, 100, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_author.setFont(font)
        self.label_author.setObjectName("label_author")
        self.lineEdit_author = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_author.setGeometry(QtCore.QRect(130, 100, 211, 31))
        self.lineEdit_author.setObjectName("lineEdit_author")
        self.label_year = QtWidgets.QLabel(self.centralwidget)
        self.label_year.setGeometry(QtCore.QRect(70, 150, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_year.setFont(font)
        self.label_year.setObjectName("label_year")
        self.lineEdit_year = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_year.setGeometry(QtCore.QRect(130, 150, 211, 31))
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.label_isbn = QtWidgets.QLabel(self.centralwidget)
        self.label_isbn.setGeometry(QtCore.QRect(70, 200, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_isbn.setFont(font)
        self.label_isbn.setObjectName("label_isbn")
        self.lineEdit_isbn = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_isbn.setGeometry(QtCore.QRect(130, 200, 211, 31))
        self.lineEdit_isbn.setObjectName("lineEdit_isbn")
        self.pushButton_view = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_view.setGeometry(QtCore.QRect(230, 260, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_view.setFont(font)
        self.pushButton_view.setObjectName("pushButton_view")
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setGeometry(QtCore.QRect(230, 320, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(60, 260, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_update.setGeometry(QtCore.QRect(60, 320, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_update.setFont(font)
        self.pushButton_update.setObjectName("pushButton_update")
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(60, 380, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(230, 380, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setObjectName("pushButton_clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout_Book_Store = QAction(MainWindow)
        self.actionAbout_Book_Store.setObjectName("actionAbout_Book_Store")
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout_Book_Store)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.actionExit.triggered.connect(lambda: self.exit_program())
        self.actionAbout_Book_Store.triggered.connect(lambda: self.About_Game())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_add.clicked.connect(self.insert_into_table)
        self.pushButton_view.clicked.connect(self.view_from_table)
        self.listWidget.clicked.connect(self.listview_clicked)
        self.pushButton_delete.clicked.connect(self.delete_from_table)
        self.pushButton_update.clicked.connect(self.update_table)
        self.pushButton_search.clicked.connect(self.search_table)
        self.pushButton_clear.clicked.connect(self.clear_screen)

    def About_Game(self):
        msg = QMessageBox()
        msg.setWindowTitle('About Game')
        msg.setWindowIcon(QtGui.QIcon("book.jpg"))
        with open('book.txt', 'r') as f:
            text = f.read()
            msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Close)
        x = msg.exec_()


    def exit_program(self):
        QCoreApplication.instance().quit()

    def insert_into_table(self):
        title = self.lineEdit_title.text()
        author = self.lineEdit_author.text()
        year = self.lineEdit_year.text()
        isbn = self.lineEdit_isbn.text()
        if title and author and year and isbn:
            self.clear_lineEdit()
            conn = sqlite3.connect('book.db')
            cur = conn.cursor()
            cur.execute('INSERT INTO store VALUES (?,?,?,?)',(title, author, year, isbn))
            conn.commit()
            conn.close()
            self.view_from_table()

    def create_table(self):
        conn = sqlite3.connect('book.db')
        cur = conn.cursor()
        cur.execute('CREATE TABLE If NOT EXISTS store(title TEXT, author TEXT, year TEXT, isbn TEXT)')
        conn.commit()
        conn.close()

    def listview_clicked(self):
        item = self.listWidget.currentItem()
        text = item.text().split('  ')
        self.lineEdit_title.setText(text[0])
        self.lineEdit_author.setText(text[1])
        self.lineEdit_year.setText(text[2])
        self.lineEdit_isbn.setText(text[3])
    
    def view_from_table(self):
        self.listWidget.clear()
        conn = sqlite3.connect('book.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM store")
        rows = cur.fetchall()
        conn.close()
        for content in rows:
            text_print = ''
            for text in content:
                text_print += text + "  "
            self.listWidget.addItem(text_print)

    def delete_from_table(self):
        if self.listWidget.currentItem():
            item = self.listWidget.currentItem()
            text = item.text().split('  ')
            conn = sqlite3.connect('book.db')
            cur = conn.cursor()
            cur.execute("DELETE FROM store WHERE title=? and author=? and year=? and isbn=?",(text[0],text[1],text[2],text[3]))
            conn.commit()
            conn.close()
            self.clear_lineEdit()
            self.view_from_table()

    def clear_lineEdit(self):
        self.lineEdit_title.clear()
        self.lineEdit_author.clear()
        self.lineEdit_year.clear()
        self.lineEdit_isbn.clear()
        
    def update_table(self):
        if self.listWidget.currentItem() and self.lineEdit_author.text() and self.lineEdit_title.text() and self.lineEdit_year.text() and self.lineEdit_isbn.text():
            item = self.listWidget.currentItem()
            text = item.text().split('  ')
            conn = sqlite3.connect('book.db')
            cur = conn.cursor()
            cur.execute("UPDATE store SET author=?, year=?, isbn=? WHERE title=?",(self.lineEdit_author.text(), self.lineEdit_year.text(), self.lineEdit_isbn.text(), text[0]))
            conn.commit()
            conn.close()
            self.clear_lineEdit()
            self.view_from_table()

    def search_table(self):
        if self.lineEdit_title.text():
            self.listWidget.clear()
            conn = sqlite3.connect('book.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM store WHERE title=?",(self.lineEdit_title.text(),))
            rows = cur.fetchall()
            conn.close()
            for content in rows:
                text_print = ''
                for text in content:
                    text_print += text + "  "
                self.listWidget.addItem(text_print)

    def clear_screen(self):
        self.listWidget.clear()
        self.clear_lineEdit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Book Store"))
        MainWindow.setWindowIcon(QtGui.QIcon("book.jpg"))
        self.label_information.setText(_translate("MainWindow", "Information"))
        self.label_title.setText(_translate("MainWindow", "Title"))
        self.label_author.setText(_translate("MainWindow", "Author"))
        self.label_year.setText(_translate("MainWindow", "Year"))
        self.label_isbn.setText(_translate("MainWindow", "ISBN"))
        self.pushButton_view.setText(_translate("MainWindow", "View All"))
        self.pushButton_search.setText(_translate("MainWindow", "Search"))
        self.pushButton_add.setText(_translate("MainWindow", "Add Entry"))
        self.pushButton_update.setText(_translate("MainWindow", "Update"))
        self.pushButton_delete.setText(_translate("MainWindow", "Delete"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit"))
        self.actionAbout_Book_Store.setText(_translate("MainWindow", "About Book Store"))
        self.actionAbout_Book_Store.setStatusTip(_translate("MainWindow", "About Book Store"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.create_table()
    MainWindow.show()
    sys.exit(app.exec())
