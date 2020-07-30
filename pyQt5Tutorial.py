# NOTE: gx-to-open https://www.youtube.com/watch?v=FVpho_UiDAY&list=PLzMcBGfZo4-lB8MZfHPLTEHO9zJDDLpYj&index=3&t=42s

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 200, 200)
        self.setWindowTitle("PyQt5 Tutorial")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label!")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click Me!")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("yay, you clicked me!")
        self.update()

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
