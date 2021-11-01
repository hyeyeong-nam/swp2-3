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
        self.setGeometry(300, 300, 500, 600)
        self.setWindowTitle('Assignment6')

        name = QLabel("Name: ", self)
        self.nameEdit = QLineEdit()

        age = QLabel("Age: ", self)
        self.ageEdit = QLineEdit(self)

        score = QLabel("Score: ", self)
        self.scoreEdit = QLineEdit(self)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(name)
        hbox1.addWidget(self.nameEdit)
        hbox1.addWidget(age)
        hbox1.addWidget(self.ageEdit)
        hbox1.addWidget(score)
        hbox1.addWidget(self.scoreEdit)
        hbox1.addStretch(1)

        amount = QLabel("Amount: ", self)
        self.amountEdit = QLineEdit(self)

        key = QLabel("Key: ", self)
        self.keyEdit = QComboBox(self)
        self.keyEdit.addItem("Name")
        self.keyEdit.addItem("Age")
        self.keyEdit.addItem("Score")

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(amount)
        hbox2.addWidget(self.amountEdit)
        hbox2.addWidget(key)
        hbox2.addWidget(self.keyEdit)

        self.add = QPushButton("Add", self)
        self.delete = QPushButton("Del", self)
        self.find = QPushButton("Find", self)
        self.inc = QPushButton("Inc", self)
        self.showdb = QPushButton("Show", self)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.add)
        hbox3.addWidget(self.delete)
        hbox3.addWidget(self.find)
        hbox3.addWidget(self.inc)
        hbox3.addWidget(self.showdb)

        result = QLabel("Result: ", self)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(result)
        hbox4.addStretch(1)

        self.resultWindow = QTextEdit(self)
        self.resultWindow.setReadOnly(True)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.resultWindow)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        self.add.clicked.connect(self.buttonClicked)
        self.delete.clicked.connect(self.buttonClicked)
        self.find.clicked.connect(self.buttonClicked)
        self.inc.clicked.connect(self.buttonClicked)
        self.showdb.clicked.connect(self.buttonClicked)

        self.setLayout(vbox)
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

    def showScoreDB(self):
        pass

    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        find = False
        if key == "Add":
            record = {'Name':self.nameEdit.text(), 'Age':int(self.ageEdit.text()), 'Score':int(self.scoreEdit.text())}
            self.scoredb += [record]
        elif key == "Del":
            repeat = True
            while (repeat):
                repeat = True
                for p in self.scoredb:
                    if p['Name'] == self.nameEdit.text():
                        self.scoredb.remove(p)
                        break
                else:
                    repeat = False
        elif key == "Find":
            find = True
            findKey = self.nameEdit.text()
        elif key == "Inc":
            for p in self.scoredb:
                if self.nameEdit.text() == p['Name']:
                    p['Score'] += int(self.amountEdit.text())
        s = ""
        for p in sorted(self.scoredb, key=lambda person: person[self.keyEdit.currentText()]):
            for attr in sorted(p):
                if find:
                    if p["Name"] == findKey:
                        s += "%-16s" % (str(attr)+" = "+str(p[attr]))
                        s += "\t"
                else:
                    s += "%-16s" % (str(attr) + " = " + str(p[attr]))
                    s += "\t"
            if find:
                if p["Name"] == findKey:
                    s += "\n"
            else:
                s += "\n"
        self.resultWindow.setText(s)


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

