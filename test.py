from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sys
 
 
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"C:\Users\danielefiorucci1\Downloads\interfaceLab-main\interfaceLab-main\mainwindow.ui", self)
 
        # find the widgets in the xml file
 
        self.table = self.findChild(QTableWidget, "table1")
        self.button0 = self.findChild(QPushButton, "push0")
        self.button0.clicked.connect(self.inserisciRighe)
        self.button1 = self.findChild(QPushButton, "push1")
        self.button1.clicked.connect(self.inserisciDocenti)
        self.table.setColumnCount(3)
        self.table.setRowCount(2)
        self.table.setHorizontalHeaderLabels(["nomeP", "nomeA", "nOre"])
 
        self.show()
 
        self.lista = [{"nomeProf": "matteoPicciolini", "nomeAlunno": "danieleFiorucci", "nOre": "4"}, 
             {"nomeProf": "cristianaNeri", "nomeAlunno": "micheleBellucci", "nOre": "6"}, 
             {"nomeProf": "edoardoPanfili", "nomeAlunno": "lorenzoScanu", "nOre": "8"}]

    def inserisciRighe(self):
        self.table.setRowCount(len(self.lista))
    def inserisciDocenti(self):
        riga=0
        for x in self.lista:
            item_nomeProf = QTableWidgetItem(x["nomeProf"])
            item_nomeAlunno = QTableWidgetItem(x["nomeAlunno"])
            item_nOre = QTableWidgetItem(x["nOre"])
            self.table.setItem(riga, 0, item_nomeProf)
            self.table.setItem(riga, 1, item_nomeAlunno)
            self.table.setItem(riga, 2, item_nOre)
            riga+=1
            

app = QApplication(sys.argv)
window = UI()
app.exec_()
