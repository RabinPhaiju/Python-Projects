import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
layout = QtWidgets.QVBoxLayout(window)


myListWidget = QtWidgets.QListWidget()
for i in range(1,20):
    myListWidget.addItem(str(i))

def listview_clicked():
    item = myListWidget.currentItem()
    print(item.text())

myListWidget.clicked.connect(listview_clicked)




layout.addWidget(myListWidget)
window.show()

sys.exit(app.exec_())