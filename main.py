from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

from second_win import *

class FirstScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.set_win()
        self.initUI()
        self.connects()
        self.show()

    def set_win(self):
        self.setWindowTitle("Тест Руфье")
        self.resize(1440, 960)

    def initUI(self):
        self.greetings = QLabel(greetings_t)
        self.desc = QLabel(description_t)
        self.next = QPushButton("Начать")

        self.lay = QVBoxLayout()
        self.lay.addWidget(self.greetings)
        self.lay.addWidget(self.desc)
        self.lay.addWidget(self.next)
        self.setLayout(self.lay)


    def connects(self):
        self.next.clicked.connect(self.to_second)

    def to_second(self):
        self.hide()
        self.next_screen = SecondScreen()

app = QApplication([])
my_app = FirstScreen()
app.exec()