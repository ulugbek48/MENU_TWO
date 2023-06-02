import sys
import random


from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QLabel, QMainWindow, QApplication, QStackedWidget, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import *
from password import Password
from passwordcore import PasswordCore



class WelcomeScreen(QDialog):
    def __init__(self) -> None:
        super(WelcomeScreen, self).__init__()
        loadUi("TIT.ui", self)
        self.login.clicked.connect(self.gotologin)
        self.createacc.clicked.connect(self.gotocreate)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def gotocreate(self):
        create = CreateAccScrean()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)




class LoginScreen(QDialog):
    def __init__(self) -> None:
        super(LoginScreen, self).__init__()
        loadUi("login.ui", self)
        self.passwordcore = PasswordCore()
        self.passwordfeld.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_p.clicked.connect(self.loginfunction)


    def loginfunction(self):
        user = self.emailfeld.text()
        pasword = self.passwordfeld.text()
        

        if len(user)==0 or len(pasword)==0:
            self.error.setText("Please input all fields.")

        else:
            data = self.passwordcore.selectAllUsers(user, pasword)
            if data != -1:
                self.error.setText("")
                login_p = Menu()
                widget.addWidget(login_p)
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:

                self.error.setText("Invalid username or password")






class Menu(QDialog):
    def __init__(self) -> None:
        super(Menu, self).__init__()
        loadUi("menu.ui", self)
        self.calculator.clicked.connect(self.calCulator)
        self.xofeld.clicked.connect(self.XandO)
        self.profilefeld.clicked.connect(self.myprofile)
        self.tetrisfeld.clicked.connect(self.tetrisGame)





    def tetrisGame(self):
        tetgame = Tetris()
        widget.addWidget(tetgame)
        widget.setCurrentIndex(widget.currentIndex()+1)




    def calCulator(self):
        cal = Windowca()
        widget.addWidget(cal)
        widget.setCurrentIndex(widget.currentIndex()+1)

        



    def XandO(self):
        gamexo = Window()
        widget.addWidget(gamexo)
        widget.setCurrentIndex(widget.currentIndex()+1)



    def myprofile(self):
       profile = MyProfile()
       widget.addWidget(profile)
       widget.setCurrentIndex(widget.currentIndex()+1)



