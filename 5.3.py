import sys
from PyQt5 import QtWidgets,QtGui

def pencere():
 app = QtWidgets.QApplication(sys.argv)
 pencere = QtWidgets.QWidget()
 pencere.setWindowTitle("pyqt5.3")
 buton=QtWidgets.QPushButton(pencere)#buton oluşturur
 buton.setText("TIKLA")
 etiket1 = QtWidgets.QLabel(pencere)
 etiket1.setText("merhaba dünya")
 etiket1.move(200, 30)
 buton.move(200, 60)
 pencere.setGeometry(100, 100,500,500)
 pencere.show()
 sys.exit(app.exec_())


pencere()