from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.window = QtWidgets.QFrame(self.centralwidget)
        self.window.setGeometry(QtCore.QRect(60, 200, 510, 291))
        self.window.setStyleSheet("QFrame {\n"
"    background-color: #224168;\n"
"    border-radius: 10px;\n"
"}")
        self.window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.window.setObjectName("window")
        self.close = QtWidgets.QPushButton(self.window)
        self.close.setGeometry(QtCore.QRect(10, 8, 16, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close.sizePolicy().hasHeightForWidth())
        self.close.setSizePolicy(sizePolicy)
        self.close.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(255, 96, 92);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(221, 82, 80);\n"
"}")
        self.close.setText("")
        self.close.setAutoDefault(False)
        self.close.setObjectName("close")
        self.minimize = QtWidgets.QPushButton(self.window)
        self.minimize.setGeometry(QtCore.QRect(40, 8, 16, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimize.sizePolicy().hasHeightForWidth())
        self.minimize.setSizePolicy(sizePolicy)
        self.minimize.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius: 8px;\n"
"    \n"
"    background-color:rgb(255, 189, 68);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(225, 164, 60);\n"
"}")
        self.minimize.setText("")
        self.minimize.setAutoDefault(False)
        self.minimize.setObjectName("minimize")
        self.maximize = QtWidgets.QPushButton(self.window)
        self.maximize.setGeometry(QtCore.QRect(70, 8, 16, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maximize.sizePolicy().hasHeightForWidth())
        self.maximize.setSizePolicy(sizePolicy)
        self.maximize.setStyleSheet("QPushButton {\n"
"\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(0, 221, 85);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(0, 191, 73);\n"
"}")
        self.maximize.setText("")
        self.maximize.setAutoDefault(False)
        self.maximize.setObjectName("maximize")
        self.title_bar = QtWidgets.QLabel(self.window)
        self.title_bar.setGeometry(QtCore.QRect(0, 0, 511, 31))
        self.title_bar.setStyleSheet("QLabel {\n"
"    background-color: rgb(39, 75, 120);\n"
"    border-radius: 5px;\n"
"    color: #f09469;\n"
"    qproperty-alignment: AlignCenter;\n"
"    padding-bottom: 2px;\n"
"    \n"
"    font: 13pt \"Cascadia Code\";\n"
"}")
        self.title_bar.setObjectName("title_bar")
        self.dna_taker = QtWidgets.QLineEdit(self.window)
        self.dna_taker.setGeometry(QtCore.QRect(150, 50, 341, 31))
        self.dna_taker.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    background-color: #65c7ab;\n"
"    color: #224168;\n"
"    padding: 2px;\n"
"    padding-bottom: 5px;    \n"
"    font: 9pt \"Leelawadee UI Semilight\";\n"
"}")
        self.dna_taker.setText("")
        self.dna_taker.setObjectName("dna_taker")
        self.rna_output = QtWidgets.QLabel(self.window)
        self.rna_output.setGeometry(QtCore.QRect(150, 100, 341, 31))
        self.rna_output.setStyleSheet("QLabel {\n"
"    border-radius: 3px;\n"
"    background-color: #65c7ab;\n"
"    color: #224168;\n"
"    padding: 2px;\n"
"    padding-bottom: 5px;    \n"
"    font: 9pt \"Leelawadee UI Semilight\";\n"
"}")
        self.rna_output.setText("")
        self.rna_output.setObjectName("rna_output")
        self.protein_output = QtWidgets.QLabel(self.window)
        self.protein_output.setGeometry(QtCore.QRect(150, 150, 341, 31))
        self.protein_output.setStyleSheet("QLabel {\n"
"    border-radius: 3px;\n"
"    background-color: #65c7ab;\n"
"    color: #224168;\n"
"    padding: 2px;\n"
"    padding-bottom: 5px;    \n"
"    font: 8pt \"Leelawadee UI Semilight\";\n"
"}")
        self.protein_output.setText("")
        self.protein_output.setObjectName("protein_output")
        self.RNALabel = QtWidgets.QLabel(self.window)
        self.RNALabel.setGeometry(QtCore.QRect(50, 100, 81, 31))
        self.RNALabel.setStyleSheet("QLabel {\n"
"    border-radius: 3px;\n"
"    color: #bdece9;\n"
"    font: 11pt \"Arial\";\n"
"}")
        self.RNALabel.setObjectName("RNALabel")
        self.ProteinLabel = QtWidgets.QLabel(self.window)
        self.ProteinLabel.setGeometry(QtCore.QRect(50, 150, 81, 31))
        self.ProteinLabel.setStyleSheet("QLabel {\n"
"    border-radius: 3px;\n"
"    color: #bdece9;\n"
"    \n"
"    font: 11pt \"Arial\";\n"
"}")
        self.ProteinLabel.setObjectName("ProteinLabel")
        self.DNALabel = QtWidgets.QLabel(self.window)
        self.DNALabel.setGeometry(QtCore.QRect(50, 50, 81, 31))
        self.DNALabel.setStyleSheet("QLabel {\n"
"    border-radius: 3px;\n"
"    color: #bdece9;\n"
"    font: 11pt \"Arial\";\n"
"}")
        self.DNALabel.setObjectName("DNALabel")
        self.enter = QtWidgets.QPushButton(self.window)
        self.enter.setGeometry(QtCore.QRect(164, 210, 71, 21))
        self.enter.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    color: rgb(72, 112, 86);\n"