class Windowca(QMainWindow):
 
    def __init__(self):
        super().__init__()
 
        # setting title
        self.setWindowTitle("Python ")
 
        # setting geometry
        self.setGeometry(100, 100, 360, 350)
 
        # calling method
        self.UiComponents()
 
        # showing all the widgets
        self.show()
 
        # method for widgets
    def UiComponents(self):
 
        # creating a label
        self.label = QLabel(self)
 
        # setting geometry to the label
        self.label.setGeometry(5, 5, 350, 70)
 
        # creating label multi line
        self.label.setWordWrap(True)
 
        # setting style sheet to the label
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid black;"
                                 "background : white;"
                                 "}")
 
        # setting alignment to the label
        self.label.setAlignment(Qt.AlignRight)
 
        # setting font
        self.label.setFont(QFont('Arial', 15))
 
 
        # adding number button to the screen
        # creating a push button
        push1 = QPushButton("1", self)
 
        # setting geometry
        push1.setGeometry(5, 150, 80, 40)
 
        # creating a push button
        push2 = QPushButton("2", self)
 
        # setting geometry
        push2.setGeometry(95, 150, 80, 40)
 
        # creating a push button
        push3 = QPushButton("3", self)
 
        # setting geometry
        push3.setGeometry(185, 150, 80, 40)
 
        # creating a push button
        push4 = QPushButton("4", self)
 
        # setting geometry
        push4.setGeometry(5, 200, 80, 40)
 
        # creating a push button
        push5 = QPushButton("5", self)
 
        # setting geometry
        push5.setGeometry(95, 200, 80, 40)
 
        # creating a push button
        push6 = QPushButton("5", self)
 
        # setting geometry
        push6.setGeometry(185, 200, 80, 40)
 
        # creating a push button
        push7 = QPushButton("7", self)
 
        # setting geometry
        push7.setGeometry(5, 250, 80, 40)
 
        # creating a push button
        push8 = QPushButton("8", self)
 
        # setting geometry
        push8.setGeometry(95, 250, 80, 40)
 
        # creating a push button
        push9 = QPushButton("9", self)
 
        # setting geometry
        push9.setGeometry(185, 250, 80, 40)
 
        # creating a push button
        push0 = QPushButton("0", self)
 
        # setting geometry
        push0.setGeometry(5, 300, 80, 40)
 
        # adding operator push button
        # creating push button
        push_equal = QPushButton("=", self)
 
        # setting geometry
        push_equal.setGeometry(275, 300, 80, 40)
 
        # adding equal button a color effect
        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.blue)
        push_equal.setGraphicsEffect(c_effect)
 
        # creating push button
        push_plus = QPushButton("+", self)
 
        # setting geometry
        push_plus.setGeometry(275, 250, 80, 40)
 
        # creating push button
        push_minus = QPushButton("-", self)
 
        # setting geometry
        push_minus.setGeometry(275, 200, 80, 40)
 
        # creating push button
        push_mul = QPushButton("*", self)
 
        # setting geometry
        push_mul.setGeometry(275, 150, 80, 40)
 
        # creating push button
        push_div = QPushButton("/", self)
 
        # setting geometry
        push_div.setGeometry(185, 300, 80, 40)
 
        # creating push button
        push_point = QPushButton(".", self)
 
        # setting geometry
        push_point.setGeometry(95, 300, 80, 40)
 
 
        # clear button
        push_clear = QPushButton("Clear", self)
        push_clear.setGeometry(5, 100, 145, 40)
 
        # del one character button
        push_del = QPushButton("Del", self)
        push_del.setGeometry(210, 100, 145, 40)

        push_menu = QPushButton("Menu", self)
        push_menu.setGeometry(100, 100, 145, 40)
 
        # adding action to each of the button
        push_minus.clicked.connect(self.action_minus)
        push_equal.clicked.connect(self.action_equal)
        push0.clicked.connect(self.action0)
        push1.clicked.connect(self.action1)
        push2.clicked.connect(self.action2)
        push3.clicked.connect(self.action3)
        push4.clicked.connect(self.action4)
        push5.clicked.connect(self.action5)
        push6.clicked.connect(self.action6)
        push7.clicked.connect(self.action7)
        push8.clicked.connect(self.action8)
        push9.clicked.connect(self.action9)
        push_div.clicked.connect(self.action_div)
        push_mul.clicked.connect(self.action_mul)
        push_plus.clicked.connect(self.action_plus)
        push_point.clicked.connect(self.action_point)
        push_clear.clicked.connect(self.action_clear)
        push_del.clicked.connect(self.action_del)
        push_menu.clicked.connect(self.action_menu)
 
    def action_equal(self):
 
        # get the label text
        equation = self.label.text()
 
        try:
            # getting the ans
            ans = eval(equation)
 
            # setting text to the label
            self.label.setText(str(ans))
 
        except:
            # setting text to the label
            self.label.setText("Wrong Input")
 
    def action_plus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " + ")
 
    def action_minus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " - ")
 
    def action_div(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " / ")
 
    def action_mul(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " * ")
 
    def action_point(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + ".")
 
    def action0(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "0")
 
    def action1(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "1")
 
    def action2(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "2")
 
    def action3(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "3")
 
    def action4(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "4")
 
    def action5(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "5")
 
    def action6(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "6")
 
    def action7(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "7")
 
    def action8(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "8")
 
    def action9(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "9")
 
    def action_clear(self):
        # clearing the label text
        self.label.setText("")
 
    def action_del(self):
        # clearing a single digit
        text = self.label.text()
        print(text[:len(text)-1])
        self.label.setText(text[:len(text)-1])

    def action_menu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
 
 







class Tetris(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        """initiates application UI"""

        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)

        self.tboard.start()

        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris')
        self.show()

    def center(self):
        """centers the window on the screen"""

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2),
                  int((screen.height() - size.height()) / 2))


