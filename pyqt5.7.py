import sys
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout
class pencere(QWidget):
    def __init__(self):
        super() .__init__()
        self.init_ui()
    def init_ui(self):
        self.checkbox = QCheckBox("pythonu seviyor musunuz?")
        self.yazi_alani = QLabel(" ")
        self.buton = QPushButton("TIKLA")
        v_box = QVBoxLayout()
        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)
        self.setWindowTitle("checkbox")
        self.buton.clicked.connect(lambda:self.click(self.checkbox.isChecked(),self.yazi_alani))
        #lambda önündeki fonksiyona obje gönderir

        self.setLayout(v_box)
        self.show()
    def click(self,checkbox,yazi_alani):
        if checkbox:
            yazi_alani.setText("pitonu seviyorum Xd")
        else:
            yazi_alani.setText("Neden sevmiyorsun:/")
            


app = QApplication(sys.argv)
pencere = pencere()
sys.exit(app.exec_())