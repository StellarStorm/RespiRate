# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RespiRate.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1085, 954)
        font = QtGui.QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(100, -1, 100, -1)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 5, 2, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_3.setHorizontalSpacing(4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(1000, 1000))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 274, 232))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_3.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_3.setMaximumSize(QtCore.QSize(800, 16777215))
        self.scrollAreaWidgetContents_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_mouseNum = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_mouseNum.sizePolicy().hasHeightForWidth())
        self.label_mouseNum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_mouseNum.setFont(font)
        self.label_mouseNum.setScaledContents(True)
        self.label_mouseNum.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_mouseNum.setObjectName("label_mouseNum")
        self.gridLayout_4.addWidget(self.label_mouseNum, 0, 0, 1, 1)
        self.label_RespRate = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_RespRate.sizePolicy().hasHeightForWidth())
        self.label_RespRate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_RespRate.setFont(font)
        self.label_RespRate.setAlignment(QtCore.Qt.AlignCenter)
        self.label_RespRate.setObjectName("label_RespRate")
        self.gridLayout_4.addWidget(self.label_RespRate, 0, 1, 1, 1)
        self.label_StDev = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_StDev.sizePolicy().hasHeightForWidth())
        self.label_StDev.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_StDev.setFont(font)
        self.label_StDev.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_StDev.setAlignment(QtCore.Qt.AlignCenter)
        self.label_StDev.setObjectName("label_StDev")
        self.gridLayout_4.addWidget(self.label_StDev, 0, 2, 1, 1)
        self.textBrowser_Output = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_3)
        self.textBrowser_Output.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_Output.sizePolicy().hasHeightForWidth())
        self.textBrowser_Output.setSizePolicy(sizePolicy)
        self.textBrowser_Output.setMaximumSize(QtCore.QSize(800, 16777215))
        self.textBrowser_Output.setObjectName("textBrowser_Output")
        self.gridLayout_4.addWidget(self.textBrowser_Output, 1, 0, 1, 3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 4, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setLineWidth(3)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_Play = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Play.setFont(font)
        self.pushButton_Play.setObjectName("pushButton_Play")
        self.gridLayout_2.addWidget(self.pushButton_Play, 2, 0, 1, 1)
        self.pushButton_Pause = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Pause.setFont(font)
        self.pushButton_Pause.setObjectName("pushButton_Pause")
        self.gridLayout_2.addWidget(self.pushButton_Pause, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 3, 1, 1)
        self.videoFrame = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoFrame.sizePolicy().hasHeightForWidth())
        self.videoFrame.setSizePolicy(sizePolicy)
        self.videoFrame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.videoFrame.setText("")
        self.videoFrame.setObjectName("videoFrame")
        self.gridLayout_2.addWidget(self.videoFrame, 0, 0, 1, 5)
        self.horizontalSlider = QtWidgets.QSlider(self.frame_4)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 1, 0, 1, 4)
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_4)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_2.addWidget(self.lcdNumber, 1, 4, 1, 1)
        self.pushButton_SelectST = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_SelectST.setFont(font)
        self.pushButton_SelectST.setObjectName("pushButton_SelectST")
        self.gridLayout_2.addWidget(self.pushButton_SelectST, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.frame_4, 0, 0, 2, 3)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout.addWidget(self.frame_5, 3, 2, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_lenMeasure = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_lenMeasure.sizePolicy().hasHeightForWidth())
        self.label_lenMeasure.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_lenMeasure.setFont(font)
        self.label_lenMeasure.setObjectName("label_lenMeasure")
        self.gridLayout_5.addWidget(self.label_lenMeasure, 3, 0, 1, 1)
        self.label_mouseID = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_mouseID.sizePolicy().hasHeightForWidth())
        self.label_mouseID.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_mouseID.setFont(font)
        self.label_mouseID.setObjectName("label_mouseID")
        self.gridLayout_5.addWidget(self.label_mouseID, 1, 0, 1, 1)
        self.label_startT = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_startT.sizePolicy().hasHeightForWidth())
        self.label_startT.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_startT.setFont(font)
        self.label_startT.setObjectName("label_startT")
        self.gridLayout_5.addWidget(self.label_startT, 2, 0, 1, 1)
        self.lineEdit_startT = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_startT.sizePolicy().hasHeightForWidth())
        self.lineEdit_startT.setSizePolicy(sizePolicy)
        self.lineEdit_startT.setObjectName("lineEdit_startT")
        self.gridLayout_5.addWidget(self.lineEdit_startT, 2, 1, 1, 1)
        self.lineEdit_lenMeasure = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_lenMeasure.sizePolicy().hasHeightForWidth())
        self.lineEdit_lenMeasure.setSizePolicy(sizePolicy)
        self.lineEdit_lenMeasure.setObjectName("lineEdit_lenMeasure")
        self.gridLayout_5.addWidget(self.lineEdit_lenMeasure, 3, 1, 1, 1)
        self.lineEdit_mouseID = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_mouseID.sizePolicy().hasHeightForWidth())
        self.lineEdit_mouseID.setSizePolicy(sizePolicy)
        self.lineEdit_mouseID.setObjectName("lineEdit_mouseID")
        self.gridLayout_5.addWidget(self.lineEdit_mouseID, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(270, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 6, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem4, 5, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 5, 1, 1, 1)
        self.pushButton_Contour = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Contour.sizePolicy().hasHeightForWidth())
        self.pushButton_Contour.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Contour.setFont(font)
        self.pushButton_Contour.setObjectName("pushButton_Contour")
        self.gridLayout_5.addWidget(self.pushButton_Contour, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 4, 0, 1, 1)
        self.pushButton_Clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Clear.sizePolicy().hasHeightForWidth())
        self.pushButton_Clear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Clear.setFont(font)
        self.pushButton_Clear.setToolTip("")
        self.pushButton_Clear.setToolTipDuration(5)
        self.pushButton_Clear.setWhatsThis("")
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.gridLayout.addWidget(self.pushButton_Clear, 5, 1, 1, 1, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1085, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_video = QtWidgets.QAction(MainWindow)
        self.actionOpen_video.setObjectName("actionOpen_video")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_Qt = QtWidgets.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionOpen_spreadsheet = QtWidgets.QAction(MainWindow)
        self.actionOpen_spreadsheet.setObjectName("actionOpen_spreadsheet")
        self.menuFile.addAction(self.actionOpen_video)
        self.menuFile.addAction(self.actionOpen_spreadsheet)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.label_lenMeasure.setBuddy(self.lineEdit_lenMeasure)
        self.label_mouseID.setBuddy(self.lineEdit_mouseID)
        self.label_startT.setBuddy(self.lineEdit_startT)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_mouseNum.setText(_translate("MainWindow", "Mouse #"))
        self.label_RespRate.setText(_translate("MainWindow", "Respiratory Rate"))
        self.label_StDev.setText(_translate("MainWindow", "St. Dev."))
        self.textBrowser_Output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.pushButton_Play.setText(_translate("MainWindow", "Play"))
        self.pushButton_Pause.setText(_translate("MainWindow", "Pause"))
        self.pushButton_SelectST.setText(_translate("MainWindow", " Select start time "))
        self.label_lenMeasure.setText(_translate("MainWindow", "                  Length of measurement (s):"))
        self.label_mouseID.setText(_translate("MainWindow", "      Mouse IDs (separated by commas):"))
        self.label_startT.setText(_translate("MainWindow", "                        Start time (hh:mm:ss):  "))
        self.pushButton_Contour.setText(_translate("MainWindow", "Contour"))
        self.pushButton_Clear.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_video.setText(_translate("MainWindow", "Open Video"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt"))
        self.actionOpen_spreadsheet.setText(_translate("MainWindow", "Open Spreadsheet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