class Board(QFrame):
    msg2Statusbar = pyqtSignal(str)
    

    BoardWidth = 10
    BoardHeight = 22
    Speed = 300

    def __init__(self, parent):
        super().__init__(parent)
        self.initBoard()

    def initBoard(self):
        """initiates board"""

        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False

        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []

        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()

    def shapeAt(self, x, y):
        """determines shape at the board position"""

        return self.board[(y * Board.BoardWidth) + x]

    def setShapeAt(self, x, y, shape):
        """sets a shape at the board"""

        self.board[(y * Board.BoardWidth) + x] = shape

    def squareWidth(self):
        """returns the width of one square"""

        return self.contentsRect().width() // Board.BoardWidth

    def squareHeight(self):
        """returns the height of one square"""

        return self.contentsRect().height() // Board.BoardHeight

    def start(self):
        """starts game"""

        if self.isPaused:
            return

        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()

        self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.newPiece()
        self.timer.start(Board.Speed, self)

    def pause(self):
        """pauses game"""

        if not self.isStarted:
            return

        self.isPaused = not self.isPaused

        if self.isPaused:
            self.timer.stop()
            self.msg2Statusbar.emit("paused")

        else:
            self.timer.start(Board.Speed, self)
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.update()

    def paintEvent(self, event):
        """paints all shapes of the game"""

        painter = QPainter(self)
        rect = self.contentsRect()

        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()

        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shapeAt(j, Board.BoardHeight - i - 1)

                if shape != Tetrominoe.NoShape:
                    self.drawSquare(painter,
                                    rect.left() + j * self.squareWidth(),
                                    boardTop + i * self.squareHeight(), shape)

        if self.curPiece.shape() != Tetrominoe.NoShape:

            for i in range(4):
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                                boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
                                self.curPiece.shape())

    def keyPressEvent(self, event):
        """processes key press events"""

        if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
            super(Board, self).keyPressEvent(event)
            return

        key = event.key()

        if key == Qt.Key_P:
            self.pause()
            return

        if self.isPaused:
            return

        elif key == Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)

        elif key == Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)

        elif key == Qt.Key_Down:
            self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)

        elif key == Qt.Key_Up:
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)

        elif key == Qt.Key_Space:
            self.dropDown()

        elif key == Qt.Key_D:
            self.oneLineDown()

        else:
            super(Board, self).keyPressEvent(event)

    def timerEvent(self, event):
        """handles timer event"""

        if event.timerId() == self.timer.timerId():

            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()

        else:
            super(Board, self).timerEvent(event)

    def clearBoard(self):
        """clears shapes from the board"""

        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetrominoe.NoShape)

    def dropDown(self):
        """drops down a shape"""

        newY = self.curY

        while newY > 0:

            if not self.tryMove(self.curPiece, self.curX, newY - 1):
                break

            newY -= 1

        self.pieceDropped()

    def oneLineDown(self):
        """goes one line down with a shape"""

        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()

    def pieceDropped(self):
        """after dropping shape, remove full lines and create new shape"""

        for i in range(4):
            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())

        self.removeFullLines()

        if not self.isWaitingAfterLine:
            self.newPiece()

    def removeFullLines(self):
        """removes all full lines from the board"""

        numFullLines = 0
        rowsToRemove = []

        for i in range(Board.BoardHeight):

            n = 0
            for j in range(Board.BoardWidth):
                if not self.shapeAt(j, i) == Tetrominoe.NoShape:
                    n = n + 1

            if n == 10:
                rowsToRemove.append(i)

        rowsToRemove.reverse()

        for m in rowsToRemove:

            for k in range(m, Board.BoardHeight):
                for l in range(Board.BoardWidth):
                    self.setShapeAt(l, k, self.shapeAt(l, k + 1))

        numFullLines = numFullLines + len(rowsToRemove)

        if numFullLines > 0:
            self.numLinesRemoved = self.numLinesRemoved + numFullLines
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

            self.isWaitingAfterLine = True
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.update()

    def newPiece(self):
        """creates a new shape"""
        self.v_box = QVBoxLayout()
        self.menu = QPushButton("Menu")
        self.v_box.addWidget(self.menu)
        
        self.curPiece = Shape()
        self.curPiece.setRandomShape()
        self.curX = Board.BoardWidth // 2 + 1
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()

        if not self.tryMove(self.curPiece, self.curX, self.curY):
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.timer.stop()
            self.isStarted = False
            self.exitgame = self.msg2Statusbar.emit("Game over")
            self.exitgame = ExitGameOwer("Game Ower", self)
            self.exitgame.show()



    def tryMove(self, newPiece, newX, newY):
        """tries to move a shape"""

        for i in range(4):

            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)

            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False

            if self.shapeAt(x, y) != Tetrominoe.NoShape:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()

        return True

    def drawSquare(self, painter, x, y, shape):
        """draws a square of a shape"""

        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
                         self.squareHeight() - 2, color)

        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
                         x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1,
                         y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)




