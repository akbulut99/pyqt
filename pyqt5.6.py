import sys
from PyQt5 import QtWidgets

class pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
     self.yazı_alanı = QtWidgets.QLabel("henüz tıklanmadı")
     self.buton = QtWidgets.QPushButton("TIKLA")
     self.say = 0
     
     v_box = QtWidgets.QVBoxLayout()
     v_box.addWidget(self.buton)
     v_box.addWidget(self.yazı_alanı)
     v_box.addStretch()
     h_box = QtWidgets.QHBoxLayout()
     
     h_box.addStretch()
     h_box.addLayout(v_box)
     h_box.addStretch()
     self.setLayout(h_box)
     self.show()

app = QtWidgets.QApplication(sys.argv)
pencere = pencere()
sys.exit(app.exec_())