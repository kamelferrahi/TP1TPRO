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
            self.erreur("Erreur","Poid et valeur doivent etre des nombre entiers")
    
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
