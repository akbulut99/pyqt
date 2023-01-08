import sys

from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QTextEdit,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
 def __init__(self):
    super().__init__()
    self.init_ui()
 def init_ui(self):
    self.yazi_alani = QTextEdit()
    self.buton = QPushButton("TEMİZLE")
    v_box = QVBoxLayout()
    v_box.addWidget(self.yazi_alani)
    v_box.addWidget(self.buton)
    self.setWindowTitle("text alanı")
    self.setLayout(v_box)
    self.buton.clicked.connect(self.click)
    self.show()

 def click(self):
   self.yazi_alani.clear()




app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())