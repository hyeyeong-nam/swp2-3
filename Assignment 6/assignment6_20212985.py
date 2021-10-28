from os import name
import pickle
import sys
from PyQt5.QtWidgets import (QGridLayout, QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import QLine, Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        Name = QLabel("Name:") 
        Age = QLabel("Age:")
        Score = QLabel("Score:")   
        Amount = QLabel("Amount:")
        Key = QLabel("Key:")
        Result = QLabel("Result:")

        self.NameEdit = QLineEdit()
        self.AgeEdit = QLineEdit()
        self.ScoreEdit = QLineEdit()
        self.AmountEdit = QLineEdit()
        self.KeyEdit = QComboBox()
        self.ResultEdit = QTextEdit()
        self.ResultEdit.setReadOnly(True)

        addButton = QPushButton("Add")
        delButton = QPushButton("Del")
        findButton = QPushButton("Find")
        incButton = QPushButton("Inc")
        showButton = QPushButton("Show")

        self.KeyEdit.addItem("Name")
        self.KeyEdit.addItem("Age")
        self.KeyEdit.addItem("Score")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        
        hbox.addWidget(Name)
        hbox.addWidget(self.NameEdit)

        hbox.addWidget(Age)
        hbox.addWidget(self.AgeEdit)

        hbox.addWidget(Score)
        hbox.addWidget(self.ScoreEdit)

        hbox.addStretch(1)
        
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)

        hbox1.addWidget(Amount)
        hbox1.addWidget(self.AmountEdit)
        hbox1.addWidget(Key)
        hbox1.addWidget(self.KeyEdit)
        

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)

        hbox2.addWidget(addButton)
        hbox2.addWidget(delButton)
        hbox2.addWidget(findButton)
        hbox2.addWidget(incButton)
        hbox2.addWidget(showButton)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(Result)
        hbox3.addStretch(1)
        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.ResultEdit)

        vbox = QVBoxLayout()
        
        vbox.addLayout(hbox)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addStretch(1)
        
        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 300)
        self.show()

        addButton.clicked.connect(self.ClickedAdd)
        delButton.clicked.connect(self.ClickedDel)
        findButton.clicked.connect(self.ClickedFind)
        incButton.clicked.connect(self.ClickedInc)
        showButton.clicked.connect(self.showScoreDB)

    def ClickedAdd(self):
        
        Name = self.NameEdit.text()
        Age = int(self.AgeEdit.text())
        Score = int(self.ScoreEdit.text())
        self.scoredb.append({'Name':Name, 'Age':Age, 'Score':Score})
        self.showScoreDB()

    def ClickedDel(self):
        Name = self.NameEdit.text()
        has_deleted = True
        while has_deleted:
            has_deleted = False
            for p in self.scoredb:
                if p['Name'] == Name:
                    self.scoredb.remove(p)
                    has_deleted = True
        self.showScoreDB()
    def ClickedFind(self):
        Name = self.NameEdit.text()
        self.showScoreDB(Name)
    
    def ClickedInc(self):
        Name = self.NameEdit.text()
        Amount = int(self.AmountEdit.text())
        for p in self.scoredb:
            if p['Name'] == Name:
                p['Score'] = str(int(p['Score']) + int(Amount))
        self.showScoreDB()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self, Name=None):
        sort_key = self.KeyEdit.currentText()

        te = []

        for p in sorted(self.scoredb, key=lambda person: person[sort_key]):
            if Name != None and Name != p['Name']:
                continue

            for attr in sorted(p):
                te.append(str(attr) + ":")
                te.append('\t')
                te.append(str(p[attr]))
                te.append("\t")
        
        self.ResultEdit.setText(''.join(te))
        
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

