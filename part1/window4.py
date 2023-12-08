from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Jatin GUI development")
        self.setWindowIcon(QIcon('Images/WIN_20230929_19_17_46_Pro.jpg'))
        # self.setFixedWidth(500)
        # self.setFixedHeight(1400)
        self.setStyleSheet('background-color:green')



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
