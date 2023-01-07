import sys
from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        
        super().__init__()
        
        self.init_ui()

    def init_ui(self):
        self.radio_yazisi = QLabel("Hangi dili daha çok seviyorsun?")
        self.java = QRadioButton("java")
        self.python = QRadioButton("piton")
        self.php = QRadioButton("php")
        self.yazi_alani = QLabel(" ")
        self.buton = QPushButton("GÖNDER")
        v_box = QVBoxLayout()
        v_box.addWidget(self.radio_yazisi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.php)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addStretch()
        v_box.addWidget(self.buton)
        self.setLayout(v_box)
        self.setWindowTitle("radio button")
        self.buton.clicked.connect(lambda: self.click(self.python.isChecked(),self.java.isChecked(),self.php.isChecked(),self.yazi_alani))

        self.show()

    def click(self,python,java,php,yazi_alani):
        if python:
            yazi_alani.setText("python seçildi")
        if java:
            yazi_alani.setText("java seçildi")
        if php:
            yazi_alani.setText("php seçildi")


app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())