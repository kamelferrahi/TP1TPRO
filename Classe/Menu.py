from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QStyleFactory, QCompleter,QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal, QRect
from PyQt5.uic import loadUi
from .AjoutObjets import AjoutObjets
from .AlgorithmeduSac import ProblemeduSac
from .Resultat import Resultat

class Menu(QDialog):
    def __init__(self):
        super(Menu, self).__init__()
        loadUi("UI/Menu.ui",self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ok.clicked.connect(self.Executer)
        self.ajouter.clicked.connect(self.Ajouter)
        self.Re.clicked.connect(self.Reinialiter)
        self.supprimer.clicked.connect(self.suppression)
        self.Objets = list()

    def Ajouter(self):
        self.window = AjoutObjets()
        self.window.show()
        self.window.SigClicked.connect(lambda nom,poid,valeur: self.loadData(nom,poid,valeur))

    def loadData(self,nom,poid,valeur):

        self.Objets.append({
            "valeur":valeur,"nom":nom,"poid":poid
        })
        self.tableWidget.setRowCount(len(self.Objets))
        i = len(self.Objets)-1
        objet = self.Objets[i]
        self.tableWidget.setItem(i,1,QTableWidgetItem(str(objet["poid"])))
        self.tableWidget.setItem(i,2,QTableWidgetItem(str(objet["valeur"])))
        self.tableWidget.setItem(i,0,QTableWidgetItem(objet["nom"]))
    
    

    def Executer(self):
        try:
            wmax = int(self.filtre.text())
            res = ProblemeduSac(self.Objets,wmax)
            sac = list()
            for index in res[1]:
                sac.append(self.Objets[index])
            self.window = Resultat(sac,res[0])
            self.window.show()
        except:
            self.messagebox("Erreur","Le poid maximal doit étre spécifié et doit etre un entier")
    
    def Reinialiter(self):
        self.Objets = list()
        self.tableWidget.setRowCount(0)

    def suppression(self):
        index = self.tableWidget.currentRow()
        self.Objets.pop(index)
        self.tableWidget.setRowCount(len(self.Objets))
        i = 0
    
        for objet in self.Objets:
            self.tableWidget.setItem(i,1,QTableWidgetItem(str(objet["poid"])))
            self.tableWidget.setItem(i,2,QTableWidgetItem(str(objet["valeur"])))
            self.tableWidget.setItem(i,0,QTableWidgetItem(objet["nom"]))
            i+=1
    
    def messagebox(self,title,message):

        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()  

