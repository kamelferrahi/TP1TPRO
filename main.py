from PyQt5.QtWidgets import QApplication
from Classe.Menu import Menu

if __name__ == "__main__":
    
    app = QApplication([])
    widget = Menu()
    widget.show()
    app.exec()