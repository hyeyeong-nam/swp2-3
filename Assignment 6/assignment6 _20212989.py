import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        Name = QLabel("Name:")
        Age = QLabel("Age:")
        Score = QLabel("Score:")
        Amount = QLabel("Amount:")

        self.Nameline = QLineEdit()
        self.Ageline = QLineEdit()
        self.Scoreline = QLineEdit()
        self.Amountline = QLineEdit()

        AddButten = QPushButton("Add")
        DelButten = QPushButton("Del")
        FindButten = QPushButton("Find")
        IncButten = QPushButton("Inc")
        ShowButten = QPushButton("Show")

        Result = QLabel("Result:")
        self.ResultText = QTextEdit()
        Key = QLabel("Key:")
        self.KeyBox = QComboBox()
        self.KeyBox.addItem('Name')
        self.KeyBox.addItem('Age')
        self.KeyBox.addItem('Score')

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(Name)
        hbox1.addWidget(self.Nameline)
        hbox1.addWidget(Age)
        hbox1.addWidget(self.Ageline)
        hbox1.addWidget(Score)
        hbox1.addWidget(self.Scoreline)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(Amount)
        hbox2.addWidget(self.Amountline)
        hbox2.addWidget(Key)
        hbox2.addWidget(self.KeyBox)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(AddButten)
        hbox3.addWidget(DelButten)
        hbox3.addWidget(FindButten)
        hbox3.addWidget(IncButten)
        hbox3.addWidget(ShowButten)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(Result)
        hbox4.addStretch(1)
        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.ResultText)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addStretch(1)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

        AddButten.clicked.connect(self.addScoreDB)
        DelButten.clicked.connect(self.delScoreDB)
        FindButten.clicked.connect(self.findScoreDB)
        IncButten.clicked.connect(self.incScoreDB)
        ShowButten.clicked.connect(self.showScoreDB)



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
        sort_key = self.KeyBox.currentText()

        a = []

        for p in sorted(self.scoredb, key=lambda person: person[sort_key]):

            for k in sorted(p):
                a.append(str(k) + ":")
                a.append(str(p[k]))
                a.append("\t")
            a.append("\n")
        self.ResultText.setText(''.join(a))

    def addScoreDB(self):
        Name = self.Nameline.text()
        Age = int(self.Ageline.text())
        Score = int(self.Scoreline.text())
        self.scoredb.append({'Name': Name, 'Age': Age, 'Score': Score})
        self.showScoreDB()

    def delScoreDB(self):
        Name = self.Nameline.text()
        for p in reversed(self.scoredb):
            if p['Name'] == Name:
                self.scoredb.remove(p)
        self.showScoreDB()

    def incScoreDB(self):
        Name = self.Nameline.text()
        Amount = self.Amountline.text()
        for p in self.scoredb:
            if p['Name'] == Name:
                p['Score'] = str(int(p['Score']) + int(Amount))
        self.showScoreDB()

    def findScoreDB(self):
        Name = self.Nameline.text()
        self.showScoreDB(Name)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())