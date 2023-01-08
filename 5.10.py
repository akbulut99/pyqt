import sys
from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow
class menu(QMainWindow):
    def __init__(self):
        super().__init__()
        menubar = self.menuBar()#menubar oluşturmanı sağlar
        dosya = menubar.addMenu("Dosya")
        düzenle = menubar.addMenu("Düzenle")
        dosya_ac = QAction("Dosya aç",self)#aksiyon eklemeni sağlar
        dosya_ac.setShortcut("Ctrl+O")#kısa yol eklemeni sağlar
        dosya_kaydet = QAction("Dosya kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")
        cikis = QAction("Çıkış",self)
        cikis.setShortcut("Ctrl+Q")
        temizle = QAction("Temizle", self)
        düzenle.addAction(temizle)
        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)
        arave_degistir=düzenle.addMenu("Ara ve Değiştir")#alt menü
        ara=QAction("Ara",self)
        degistir = QAction("Değiştir", self)
        arave_degistir.addAction(ara)
        arave_degistir.addAction(degistir)
        cikis.triggered.connect(self.cikis_yap) #çıkış aksiyona yeni bir fonksiyon ekler
        dosya.triggered.connect(self.response)#hangi aksiyonun devreye girdiğini anlamak için kullanıyoruz
        self.setWindowTitle("Menüler")
        self.setGeometry(100, 100, 500, 500)#safya boyutlarını ayarlar
        
        self.show()
    def cikis_yap(self):
     qApp.quit() #programı kapatır
    def response(self, action):
        if action.text()=="Dosya aç":
            print("dosya aç'a basıldı...")
        elif action.text() == "Dosya kaydet":
            print("dosya kaydet'e basıldı...")
        elif action.text() == "Çıkış":
            print("çıkış'a basıldı...")


    

app = QApplication(sys.argv)
menu = menu()
sys.exit(app.exec_())