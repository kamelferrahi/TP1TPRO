from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QStyleFactory, QCompleter,QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal, QRect
from PyQt5.uic import loadUi


class Resultat(QDialog):
    def __init__(self,sac,cout):
        super(Resultat, self).__init__()
        loadUi("./UI/Resultat.ui",self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.sac = sac
        self.cout = cout
        self.loadData()
        self.ok.clicked.connect(self.close)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnWidth(0,400)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(3,200)

    def loadData(self):
        self.label.setText("Cout = "+str(self.cout))
        self.tableWidget.setRowCount(len(self.sac))
        i = 0
    
        for objet in self.sac:
            self.tableWidget.setItem(i,1,QTableWidgetItem(str(objet["poid"])))
            self.tableWidget.setItem(i,2,QTableWidgetItem(str(objet["valeur"])))
            self.tableWidget.setItem(i,0,QTableWidgetItem(objet["nom"]))
            i+=1

    
