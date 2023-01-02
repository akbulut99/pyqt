import sys
from PyQt5 import QtWidgets
def pencere():
    app = QtWidgets.QApplication(sys.argv)
    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")

    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)
    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Ders 4")
    pencere.setGeometry(100, 100, 500, 500)
    pencere.setLayout(v_box)
    pencere.show()
    sys.exit(app.exec_())
# h_box.addStretch() bunu nereye yazarsak oraya yaslar



pencere()