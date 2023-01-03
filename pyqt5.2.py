import sys
from PyQt5 import QtWidgets,QtGui

def pencere():
    app=QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("pyqt5.2")
    etiket1=QtWidgets.QLabel(pencere)
    etiket2=QtWidgets.QLabel(pencere)#etiket oluşturur
    etiket1.setText("YILDIZ STALLIONS")#olşturduğumuz etiket içine yazı ekler
    etiket1.move(200, 150)
    etiket2.setPixmap(QtGui.QPixmap("sta at.png"))#resim eklmeyi sağlar
    
    pencere.setGeometry(100, 100, 500, 500)
    pencere.show()
    sys.exit(app.exec_())

pencere()