import self as self
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Jatin GUI development")
        self.setWindowIcon(QIcon('Pyqt/pyqtapp/Images/002 python.png'))

 '''  #For puting image in the label
        label = QLabel(self)
        pixmap = QPixmap('Pyqt\pyqtapp/Images/WIN_20230929_19_17_46_Pro.jpg')
        label.setPixmap(pixmap)
'''
'''  #For GIF in the label
        label = QLabel(self)
        movie = QMovie('Pyqt\pyqtapp/Images/WIN_20230929_19_17_46_Pro.jpg')
        movie.setSpeed(500)c
        label.setMovie(pixmap)
        movie.start
'''


'''
        #Adding Text
        label = QLabel("Python GUI Development", self)
        # label.setNum(15)
        label.setText("This is Set-Text")
        label.move(200, 200)
        label.setFont(QFont("Sanserif", 15))
        label.setStyleSheet('color:red')
        # label.setText()
        #   label.setTabOrder()

'''





app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())