# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1200, 900)
        mainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 2)
        self.view = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view.sizePolicy().hasHeightForWidth())
        self.view.setSizePolicy(sizePolicy)
        self.view.setMinimumSize(QtCore.QSize(700, 700))
        self.view.setBaseSize(QtCore.QSize(0, 0))
        self.view.setObjectName("view")
        self.gridLayout.addWidget(self.view, 0, 0, 3, 1)
        self.fenGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fenGroupBox.sizePolicy().hasHeightForWidth())
        self.fenGroupBox.setSizePolicy(sizePolicy)
        self.fenGroupBox.setMinimumSize(QtCore.QSize(350, 0))
        self.fenGroupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.fenGroupBox.setObjectName("fenGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.fenGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.fenField = QtWidgets.QPlainTextEdit(self.fenGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fenField.sizePolicy().hasHeightForWidth())
        self.fenField.setSizePolicy(sizePolicy)
        self.fenField.setMinimumSize(QtCore.QSize(300, 0))
        self.fenField.setMaximumSize(QtCore.QSize(16777215, 30))
        self.fenField.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.fenField.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fenField.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fenField.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.fenField.setObjectName("fenField")
        self.gridLayout_4.addWidget(self.fenField, 0, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 2, 1, 1)
        self.setFenButton = QtWidgets.QPushButton(self.fenGroupBox)
        self.setFenButton.setStyleSheet("background-color: rgb(180, 180, 180);\n"
"color: rgb(0, 0, 0);")
        self.setFenButton.setObjectName("setFenButton")
        self.gridLayout_4.addWidget(self.setFenButton, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.fenGroupBox, 2, 1, 1, 1)
        self.boardGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boardGroupBox.sizePolicy().hasHeightForWidth())
        self.boardGroupBox.setSizePolicy(sizePolicy)
        self.boardGroupBox.setMinimumSize(QtCore.QSize(350, 0))
        self.boardGroupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.boardGroupBox.setObjectName("boardGroupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.boardGroupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.playerViewSelect = QtWidgets.QComboBox(self.boardGroupBox)
        self.playerViewSelect.setEnabled(False)
        self.playerViewSelect.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.playerViewSelect.setObjectName("playerViewSelect")
        self.playerViewSelect.addItem("")
        self.playerViewSelect.addItem("")
        self.playerViewSelect.addItem("")
        self.playerViewSelect.addItem("")
        self.gridLayout_6.addWidget(self.playerViewSelect, 0, 3, 1, 1)
        self.boardResetButton = QtWidgets.QPushButton(self.boardGroupBox)
        self.boardResetButton.setStyleSheet("background-color: rgb(180, 180, 180);\n"
"color: rgb(0, 0, 0);")
        self.boardResetButton.setObjectName("boardResetButton")
        self.gridLayout_6.addWidget(self.boardResetButton, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.boardGroupBox)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 0, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.boardGroupBox, 0, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(350, 600))
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.moveListTab = QtWidgets.QWidget()
        self.moveListTab.setObjectName("moveListTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.moveListTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.nextMoveButton = QtWidgets.QPushButton(self.moveListTab)
        self.nextMoveButton.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.nextMoveButton.setObjectName("nextMoveButton")
        self.gridLayout_2.addWidget(self.nextMoveButton, 1, 2, 1, 1)
        self.moveListWidget = QtWidgets.QListWidget(self.moveListTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moveListWidget.sizePolicy().hasHeightForWidth())
        self.moveListWidget.setSizePolicy(sizePolicy)
        self.moveListWidget.setMinimumSize(QtCore.QSize(300, 500))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.moveListWidget.setFont(font)
        self.moveListWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.moveListWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.moveListWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.moveListWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.moveListWidget.setProperty("showDropIndicator", False)
        self.moveListWidget.setObjectName("moveListWidget")
        self.gridLayout_2.addWidget(self.moveListWidget, 0, 0, 1, 4)
        self.prevMoveButton = QtWidgets.QPushButton(self.moveListTab)
        self.prevMoveButton.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.prevMoveButton.setObjectName("prevMoveButton")
        self.gridLayout_2.addWidget(self.prevMoveButton, 1, 1, 1, 1)
        self.firstMoveButton = QtWidgets.QPushButton(self.moveListTab)
        self.firstMoveButton.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.firstMoveButton.setObjectName("firstMoveButton")
        self.gridLayout_2.addWidget(self.firstMoveButton, 1, 0, 1, 1)
        self.lastMoveButton = QtWidgets.QPushButton(self.moveListTab)
        self.lastMoveButton.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.lastMoveButton.setObjectName("lastMoveButton")
        self.gridLayout_2.addWidget(self.lastMoveButton, 1, 3, 1, 1)
        self.tabWidget.addTab(self.moveListTab, "")
        self.pgnTab = QtWidgets.QWidget()
        self.pgnTab.setObjectName("pgnTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.pgnTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 3, 1, 1)
        self.pgnField = QtWidgets.QPlainTextEdit(self.pgnTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pgnField.sizePolicy().hasHeightForWidth())
        self.pgnField.setSizePolicy(sizePolicy)
        self.pgnField.setMinimumSize(QtCore.QSize(300, 500))
        self.pgnField.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pgnField.setObjectName("pgnField")
        self.gridLayout_3.addWidget(self.pgnField, 0, 0, 1, 4)
        self.savePgnButton = QtWidgets.QPushButton(self.pgnTab)
        self.savePgnButton.setEnabled(True)
        self.savePgnButton.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.savePgnButton.setObjectName("savePgnButton")
        self.gridLayout_3.addWidget(self.savePgnButton, 1, 2, 1, 1)
        self.loadPgnButton = QtWidgets.QPushButton(self.pgnTab)
        self.loadPgnButton.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.loadPgnButton.setObjectName("loadPgnButton")
        self.gridLayout_3.addWidget(self.loadPgnButton, 1, 1, 1, 1)
        self.tabWidget.addTab(self.pgnTab, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 2, 3, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menu4PlayerChess = QtWidgets.QMenu(self.menubar)
        self.menu4PlayerChess.setObjectName("menu4PlayerChess")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: grey;")
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Game = QtWidgets.QAction(mainWindow)
        self.actionLoad_Game.setObjectName("actionLoad_Game")
        self.actionSave_Game_As = QtWidgets.QAction(mainWindow)
        self.actionSave_Game_As.setObjectName("actionSave_Game_As")
        self.actionQuit = QtWidgets.QAction(mainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionCopy_FEN4 = QtWidgets.QAction(mainWindow)
        self.actionCopy_FEN4.setObjectName("actionCopy_FEN4")
        self.actionPaste_FEN4 = QtWidgets.QAction(mainWindow)
        self.actionPaste_FEN4.setObjectName("actionPaste_FEN4")
        self.actionRotate_Board_Left = QtWidgets.QAction(mainWindow)
        self.actionRotate_Board_Left.setEnabled(False)
        self.actionRotate_Board_Left.setObjectName("actionRotate_Board_Left")
        self.actionRotate_Board_Right = QtWidgets.QAction(mainWindow)
        self.actionRotate_Board_Right.setEnabled(False)
        self.actionRotate_Board_Right.setObjectName("actionRotate_Board_Right")
        self.actionFlip_Board = QtWidgets.QAction(mainWindow)
        self.actionFlip_Board.setEnabled(False)
        self.actionFlip_Board.setObjectName("actionFlip_Board")
        self.actionNew_Game = QtWidgets.QAction(mainWindow)
        self.actionNew_Game.setObjectName("actionNew_Game")
        self.actionAbout = QtWidgets.QAction(mainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionPreferences = QtWidgets.QAction(mainWindow)
        self.actionPreferences.setEnabled(False)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionCheck_for_Updates = QtWidgets.QAction(mainWindow)
        self.actionCheck_for_Updates.setEnabled(False)
        self.actionCheck_for_Updates.setObjectName("actionCheck_for_Updates")
        self.menuFile.addAction(self.actionNew_Game)
        self.menuFile.addAction(self.actionLoad_Game)
        self.menuFile.addAction(self.actionSave_Game_As)
        self.menuEdit.addAction(self.actionCopy_FEN4)
        self.menuEdit.addAction(self.actionPaste_FEN4)
        self.menuView.addAction(self.actionRotate_Board_Left)
        self.menuView.addAction(self.actionRotate_Board_Right)
        self.menuView.addAction(self.actionFlip_Board)
        self.menu4PlayerChess.addAction(self.actionAbout)
        self.menu4PlayerChess.addAction(self.actionCheck_for_Updates)
        self.menu4PlayerChess.addAction(self.actionPreferences)
        self.menu4PlayerChess.addSeparator()
        self.menu4PlayerChess.addAction(self.actionQuit)
        self.menubar.addAction(self.menu4PlayerChess.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Four-Player Chess Analysis Board"))
        self.fenGroupBox.setTitle(_translate("mainWindow", "FEN4"))
        self.fenField.setStatusTip(_translate("mainWindow", "Enter FEN4"))
        self.fenField.setPlaceholderText(_translate("mainWindow", "Enter FEN4 here..."))
        self.setFenButton.setStatusTip(_translate("mainWindow", "Set position to current FEN4"))
        self.setFenButton.setText(_translate("mainWindow", "Set Position"))
        self.boardGroupBox.setTitle(_translate("mainWindow", "Board"))
        self.playerViewSelect.setItemText(0, _translate("mainWindow", "Red"))
        self.playerViewSelect.setItemText(1, _translate("mainWindow", "Blue"))
        self.playerViewSelect.setItemText(2, _translate("mainWindow", "Yellow"))
        self.playerViewSelect.setItemText(3, _translate("mainWindow", "Green"))
        self.boardResetButton.setStatusTip(_translate("mainWindow", "Reset board"))
        self.boardResetButton.setText(_translate("mainWindow", "Reset"))
        self.label.setText(_translate("mainWindow", "View:"))
        self.nextMoveButton.setStatusTip(_translate("mainWindow", "Go to next move"))
        self.nextMoveButton.setText(_translate("mainWindow", ">"))
        self.prevMoveButton.setStatusTip(_translate("mainWindow", "Go to previous move"))
        self.prevMoveButton.setText(_translate("mainWindow", "<"))
        self.firstMoveButton.setStatusTip(_translate("mainWindow", "Go to first move"))
        self.firstMoveButton.setText(_translate("mainWindow", "<<"))
        self.lastMoveButton.setStatusTip(_translate("mainWindow", "Go to last move"))
        self.lastMoveButton.setText(_translate("mainWindow", ">>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.moveListTab), _translate("mainWindow", "Move List"))
        self.savePgnButton.setStatusTip(_translate("mainWindow", "Save game to PGN4 file"))
        self.savePgnButton.setText(_translate("mainWindow", "Save"))
        self.loadPgnButton.setStatusTip(_translate("mainWindow", "Load game from PGN4 file"))
        self.loadPgnButton.setText(_translate("mainWindow", "Load"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pgnTab), _translate("mainWindow", "PGN4"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.menuEdit.setTitle(_translate("mainWindow", "Edit"))
        self.menuView.setTitle(_translate("mainWindow", "View"))
        self.menu4PlayerChess.setTitle(_translate("mainWindow", "4PlayerChess"))
        self.actionLoad_Game.setText(_translate("mainWindow", "Load Game..."))
        self.actionLoad_Game.setToolTip(_translate("mainWindow", "Load Game..."))
        self.actionLoad_Game.setStatusTip(_translate("mainWindow", "Load game from PGN4 file"))
        self.actionLoad_Game.setShortcut(_translate("mainWindow", "Ctrl+O"))
        self.actionSave_Game_As.setText(_translate("mainWindow", "Save Game As..."))
        self.actionSave_Game_As.setToolTip(_translate("mainWindow", "Save Game As..."))
        self.actionSave_Game_As.setStatusTip(_translate("mainWindow", "Save game to PGN4 file"))
        self.actionSave_Game_As.setShortcut(_translate("mainWindow", "Ctrl+Shift+S"))
        self.actionQuit.setText(_translate("mainWindow", "Quit 4PlayerChess"))
        self.actionQuit.setStatusTip(_translate("mainWindow", "Quit application"))
        self.actionQuit.setShortcut(_translate("mainWindow", "Ctrl+Q"))
        self.actionCopy_FEN4.setText(_translate("mainWindow", "Copy FEN4"))
        self.actionCopy_FEN4.setStatusTip(_translate("mainWindow", "Copy FEN4 to clipboard"))
        self.actionCopy_FEN4.setShortcut(_translate("mainWindow", "Ctrl+C"))
        self.actionPaste_FEN4.setText(_translate("mainWindow", "Paste FEN4"))
        self.actionPaste_FEN4.setStatusTip(_translate("mainWindow", "Paste FEN4 from clipboard"))
        self.actionPaste_FEN4.setShortcut(_translate("mainWindow", "Ctrl+V"))
        self.actionRotate_Board_Left.setText(_translate("mainWindow", "Rotate Board Left"))
        self.actionRotate_Board_Left.setShortcut(_translate("mainWindow", "Ctrl+L"))
        self.actionRotate_Board_Right.setText(_translate("mainWindow", "Rotate Board Right"))
        self.actionRotate_Board_Right.setShortcut(_translate("mainWindow", "Ctrl+R"))
        self.actionFlip_Board.setText(_translate("mainWindow", "Flip Board"))
        self.actionFlip_Board.setShortcut(_translate("mainWindow", "Ctrl+F"))
        self.actionNew_Game.setText(_translate("mainWindow", "New Game"))
        self.actionNew_Game.setStatusTip(_translate("mainWindow", "Start new game"))
        self.actionNew_Game.setShortcut(_translate("mainWindow", "Ctrl+N"))
        self.actionAbout.setText(_translate("mainWindow", "About 4PlayerChess"))
        self.actionAbout.setStatusTip(_translate("mainWindow", "Application info"))
        self.actionPreferences.setText(_translate("mainWindow", "Preferences..."))
        self.actionPreferences.setStatusTip(_translate("mainWindow", "Application preferences"))
        self.actionCheck_for_Updates.setText(_translate("mainWindow", "Check for Updates"))
        self.actionCheck_for_Updates.setStatusTip(_translate("mainWindow", "Check if updates are available"))

