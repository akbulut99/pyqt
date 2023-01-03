import sys
from PyQt5 import QtWidgets
import sqlite3


class pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def baglanti(self):
        baglanti = sqlite3.connect("database.db")
        self.cursor = baglanti.cursor()
        self.cursor.execute("Create Table If not exists üyler(kullanici_adi TEXT,parola TEXT)")
        baglanti.commit()

    def init_ui(self):
        self.setWindowTitle("Arayüz")
        self.setGeometry(100, 100, 500, 400)

        self.kullanıcı_Adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.buton = QtWidgets.QPushButton("Giriş Yap")
        self.yazi_alani = QtWidgets.QLabel("")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanıcı_Adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.buton)
        self.setLayout(v_box)
        self.buton.clicked.connect(self.login)

        self.show()
    def login(self):
        adi = self.kullanıcı_Adi.text()
        parola = self.parola.text()
        self.cursor.execute("Select * From üyler WHERE kullanici_adi = ? and  parola = ?",(adi,parola))
        data = self.cursor.fetchall()
        if len(data) == 0:
            self.yazi_alani.setText("Böyle bir kullanıcı bulunamadı lütfen tekrar deneyin.")
        else:
            self.yazi_alani.setText("Hoşgeldiniz" + adi)
app = QtWidgets.QApplication(sys.argv)
pencere = pencere()
sys.exit(app.exec_())
