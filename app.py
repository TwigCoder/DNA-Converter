from dna import *
import sys, PyQt5
from PyQt5 import  QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow

from my_ui import Ui_MainWindow

class Window(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.title_bar.isPressed = False

        # Hide Title Bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.close.clicked.connect(self.exit_app)
        self.ui.minimize.clicked.connect(self.min_app)
        self.ui.maximize.clicked.connect(self.max_app)
        self.ui.enter.clicked.connect(self.dna_conversion)
        self.ui.clear.clicked.connect(self.cler_forms)

        self.setMouseTracking(True)

        self.show()
        self.ui.error_console.hide()

    def exit_app(self):
        sys.exit()

    def min_app(self):
        self.showMinimized() 
        print("Passed: App successfully minimized.")

    def max_app(self):
        if not self.isMaximized():
            self.geometry = self.saveGeometry()
            self.showMaximized()

        else:
            self.restoreGeometry(self.geometry)

    def dna_conversion(self):

        self.ui.rna_output.setText("")
        self.ui.protein_output.setText("")
        self.ui.error_console.hide()
        
        DNA = self.ui.dna_taker.text()

        if DNA == "":
            self.ui.error_console.setText("ERROR: Please enter a DNA sequence")
            self.ui.error_console.show()
            print("Passed: ERRORnull successfully displayed.")
            return

        DNA = DNA_input(DNA)
        
        if DNA == 'ERROR1':
            self.ui.error_console.setText('ERROR: Length of DNA must be multiple of 3 (barcodes)')
            self.ui.error_console.show()
            print("Passed: ERROR1 successfully displayed.")

        elif DNA == 'ERROR2':
            self.ui.error_console.setText('ERROR: Bases(s) are incorrect...')
            self.ui.error_console.show()
            print("Passed: ERROR2 successfully displayed.")

        else:
            
            self.ui.error_console.hide()
            RNA = DNA_to_RNA(DNA)
            proteinList = get_amino_acid(RNA)
            proteins = ', '.join(proteinList)

            self.ui.dna_taker.setText(DNA.upper())
            self.ui.rna_output.setText(RNA.upper())
            print("Passed: RNA successfully outputted")
            self.ui.protein_output.setText(proteins)
            print("Passed: Protein strands successfully outputted.")

    def cler_forms(self):
        self.ui.dna_taker.setText(" ")
        self.ui.rna_output.setText("")
        self.ui.protein_output.setText("")
        self.ui.error_console.hide()

    ## Movable Title Bar

    def mousePressEvent(self, event):

        self.ui.title_bar.isPressed = True
        self.startPos = event.globalPos()
        return QWidget().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.ui.title_bar.isPressed = False
        return QWidget().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self.ui.title_bar.isPressed:

            if self.isMaximized:
                self.showNormal()

            movePos = event.globalPos() - self.startPos
            self.startPos = event.globalPos()
            self.move(self.pos() + movePos)

        return QWidget().mouseMoveEvent(event)

    ##


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    app.exec_()