class ExitGameOwer(QWidget):
    def __init__(self, text, win) -> None:
        super().__init__()
        self.win = win
        self.setFixedSize(200,100)
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.info_label = QLabel(text)

        self.v_box.addWidget(self.info_label)

        self.new_game_btn = QPushButton('New game')
        self.exit_btn = QPushButton('Exit')

        self.h_box.addWidget(self.new_game_btn)
        self.h_box.addWidget(self.exit_btn)

        self.new_game_btn.clicked.connect(self.newGame)
        self.exit_btn.clicked.connect(self.exit1)



        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

    def exit1(self):
        self.win.close()
        self.close()

    def actionMenu(self):
        self.win.close()
        gamexo = Menu()
        widget.addWidget(gamexo)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.close()

    def newGame(self):
        self.win.close()
        self.win = Tetris()
        self.win.show()
        self.close()
        










class Tetrominoe(object):
    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7


class Shape(object):
    coordsTable = (
        ((0, 0), (0, 0), (0, 0), (0, 0)),
        ((0, -1), (0, 0), (-1, 0), (-1, 1)),
        ((0, -1), (0, 0), (1, 0), (1, 1)),
        ((0, -1), (0, 0), (0, 1), (0, 2)),
        ((-1, 0), (0, 0), (1, 0), (0, 1)),
        ((0, 0), (1, 0), (0, 1), (1, 1)),
        ((-1, -1), (0, -1), (0, 0), (0, 1)),
        ((1, -1), (0, -1), (0, 0), (0, 1))
    )

    def __init__(self):

        self.coords = [[0, 0] for i in range(4)]
        self.pieceShape = Tetrominoe.NoShape

        self.setShape(Tetrominoe.NoShape)

    def shape(self):
        """returns shape"""

        return self.pieceShape

    def setShape(self, shape):
        """sets a shape"""

        table = Shape.coordsTable[shape]

        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]

        self.pieceShape = shape

    def setRandomShape(self):
        """chooses a random shape"""

        self.setShape(random.randint(1, 7))

    def x(self, index):
        """returns x coordinate"""

        return self.coords[index][0]

    def y(self, index):
        """returns y coordinate"""

        return self.coords[index][1]

    def setX(self, index, x):
        """sets x coordinate"""

        self.coords[index][0] = x

    def setY(self, index, y):
        """sets y coordinate"""

        self.coords[index][1] = y

    def minX(self):
        """returns min x value"""

        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])

        return m

    def maxX(self):
        """returns max x value"""

        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])

        return m

    def minY(self):
        """returns min y value"""

        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])

        return m

    def maxY(self):
        """returns max y value"""

        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])

        return m

    def rotateLeft(self):
        """rotates shape to the left"""

        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape

        for i in range(4):
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))

        return result

    def rotateRight(self):
        """rotates shape to the right"""

        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape

        for i in range(4):
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))

        return result


























