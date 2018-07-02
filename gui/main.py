#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file is part of the Four-Player Chess project, a four-player chess GUI.
#
# Copyright (C) 2018, GammaDeltaII
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt5.QtWidgets import QMainWindow, QSizePolicy, QLayout, QListWidget, QListWidgetItem, QListView, QFrame, \
    QFileDialog, QWidget, QLabel
from PyQt5.QtCore import Qt, QSize, QPoint, QRect
from PyQt5.QtGui import QIcon, QColor, QFont, QFontMetrics, QPainter
from ui.mainwindow import Ui_mainWindow
from gui.algorithm import Teams
from gui.view import View

# Semantic versioning: N.N.N-{alpha|beta|rc}.N
MAJOR = str(0)
MINOR = str(1)
PATCH = str(0)
PRE_RELEASE = False * ('-' + 'alpha' + str(1))  # alpha, beta or rc (= release candidate)
VERSION = MAJOR + '.' + MINOR + '.' + PATCH + PRE_RELEASE


class MainWindow(QMainWindow, Ui_mainWindow):
    """The application main window. The imported UI code is generated by PyQt5 from reading the Qt Creator .ui file."""
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Show license notice
        self.statusbar.showMessage('Copyright (C) 2018, GammaDeltaII (GNU GPL-3.0)', 5000)

        # Create view and algorithm instances
        self.view = View()
        self.gridLayout.addWidget(self.view, 0, 0, 3, 1)
        self.algorithm = Teams()

        # Set piece icons
        pieces = ['rP', 'rN', 'rR', 'rB', 'rQ', 'rK',
                  'bP', 'bN', 'bR', 'bB', 'bQ', 'bK',
                  'yP', 'yN', 'yR', 'yB', 'yQ', 'yK',
                  'gP', 'gN', 'gR', 'gB', 'gQ', 'gK']
        for piece in pieces:
            self.view.setPiece(piece, QIcon('resources/img/pieces/' + piece + '.svg'))

        # Set view size based on board square size
        self.view.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.view.setSquareSize(QSize(50, 50))
        self.layout().setSizeConstraint(QLayout.SetFixedSize)

        # Connect signals
        self.view.clicked.connect(self.viewClicked)
        self.algorithm.boardChanged.connect(self.view.setBoard)  # If algorithm changes board, view must update board
        self.algorithm.currentPlayerChanged.connect(self.view.highlightPlayer)
        self.algorithm.moveTextChanged.connect(self.updateMoveList)
        self.algorithm.selectMove.connect(self.selectMove)
        self.algorithm.removeMoveSelection.connect(self.removeMoveSelection)
        self.algorithm.fen4Generated.connect(self.fenField.setPlainText)
        self.algorithm.pgn4Generated.connect(self.pgnField.setPlainText)
        self.algorithm.removeHighlight.connect(self.view.removeHighlightsOfColor)
        self.view.playerNameEdited.connect(self.algorithm.updatePlayerNames)
        self.algorithm.playerNamesChanged.connect(self.view.setPlayerNames)
        self.algorithm.addHighlight.connect(self.addHighlight)

        # Connect menu actions
        self.actionAbout.triggered.connect(self.showAboutWindow)
        self.actionQuit.triggered.connect(self.close)
        self.actionNew_Game.triggered.connect(self.algorithm.newGame)
        self.actionNew_Game.triggered.connect(self.view.repaint)  # Forced repaint
        self.actionNew_Game.triggered.connect(self.moveListWidget.clear)
        self.actionLoad_Game.triggered.connect(self.openFileNameDialog)
        self.actionSave_Game_As.triggered.connect(self.saveFileDialog)
        self.actionCopy_FEN4.triggered.connect(self.fenField.selectAll)
        self.actionCopy_FEN4.triggered.connect(self.fenField.copy)
        self.actionCopy_FEN4.triggered.connect(self.repaint)
        self.actionPaste_FEN4.triggered.connect(self.fenField.clear)
        self.actionPaste_FEN4.triggered.connect(self.fenField.paste)
        self.actionPaste_FEN4.triggered.connect(self.repaint)

        # Connect button actions
        self.boardResetButton.clicked.connect(self.algorithm.newGame)
        self.boardResetButton.clicked.connect(self.view.repaint)  # Forced repaint
        self.boardResetButton.clicked.connect(self.moveListWidget.clear)
        self.setFenButton.clicked.connect(self.setFen4)
        self.loadPgnButton.clicked.connect(self.openFileNameDialog)
        self.savePgnButton.clicked.connect(self.saveFileDialog)
        self.prevMoveButton.clicked.connect(self.algorithm.prevMove)
        self.prevMoveButton.clicked.connect(self.view.repaint)
        self.nextMoveButton.clicked.connect(self.algorithm.nextMove)
        self.nextMoveButton.clicked.connect(self.view.repaint)
        self.firstMoveButton.clicked.connect(self.algorithm.firstMove)
        self.firstMoveButton.clicked.connect(self.view.repaint)
        self.lastMoveButton.clicked.connect(self.algorithm.lastMove)
        self.lastMoveButton.clicked.connect(self.view.repaint)

        # Start new game
        self.algorithm.newGame()

        # Initialize variables
        self.clickPoint = QPoint()
        self.selectedSquare = 0
        self.moveHighlight = 0

        # Create application info popup
        self.popup = None

    class Popup(QWidget):
        """Pop-up window with application info."""
        def __init__(self):
            super().__init__()
            self.setFixedSize(300, 220)
            self.setStyleSheet("""
            color: white;
            background-color: rgb(50, 50, 50);
            """)

            self.text = QLabel(self)
            self.text.setFixedSize(250, 120)
            self.text.setWordWrap(True)
            self.text.setOpenExternalLinks(True)
            self.text.setText("""
            <center>
            <p><b>4PlayerChess</b></p>
            <small>
            <p>Version """ + VERSION + """</p>
            <p>Copyright &copy; 2018, GammaDeltaII</p>
            <p>This software is licensed under the GNU General Public License v3.0<br>
            <a href = "https://www.gnu.org/licenses/gpl-3.0" style = "color:grey;">
            https://www.gnu.org/licenses/gpl-3.0</a></p>
            </small>
            </center>
            """)
            x = (self.width() - self.text.width()) / 2
            y = 20 + 50 + 10
            self.text.move(x, y)
            self.text.show()

        def paintEvent(self, event):
            """Implements paintEvent() method."""
            painter = QPainter()
            painter.begin(self)
            icon = QIcon('resources/img/icon.svg')
            width = 50
            height = 50
            x = (self.width() - width) / 2
            y = 20
            rect = QRect(x, y, width, height)
            icon.paint(painter, rect, Qt.AlignCenter)
            painter.end()

    def showAboutWindow(self):
        """Show pop-up window with application info."""
        self.popup = self.Popup()
        x = self.x() + (self.width() - self.popup.width()) / 2
        y = self.y() + (self.height() - self.popup.height()) / 2
        self.popup.move(x, y)
        self.popup.show()
        self.repaint()

    def addHighlight(self, fromFile, fromRank, toFile, toRank, color):
        """Adds move highlight to board view."""
        fromSquare = self.view.SquareHighlight(fromFile, fromRank, color)
        self.view.addHighlight(fromSquare)
        toSquare = self.view.SquareHighlight(toFile, toRank, color)
        self.view.addHighlight(toSquare)

    def viewClicked(self, square):
        """Handles view click event to move clicked piece to clicked square."""
        if self.algorithm.currentPlayer == self.algorithm.Red:
            color = QColor('#33bf3b43')
        elif self.algorithm.currentPlayer == self.algorithm.Blue:
            color = QColor('#334185bf')
        elif self.algorithm.currentPlayer == self.algorithm.Yellow:
            color = QColor('#33c09526')
        elif self.algorithm.currentPlayer == self.algorithm.Green:
            color = QColor('#334e9161')
        else:
            color = QColor('#00000000')
        if self.clickPoint.isNull():
            squareData = self.view.board.getData(square.x(), square.y())
            if squareData != ' ' and squareData[0] == self.algorithm.currentPlayer:
                self.clickPoint = square
                self.selectedSquare = self.view.SquareHighlight(square.x(), square.y(), color)
                self.view.addHighlight(self.selectedSquare)
        else:
            moved = False
            if square != self.clickPoint:
                moved = self.algorithm.makeMove(self.clickPoint.x(), self.clickPoint.y(), square.x(), square.y())
            self.clickPoint = QPoint()
            if not moved:
                self.view.removeHighlight(self.selectedSquare)
            else:
                self.moveHighlight = self.view.SquareHighlight(square.x(), square.y(), color)
                self.view.addHighlight(self.moveHighlight)
                # Remove highlights of next player
                if self.algorithm.currentPlayer == self.algorithm.Red:
                    color = QColor('#33bf3b43')
                elif self.algorithm.currentPlayer == self.algorithm.Blue:
                    color = QColor('#334185bf')
                elif self.algorithm.currentPlayer == self.algorithm.Yellow:
                    color = QColor('#33c09526')
                elif self.algorithm.currentPlayer == self.algorithm.Green:
                    color = QColor('#334e9161')
                else:
                    color = QColor('#00000000')
                self.view.removeHighlightsOfColor(color)
                self.moveHighlight = 0
            self.selectedSquare = 0

    def keyPressEvent(self, event):
        """Handles arrow key press events to go to previous, next, first or last move."""
        if event.key() == Qt.Key_Left:
            self.algorithm.prevMove()
        if event.key() == Qt.Key_Right:
            self.algorithm.nextMove()
        if event.key() == Qt.Key_Up:
            self.algorithm.firstMove()
        if event.key() == Qt.Key_Down:
            self.algorithm.lastMove()

    def openFileNameDialog(self):
        """Shows file dialog to load a game from a PGN4 file."""
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        # noinspection PyCallByClass,PyTypeChecker
        fileName, _ = QFileDialog.getOpenFileName(self, "Load Game", "data/games/",
                                                  "PGN4 Files (*.pgn4)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                pgn4 = ''.join(file.readlines())
                self.pgnField.setPlainText(pgn4)
                self.algorithm.parsePgn4(pgn4)
                self.statusbar.showMessage('Game loaded.', 3000)

    def saveFileDialog(self):
        """Shows file dialog to save a game to a PGN4 file."""
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        # noinspection PyTypeChecker,PyCallByClass
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Game", "data/games/",
                                                  "PGN4 Files (*.pgn4)", options=options)
        if fileName:
            ext = '.pgn4'
            if ext not in fileName:
                fileName += ext
            with open(fileName, 'w') as file:
                pgn4 = self.pgnField.toPlainText()
                file.writelines(pgn4)
                self.statusbar.showMessage('Game saved.', 3000)

    def setFen4(self):
        """Gets FEN4 from the text field to set the board accordingly."""
        fen4 = self.fenField.toPlainText()
        self.algorithm.setBoardState(fen4)
        self.view.repaint()  # Forced repaint

    def updateMoveList(self, moveText):
        """Updates move list based on movetext."""
        class Row(QListWidget):
            """Custom QListWidget class for rows in move list."""
            def __init__(self):
                super().__init__()
                self.setFlow(QListView.LeftToRight)
                self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.setWrapping(True)
                self.setFrameShape(QFrame.NoFrame)
                self.setFocusPolicy(Qt.NoFocus)
                self.setStyleSheet("""
                QListWidget {color: rgb(0, 0, 0); font-family: Trebuchet MS; font-weight: bold; font-size: 12;
                padding: 2px; margin: 0px;}
                QListWidget::item:selected {background-color: rgba(255, 255, 0, 0.3);}
                """)

            def sizeHint(self):
                """Implements sizeHint() method."""
                rowWidth = sum(self.item(index).sizeHint().width() for index in range(self.count()))
                fm = QFontMetrics(QFont('Trebuchet MS', 12, QFont.Bold))
                padding = 2  # Row padding
                width = 290
                height = fm.height() * (rowWidth // width + 1) + 2 * padding
                return QSize(width, height)

        class RowItem(QListWidgetItem):
            """Custom QListWidgetItem class for row items in move list rows."""
            def __init__(self, text):
                super().__init__(text)
                self.setTextAlignment(Qt.AlignCenter)

            def sizeHint(self):
                """Implements sizeHint() method."""
                fm = QFontMetrics(QFont('Trebuchet MS', 12, QFont.Bold))
                spacing = 10  # TODO get rid of the item spacing somehow
                width = fm.width(self.text()) + 2 * spacing
                height = fm.height()
                return QSize(width, height)

        self.moveListWidget.clear()
        tokens = moveText.split()
        row = Row()
        row.itemClicked.connect(lambda item, this=row: self.moveListItemClicked(item, this))
        level = 0
        for token in tokens:
            rowItem = RowItem(token)
            rowItem.setSizeHint(rowItem.sizeHint())  # Update size hack
            if token == '(':
                # Start of new variation
                level += 1
                if not row.count() == 0:
                    listItem = QListWidgetItem(self.moveListWidget)
                    listItem.setSizeHint(row.sizeHint())
                    self.moveListWidget.addItem(listItem)
                    self.moveListWidget.setItemWidget(listItem, row)
                row = Row()
                row.itemClicked.connect(lambda item, this=row: self.moveListItemClicked(item, this))
                if level == 1:
                    row.setStyleSheet("""
                    QListWidget {color: rgb(100, 100, 100); font-family: Trebuchet MS; font-weight: bold; font-size: 12; 
                    background-color: rgb(240, 240, 240); padding: 2px; margin: 0px;}
                    QListWidget::item:selected {color: rgb(100, 100, 100); background-color: rgba(255, 255, 0, 0.3);}
                    """)
                elif level > 1:
                    row.setStyleSheet("""
                    QListWidget {color: rgb(150, 150, 150); font-family: Trebuchet MS; font-weight: bold; font-size: 12; 
                    background-color: rgb(240, 240, 240); padding: 2px; margin: 0px;}
                    QListWidget::item:selected {color: rgb(150, 150, 150); background-color: rgba(255, 255, 0, 0.3);}
                    """)
                else:
                    # Do nothing. Main line uses default stylesheet
                    pass
                row.addItem(rowItem)
            elif token == ')':
                # End of variation
                level -= 1
                row.addItem(rowItem)
                listItem = QListWidgetItem(self.moveListWidget)
                listItem.setSizeHint(row.sizeHint())
                self.moveListWidget.addItem(listItem)
                self.moveListWidget.setItemWidget(listItem, row)
                row = Row()
                row.itemClicked.connect(lambda item, this=row: self.moveListItemClicked(item, this))
                if level == 1:
                    row.setStyleSheet("""
                    QListWidget {color: rgb(100, 100, 100); font-family: Trebuchet MS; font-weight: bold; font-size: 12; 
                    background-color: rgb(240, 240, 240); padding: 2px; margin: 0px;}
                    QListWidget::item:selected {color: rgb(100, 100, 100); background-color: rgba(255, 255, 0, 0.3);}
                    """)
                elif level > 1:
                    row.setStyleSheet("""
                    QListWidget {color: rgb(150, 150, 150); font-family: Trebuchet MS; font-weight: bold; font-size: 12; 
                    background-color: rgb(240, 240, 240); padding: 2px; margin: 0px;}
                    QListWidget::item:selected {color: rgb(150, 150, 150); background-color: rgba(255, 255, 0, 0.3);}
                    """)
                else:
                    # Do nothing. Main line uses default stylesheet
                    pass
            else:
                row.addItem(rowItem)
        listItem = QListWidgetItem(self.moveListWidget)
        listItem.setSizeHint(row.sizeHint())
        self.moveListWidget.addItem(listItem)
        self.moveListWidget.setItemWidget(listItem, row)

    def moveListItemClicked(self, clickedItem, clickedRow):
        """Handles move list click event to set game state to clicked move."""
        # If clicked item is not a move, remove selection
        char = clickedItem.text()[0]
        if char.isdigit() or char == '(' or char == ')' or char == '.':
            clickedItem.setSelected(False)
        else:
            # Remove previous selection from other row, if any
            moveIndex = None
            count = 0
            for index in range(self.moveListWidget.count()):
                row = self.moveListWidget.itemWidget(self.moveListWidget.item(index))
                if row != clickedRow:
                    count += row.count()
                    if row.selectedItems():
                        for item in row.selectedItems():
                            item.setSelected(False)
                elif row == clickedRow:
                    count += row.row(clickedItem)
                    moveIndex = count

            # Get node from dictionary and do actions to get to node from root
            key = (moveIndex, clickedItem.text())
            clickedNode = self.algorithm.moveDict[key]
            if clickedNode:
                actions = clickedNode.pathFromRoot()
                self.algorithm.firstMove()
                for action in actions:
                    exec('self.algorithm.' + action)

    def selectMove(self, key):
        """Makes current move selected in the move list."""
        moveIndex = key[0]
        index = 0
        notFound = True
        while notFound:
            row = self.moveListWidget.itemWidget(self.moveListWidget.item(index))
            rowLength = row.count()
            if moveIndex > rowLength - 1:
                moveIndex -= rowLength
                index += 1
            else:
                row.item(moveIndex).setSelected(True)
                notFound = False
        # Remove selection from other rows
        for rowIndex in range(self.moveListWidget.count()):
            row = self.moveListWidget.itemWidget(self.moveListWidget.item(rowIndex))
            if rowIndex != index and row.selectedItems:
                for item in row.selectedItems():
                    item.setSelected(False)

    def removeMoveSelection(self):
        """Removes move selection in move list."""
        for index in range(self.moveListWidget.count()):
            row = self.moveListWidget.itemWidget(self.moveListWidget.item(index))
            if row.selectedItems():
                for item in row.selectedItems():
                    item.setSelected(False)
