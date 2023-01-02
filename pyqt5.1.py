import sys

from PyQt5 import QtWidgets

def pencere():
    app=QtWidgets.QApplication(sys.argv) #komut satırından alıncak olan argümanları getirir
    pencere = QtWidgets.QWidget() #pencere oluşuturu
    pencere.setWindowTitle("pyqt5.1")
    pencere.show()
    sys.exit(app.exec_()) #uygulamayı döngüye sokar


pencere() 