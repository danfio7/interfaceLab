from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sys
 
 
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"C:\Users\TEMP\Documents\helpOur\mainwindow.ui", self)
 
        # find the widgets in the xml file
 
        self.table = self.findChild(QTableWidget, "table1")
        self.button = self.findChild(QPushButton, "push1")
        self.button.clicked.connect(self.clickedBtn)
        self.table.setColumnCount(2)
        self.table.setRowCount(2)
        self.table.setHorizontalHeaderLabels(["nome"])
 
        self.show()
 
 
 
    def clickedBtn(self):
        
        lista = [{"nome": "pippo", "cognome": "baudo", "nOre": 4}, {"nome": "p", "cognome": "b", "nOre": 6}]
        for x in lista:
            item_nome = QTableWidgetItem(x["nome"])
            self.table.setItem(item_nome)

app = QApplication(sys.argv)
window = UI()
app.exec_()
