# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:19:10 2024

@author: danielefiorucci1
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sys
import csv
from csv import DictWriter
 
 
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"ui/mainwindow.ui", self)
 
        # find the widgets in the xml file
        self.button = self.findChild(QPushButton, "pushProfs")
        self.button.clicked.connect(self.chargeProfs)
        
        self.table = self.findChild(QTableWidget, "tableProfs")
        self.table.setColumnCount(3)
        self.table.setRowCount(3)
        self.table.setHorizontalHeaderLabels(["Nome", "Cognome","Ore"])
        
        self.show()
    
    def chargeProfs(self):
        profDictionary={}

        fileIn=open("input/docenti.csv", "r", encoding="utf-8")
        reader = csv.DictReader(fileIn)

        dati = []

        for prova in reader:
            dati.append(prova)
        fileIn.close()
            
        print(dati)
        
        riga=0
        
        for element in dati:
            item_name = QTableWidgetItem(element["Nome"])
            self.table.setItem(riga,0, item_name)
            
            item_name2 = QTableWidgetItem(element["Cognome"])
            self.table.setItem(riga,1, item_name2)
           
            item_name3 = QTableWidgetItem(element["Ore"])
            self.table.setItem(riga,2, item_name3)
            riga=riga+1
            
app = QApplication(sys.argv)
window = UI()
app.exec_()