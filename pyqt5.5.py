import sys
from PyQt5 import QtWidgets,QtGui
def pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("pyqt5.4")
    okay = QtWidgets.QPushButton("TAMAM")
    cancel = QtWidgets.QPushButton("İPTAL") 
    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(okay)
    v_box.addWidget(cancel)
    pencere.setLayout(v_box)
    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())
    
    

pencere()

