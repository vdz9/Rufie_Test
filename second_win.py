from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit

from instr import *
from final_win import *

class SecondScreen(QWidget):
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
        self.FIO_l = QLabel("Введите ФИО")
        self.FIO_ld = QLineEdit()
        self.age_l = QLabel("Введите ваш возраст")
        self.age_ld = QLineEdit()

        self.rec1 = QLabel("1")
        self.rec2 = QLabel("2")
        self.rec3 = QLabel("3")
        self.res1 = QLineEdit()
        self.res2 = QLineEdit()
        self.res3 = QLineEdit()
        self.but1 = QPushButton("1")
        self.but2 = QPushButton("2")
        self.but3 = QPushButton("3")
        self.next = QPushButton("Получить результат")
        self.lay = QVBoxLayout()
        self.lay.addWidget(self.FIO_l)
        self.lay.addWidget(self.FIO_ld)
        self.lay.addWidget(self.age_l)
        self.lay.addWidget(self.age_ld)
        self.lay.addWidget(self.rec1)
        self.lay.addWidget(self.but1)
        self.lay.addWidget(self.res1)
        self.lay.addWidget(self.rec2)
        self.lay.addWidget(self.but2)
        self.lay.addWidget(self.res2)
        self.lay.addWidget(self.rec3)
        self.lay.addWidget(self.but3)
        self.lay.addWidget(self.res3)
        self.lay.addWidget(self.next)
        self.setLayout(self.lay)

    def connects(self):
        self.next.clicked.connect(self.to_third)
        self.but1.clicked.connect(self.answer_1)
        self.but2.clicked.connect(self.answer_2)
        self.but3.clicked.connect(self.answer_3)

    def to_third(self):
        self.hide()
        self.next_screen = ThirdScreen()

    def answer_1(self):
        global answer1
        answer1 = self.res1
    def answer_2(self):
        global answer2
        answer2 = self.res2
    def answer_3(self):
        global answer3
        answer3 = self.res3