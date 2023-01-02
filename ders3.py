import sys
from PyQt5 import QtWidgets,QtGui
def pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    buton = QtWidgets.QPushButton(pencere)
    buton.setText("buton")
    buton.move(200,200)
    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("Merhaba Dünya")
    pencere.setWindowTitle("Ders3")
    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())

pencere()