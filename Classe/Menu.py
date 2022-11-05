from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QStyleFactory, QCompleter,QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal, QRect
from PyQt5.uic import loadUi
from .AjoutObjets import AjoutObjets
from .AlgorithmeduSac import ProblemeduSac
from .Resultat import Resultat
from PySide2 import QtWidgets
from PySide2.QtWidgets import QHeaderView

class Menu(QDialog):
    def __init__(self):
        super(Menu, self).__init__()
        fermerSignal = pyqtSignal()
        loadUi("UI/Menu.ui",self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ok.clicked.connect(self.Executer)
        self.ajouter.clicked.connect(self.Ajouter)
        self.Re.clicked.connect(self.Reinialiter)
        self.supprimer.clicked.connect(self.suppression)
        self.Deco.clicked.connect(self.close)
        self.Objets = list()
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnWidth(0,400)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(3,200)
        

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
            self.erreur("Erreur","Le poid maximal doit étre spécifié et doit etre un entier")
    
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
    
    def erreur(self,title,message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setWindowFlag(0x00000800)
        msg.setText(message)
        msg.setStyleSheet('''QMessageBox{
                                          border: 3px solid #FF5051;
                                          background : white;
                                          border-radius: 15px;
                                          width : 288px;
                                          height : 131px;
                                          }
                                          QPushButton{
                                          background-color : white;
                                          width : 53px;
                                          height : 28px;
                                          border: 1px solid #FF5051;
                                          border-radius : 15px;   
                                          color : #FF5051;
                                          font-family:"Sitka Text";
                                          font-size : 13px;                             
                                           }
                                          QPushButton:hover{
                                          background-color: #FF5051;
                                          color : white;
                                          }
                                          QLabel{
                                          font-family: "Sitka Text";
                                          font-size : 13px;
                                          color : #666666;
                                          width : 192px;
                                          height : 32px;
                                           }''')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()  

