from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QStyleFactory, QCompleter, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal, QRect
from PyQt5.uic import loadUi

class AjoutObjets(QDialog):
    SigClicked = pyqtSignal(str,int,int)
    def __init__(self):
        super(AjoutObjets, self).__init__()
        loadUi("UI/AjoutObjets.ui",self)
        self.setWindowFlag(Qt.FramelessWindowHint)
       
        self.annuler.clicked.connect(self.close)
        self.ajouter.clicked.connect(self.ajouterObjet)
    
    def ajouterObjet(self):
        try:
            nom = self.nom.text()
            poid = int(self.poid.text())
            valeur = int(self.valeur.text())

            self.SigClicked.emit(nom,poid,valeur)
            self.close()
        except:
            self.messagebox("Erreur","Poid et valeur doivent etre des nombre entiers")
    
    def messagebox(self,title,message):

        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
