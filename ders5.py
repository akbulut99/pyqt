import sys
from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()  # miras için

        self.init_ui()

    def init_ui(self):
        self.yazi_alanı = QtWidgets.QLabel("Henüz tıklanmadı")
        self.buton = QtWidgets.QPushButton("tıkla")
        self.say = 0
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi_alanı)
        v_box.addStretch()
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.buton.clicked.connect(self.click)
        self.show()

    def click(self):
        self.say += 1
        self.yazi_alanı.setText(str(self.say)+" Kere Tıklandı.")


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
