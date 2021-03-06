#-*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton

from hangman import Hangman
from guess import Guess
from word import Word


class HangmanGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize word database
        self.word = Word('words.txt')

        # Hangman display window
        self.hangmanWindow = QTextEdit()
        self.hangmanWindow.setReadOnly(True)
        self.hangmanWindow.setAlignment(Qt.AlignLeft)
        font = self.hangmanWindow.font()
        font.setFamily('Courier New')
        self.hangmanWindow.setFont(font)

        # Layout
        hangmanLayout = QGridLayout()
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)

        # Status Layout creation
        statusLayout = QGridLayout()

        # Display widget for current status
        self.currentWord = QLineEdit()
        self.currentWord.setReadOnly(True)
        self.currentWord.setAlignment(Qt.AlignCenter)
        font = self.currentWord.font()
        font.setPointSize(font.pointSize() + 8)
        self.currentWord.setFont(font)
        self.currentWord.setFixedWidth(390)
        statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)

        # Display widget for already used characters
        self.guessedChars = QLineEdit()
        self.guessedChars.setReadOnly(True)
        self.guessedChars.setAlignment(Qt.AlignLeft)
        self.guessedChars.setMaxLength(52)
        statusLayout.addWidget(self.guessedChars, 1, 0, 1, 2)

        # Display widget for message output
        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignLeft)
        self.message.setMaxLength(52)
        statusLayout.addWidget(self.message, 2, 0, 1, 2)

        # Input widget for user selected characters
        self.charInput = QLineEdit()
        self.charInput.setMaxLength(1)
        statusLayout.addWidget(self.charInput, 3, 0)

        # Button for submitting a character
        self.guessButton = QToolButton()
        self.guessButton.setText('Guess!')
        self.guessButton.clicked.connect(self.guessClicked)
        statusLayout.addWidget(self.guessButton, 3, 1)

        # Button for a new game
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.clicked.connect(self.startGame)
        statusLayout.addWidget(self.newGameButton, 4, 0)

        # Layout placement
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(hangmanLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 0, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle('Hangman Game')

        # Start a new game on application launch!
        self.startGame()


    def startGame(self):
        self.hangman = Hangman()
        self.guess = Guess(self.word.randFromDB(3))
        self.gameOver = False

        self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
        self.currentWord.setText(self.guess.displayCurrent())
        self.guessedChars.setText(self.guess.displayGuessed())
        self.message.clear()


    def guessClicked(self):
        guessedChar = self.charInput.text()
        self.charInput.clear()
        self.message.clear()
        boobean = True
        if self.gameOver == True:
            # ????????? ???????????? - message.setText() - ??????
            #self.message.setText('restart Game!')
            return self.startGame()


        # ????????? ????????? 1 ????????? ????????????, ?????? ?????? ????????? ??????, ??????
        if len(guessedChar) != 1:

            return self.message.setText('One character at a time!')

        # ?????? ????????? ??????????????? ????????????, ?????? ?????? ????????? ??????, ??????
        if guessedChar in self.guess.guessedChars:
            self.message.setText('You already guessed \"' + guessedChar + '\"')
            boobean = False
        success = self.guess.guess(guessedChar)
        if success == False and boobean:
            # ?????? ?????? ????????? 1 ?????? ??????
            # ????????? ??????
            self.hangman.decreaseLife()
            self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
            self.guessedChars.setText(self.guess.displayGuessed())

        # hangmanWindow ??? ?????? hangman ?????? ????????? ??????
        # currentWord ??? ???????????? ??????????????? ???????????? ?????? ????????? ??????
        # guessedChars ??? ???????????? ????????? ???????????? ????????? ??????
        elif success == True:
            self.currentWord.setText(self.guess.displayCurrent())
            self.guessedChars.setText(self.guess.displayGuessed())
        if self.guess.finished() == True:
            # ????????? ("Success!") ????????????, self.gameOver ??? True ???
            self.hangmanWindow.setPlaceholderText('**** ' + self.guess.displayCurrent() + ' ****\n' 'Success')
            self.gameOver = True


        elif self.hangman.getRemainingLives() == 0:
            # ????????? ("Fail!" + ?????? ??????) ????????????, self.gameOver ??? True ???
            self.hangmanWindow.setPlaceholderText(self.hangman.currentShape() +'\n' + 'word [' + self.guess.secretWord + ']\n'+'guess [' + self.guess.displayCurrent() + ']\n'+'Fail')
            self.gameOver = True

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = HangmanGame()
    game.show()
    sys.exit(app.exec_())
