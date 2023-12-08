from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Jatin GUI development")
        self.setWindowIcon(QIcon('002 python.png'))
        self.create_button()
        
'''
        To create a push button in an application, you need to create an 
        instance of the QPushButton class.
'''
    def create_button(self):
        btn = QPushButton("Click", self)
        btn.setGeometry(100,100, 130, 130)
        btn.setFont(QFont("Times", 14, QFont.Weight.Bold))
        btn.setIcon(QIcon('WIN_20230929_19_17_46_Pro.jpg'))

        menu = QMenu()
        menu.addAction("Copy")
        menu.addAction("Cut")
        menu.addAction("Paste")
        btn.setMenu(menu)
        menu.setStyleSheet('background-color:#294521')
        '''setText(): This method is used to assign text to the push button
            setIcon(): This method is used to assign an icon to the push button
            setGeometry(): This method is used for setting the x and y position, also width and height of the button.
            setMenu(): This method is used for setting pop menu to the button.
        '''

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())