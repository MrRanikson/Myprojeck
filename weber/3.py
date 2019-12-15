import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QLineEdit


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

 
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('dis.ui',self)
        self.pushButton.clicked.connect(self.run)
        
    def run(self):
        number = self.lineEdit_2.text()
        base_number = int(self.lineEdit.text())
        res = int(number, base_number)
        self.label.setText(str(res))
        
    def __int__(self):
        super().__init__()
        uic.loadUi('dis.ui',self)
        self.checkBox.clicked.connect(self.run)    
        
 

sys.excepthook = except_hook
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())