import sys
from PyQt5 import QtWidgets,QtGui
def pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("pyqt5.4")
    okay = QtWidgets.QPushButton("TAMAM")
    cancel = QtWidgets.QPushButton("İPTAL") 
    h_box = QtWidgets.QHBoxLayout() #horizanal box oluşuturur
    h_box.addStretch()
    h_box.addWidget(okay) #butonları içine ekledik
    h_box.addWidget(cancel)
    h_box.addStretch() #sağa ve sola yaslamak için kullanılır

    pencere.setLayout(h_box)#pencereye ekler

    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())
    
    

pencere()