"    background-color: rgb(149, 232, 180);\n"
"    font: 9pt \"Cascadia Code\";\n"
"    padding-bottom: 2px;\n"
"}\n"
"QPushButton::hover {\n"
"    color: rgb(54, 85, 66);\n"
"    background-color: rgb(125, 195, 151);\n"
"}\n"
"QPushButton::disabled {\n"
"    color: rgb(108, 108, 108);\n"
"    background-color: rgb(163, 163, 163);\n"
"}")
        self.enter.setObjectName("enter")
        self.clear = QtWidgets.QPushButton(self.window)
        self.clear.setGeometry(QtCore.QRect(270, 210, 71, 21))
        self.clear.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    color: rgb(80, 125, 97);\n"
"    background-color: #f09469;\n"
"    font: 9pt \"Cascadia Code\";\n"
"    padding-bottom: 2px;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(199, 123, 87);\n"
"}")
        self.clear.setObjectName("clear")
        self.error_console = QtWidgets.QLabel(self.window)
        self.error_console.setGeometry(QtCore.QRect(10, 250, 491, 21))
        self.error_console.setStyleSheet("QLabel {\n"
"    border-radius: 3px;\n"
"    background-color: rgb(249, 87, 72);\n"
"    color: rgb(165, 38, 66);\n"
"    padding: 2px;\n"
"    \n"
"    font: 8pt \"Consolas\";\n"
"\n"
"}")
        self.error_console.setObjectName("error_console")
        self.error_console.raise_()
        self.title_bar.raise_()
        self.maximize.raise_()
        self.minimize.raise_()
        self.close.raise_()
        self.dna_taker.raise_()
        self.rna_output.raise_()
        self.protein_output.raise_()
        self.RNALabel.raise_()
        self.ProteinLabel.raise_()
        self.DNALabel.raise_()
        self.enter.raise_()
        self.clear.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_bar.setText(_translate("MainWindow", "DNA -> Protein"))
        self.RNALabel.setText(_translate("MainWindow", "RNA"))
        self.ProteinLabel.setText(_translate("MainWindow", "Protein"))
        self.DNALabel.setText(_translate("MainWindow", "DNA"))
        self.enter.setText(_translate("MainWindow", "->"))
        self.clear.setText(_translate("MainWindow", "💨"))
        self.error_console.setText(_translate("MainWindow", "Error: Console is being shown :<"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
