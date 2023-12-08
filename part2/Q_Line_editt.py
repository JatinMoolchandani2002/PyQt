from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Jatin GUI development")
        self.setWindowIcon(QIcon('part1/002 python.png'))


        line_edit = QLineEdit(self)
        line_edit.setFont(QFont("Nyala", 25))
        # line_edit.setText("DefaultText")
        #line_edit.setPlaceholderText("Please enter your Username")
        #line_edit.setEchoMode(QLineEdit.EchoMode.Password) #Like a Password
        line_edit.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())