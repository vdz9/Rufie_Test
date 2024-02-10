from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class ThirdScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.set_win()
        self.initUI()
        self.show()

    def set_win(self):
        self.setWindowTitle("И может быть сюда")
        self.resize(1440, 960)

    def initUI(self):
        self.ans1 = QLabel("Сначала ты посмотришь сюда")
        self.ans2 = QLabel("Потом сюда")
        
        self.lay = QVBoxLayout()
        self.lay.addWidget(self.ans1)
        self.lay.addWidget(self.ans2)
        self.setLayout(self.lay)
