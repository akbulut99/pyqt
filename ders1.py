import sys
from PyQt5 import QtWidgets,QtGui
def pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PYQT5 DERSLERİ")
    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("Deneme yazısı")

    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("sta at.png"))
    pencere.setGeometry(300,300,500,500)
    pencere.show()
    sys.exit(app.exec_())

pencere()