from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow): # inherit from QMainWindow
    def __init__(self, x_pos=400, y_pos=400, width=640, height=480, title='Test'):
        super(MyWindow, self).__init__()
        self.setGeometry(x_pos, y_pos, width, height)
        self.setWindowTitle(title)
        self.initUI()

    def initUI(self, x=50, y=50):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("hello welcome")
        self.label.move(x, y)
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Click me')
        self.b1.clicked.connect(self.clicked)  # call function

    def clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def update(self): # called it when there is change in window
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv) # define application how to display base in os
    win = MyWindow() # window to show in application
    win.show()
    sys.exit(app.exec_())


window()
