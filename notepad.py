import sys
import os

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout

from PyQt5.QtWidgets import QAction,qApp,QMainWindow

class notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazi_alani = QTextEdit()
        self.temizle=QPushButton("Temizle")
        self.ac = QPushButton("Aç")
        self.kaydet = QPushButton("kaydet")
        h_box = QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.kaydet)
        h_box.addWidget(self.ac)
        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box)
        self.setLayout(v_box)
        self.temizle.clicked.connect(self.yaziyi_temizle)
        self.kaydet.clicked.connect(self.Kaydet)
        self.ac.clicked.connect(self.dosya_ac)
        self.setWindowTitle("Notepad")
        
        
    def yaziyi_temizle(self):
        self.yazi_alani.clear()
    def dosya_ac(self):
        dosya_ismi = QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))

        with open(dosya_ismi[0],"r") as file:
            self.yazi_alani.setText(file.read())
    def Kaydet(self):
        dosya_ismi = QFileDialog.getSaveFileName(self,"Dosya kayder",os.getenv("HOME"))
        with open(dosya_ismi[0],"w") as file:

            file.write(self.yazi_alani.toPlainText())

class menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencere = notepad()
        
        self.setCentralWidget(self.pencere) #oluturduğumuz menünün içine notepadi eklmemizi sağlar
        
        self.menu_olustur()
        
    def menu_olustur(self):
        menubar = self.menuBar()
       
        Dosya = menubar.addMenu("Dosya")
       
        dosya_ac = QAction("Dosya Aç",self) 
        dosya_ac.setShortcut("Ctrl+O")
       
        dosya_kaydet = QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")
       
        dosya_temizle = QAction ("Dosyayı Temizle", self)
        dosya_temizle.setShortcut("Ctrl+D")
       
        cikis = QAction("çıkış", self)
        cikis.setShortcut("Ctrl+Q")
        Dosya.addAction(dosya_ac)
        Dosya.addAction(dosya_kaydet)
        Dosya.addAction(dosya_temizle)
        Dosya.addAction(cikis)
        Dosya.triggered.connect(self.response)

        self.show()
    def response(self):
        if action.text()=="Dosya Aç":
            self.pencere.dosya_ac()
        elif action.text()=="Dosya Kaydet":
            self.pencere.dosya_kaydet
        elif action.text()=="Dosyayı Temizle":
            self.pencere.dosya_temizle
        elif action.text()=="çıkış":
            qApp.quit()

app = QApplication(sys.argv)
menu = menu()
sys.exit(app.exec_())