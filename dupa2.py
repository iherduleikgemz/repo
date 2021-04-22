import cv2
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QFileDialog
from PyQt5 import uic
import sys, os
class UI(QMainWindow):
    def __init__(self):

        super(UI, self).__init__()
        uic.loadUi("form.ui", self)
        def moresteck():
            self.label.setText("moresteck to pedal")
            im=cv2.imread("1.png")
            q_im = cv2.resize(cv2.cvtColor((im), cv2.COLOR_BGR2RGB), (500,500), interpolation = cv2.INTER_NEAREST)
            self.label.setPixmap( QPixmap(QImage(q_im.data, 500, 500, 500*3,  QImage.Format_RGB888))  )
        self.pushButton.clicked.connect(moresteck)

        self.show()
        app.setStyle('fusion')

app = QApplication(sys.argv)
window = UI()
app.exec()