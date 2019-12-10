import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidgetItem, QPushButton
from design import Ui_Form
import random


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.count = 37
        self.setupUi(self)
        self.lcdNumber.display(self.count)
        self.takeButton.clicked.connect(self.get)
        self.win = False
    def func(n):
        print(int(n, base=2))
    if __name__ == '__main__':
        n = input()
        func(n)
        
    
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