class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TICTACTOE')
        self.setFixedSize(300,400)
        
        self.btns = list()
        self.turn = 0
        self.turn_count = 0

        for _ in range(3):
            row = list()
            for _ in range(3):
                row.append(QPushButton(self))
            self.btns.append(row)

        for i in range(3):
            for j in range(3):
                self.btns[i][j].setGeometry(90*i+20, 90*j+20, 80, 80)
                self.btns[i][j].clicked.connect(self.on_click)

        self.info_label = QLabel('Turn X', self)
        self.info_label.setStyleSheet('font-size: 50px')
        self.info_label.setGeometry(85,300,270,90)

    def on_click(self):
        self.turn_count += 1

        btn = self.sender()
        btn.setEnabled(False)

        if self.turn == 0:
            btn.setStyleSheet('color: blue; font-size: 50px;')

            btn.setText("X")
            self.turn = 1
            self.info_label.setText('Turn O')
        else:
            btn.setStyleSheet('color: red ; font-size: 50px')
            btn.setText("O")
            self.turn = 0
            self.info_label.setText('Turn X') 

        winner = self.check_win()

        if winner:
            if self.turn == 0:
                self.info_label.setText('Win O') 
                self.exit = ExitWin('Win O', self)
                self.exit.show()
            else:
                self.info_label.setText('Win X') 
                self.exit = ExitWin('Win X', self)
                self.exit.show()
            self.closeBtn()

        elif self.turn_count == 9:
            self.info_label.setText('Draw') 
            self.exit = ExitWin('Draw', self)
            self.exit.show()
            self.closeBtn()

    
    def closeBtn(self):
        for i in range(3):
            for j in range(3):
                self.btns[i][j].setEnabled(False)


    def check_win(self):
        
        for i in range(3):
            if self.btns[i][0].text() == self.btns[i][1].text() and self.btns[i][0].text() == self.btns[i][2].text() and self.btns[i][0].text() != '':
                return True

        for i in range(3):
            if self.btns[0][i].text() == self.btns[1][i].text() and self.btns[0][i].text() == self.btns[2][i].text() and self.btns[0][i].text() != '':
                return True
        
        if self.btns[0][0].text() == self.btns[1][1].text() and self.btns[0][0].text() == self.btns[2][2].text() and self.btns[0][0].text() != '':
                return True

        if self.btns[0][2].text() == self.btns[1][1].text() and self.btns[0][2].text() == self.btns[2][0].text() and self.btns[0][2].text() != '':
                return True

        return False

class ExitWin(QWidget):
    def __init__(self, text, win) -> None:
        super().__init__()
        self.win = win
        self.setFixedSize(200,100)
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.info_label = QLabel(text)

        self.v_box.addWidget(self.info_label)

        self.new_game_btn = QPushButton('New game')
        self.menu_btn = QPushButton('Menu')

        self.h_box.addWidget(self.new_game_btn)
        self.h_box.addWidget(self.menu_btn)
        
        self.new_game_btn.clicked.connect(self.newGame)
        self.menu_btn.clicked.connect(self.actionMenu)

        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

    def exit1(self):
        self.win.close()
        self.close()

    def actionMenu(self):
        self.exit1()
        gamexo = Menu()
        widget.addWidget(gamexo)
        widget.setCurrentIndex(widget.currentIndex()+1)
      

    def newGame(self):
        self.exit1()
        self.win = Window()
        self.win.show()
        
        















class MyProfile(QDialog):
    def __init__(self) -> None:
        super(MyProfile, self).__init__()
        loadUi("profile.ui", self)
        self.menu.clicked.connect(self.myFunction)


    def myFunction(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)








class CreateAccScrean(QDialog):
    def __init__(self) -> None:
        super(CreateAccScrean, self).__init__()
        loadUi("createacc.ui",self)
        self.passwordcore = PasswordCore()
        self.passwordfeld.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpasswordfeld.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.signupfunctio)



        
    def signupfunctio(self):
        

        user = self.usernamefeld.text()
        password = self.passwordfeld.text()
        confirmpassword = self.confirmpasswordfeld.text()

        if len(user)==0 or len(password)==0 or len(confirmpassword)==0:
            self.error2.setText("Please fill in all inputs.")

        elif password!=confirmpassword:
            self.error2.setText("Passwords do not match.")

        else:
            self.passwordcore.insert(Password(user, password))


            fillprofile = FillProfileScrean()
            widget.addWidget(fillprofile)
            widget.setCurrentIndex(widget.currentIndex()+1)
                

class FillProfileScrean(QDialog):
    def __init__(self) -> None:
        super(FillProfileScrean, self).__init__()
        loadUi("fillprofile.ui",self)
        self.continue_2.clicked.connect(self.menufunction)



    def menufunction(self):
        continue_2 = Menu()
        widget.addWidget(continue_2)
        widget.setCurrentIndex(widget.currentIndex()+1)
        


app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(531)
widget.setFixedWidth(800)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting")