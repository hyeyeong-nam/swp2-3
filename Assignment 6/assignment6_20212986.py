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
        self.KeyEdit.addItem("Name")
        self.KeyEdit.addItem("Age")
        self.KeyEdit.addItem("Score")
        self.ResultEdit = QTextEdit()
        self.ResultEdit.setReadOnly(True)

        Add = QPushButton("Add")
        Del = QPushButton("Del")
        Find = QPushButton("Find")
        Inc = QPushButton("Inc")
        Show = QPushButton("Show")

        hbox = QHBoxLayout()
        hbox.addStretch(1)

        hbox.addWidget(Name)
        hbox.addWidget(self.NameEdit)
        hbox.addWidget(Age)
        hbox.addWidget(self.AgeEdit)
        hbox.addWidget(Score)
        hbox.addWidget(self.ScoreEdit)
        hbox.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)

        hbox2.addWidget(Amount)
        hbox2.addWidget(self.AmountEdit)
        hbox2.addWidget(Key)
        hbox2.addWidget(self.KeyEdit)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)

        hbox3.addWidget(Add)
        hbox3.addWidget(Del)
        hbox3.addWidget(Find)
        hbox3.addWidget(Inc)
        hbox3.addWidget(Show)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(Result)

        hbox5 = QHBoxLayout()
        hbox5.addStretch(1)
        hbox5.addWidget(self.ResultEdit)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addStretch(1)


        Add.clicked.connect(self.ToAdd)
        Del.clicked.connect(self.ToDel)
        Find.clicked.connect(self.ToFind)
        Inc.clicked.connect(self.ToInc)
        Show.clicked.connect(self.ToShow)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 250)

        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
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

    def ToAdd(self):
        Name = self.NameEdit.text()
        Age = int(self.AgeEdit.text())
        Score = int(self.ScoreEdit.text())
        record = {'Name': Name, 'Age': Age, 'Score': Score}
        self.scoredb += [record]
        self.showScoreDB()

    def ToDel(self):
        Name = self.NameEdit.text()
        a = True
        while a:
            a = False
            for p in self.scoredb:
                if p['Name'] == Name:
                    self.remove(p)
                    a = True
        self.showScoreDB()

    def ToFind(self):
        Name = self.NameEdit.text()
        for p in self.scoredb:
            if p['Name'] == Name:
                print("Age=" + str(p['Age']), "Name=" + p['Name'], "Score=" + str(p['Score']))
        self.showScoreDB()

    def ToInc(self):
        Name = self.NameEdit.text()
        Amount = int(self.AmountEdit.text())
        for p in self.scoredb:
            if p['Name'] == Name:
                p['Score'] = str(int(p['Score']) + int(Amount))
        self.showScoreDB()

    def ToShow(self):
        sortK = self.KeyEdit.currentText()
        for p in sorted(self.scoredb, key=lambda person: person[sortK]):
            for attr in sorted(p):
                print(str(attr) + "=" + str(p[attr]), end=' ')

    def showScoreDB(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

#Name = QLabel("Name:")
