# Form implementation generated from reading ui file 'D:\TMĐT\Programming Technique\ProTech\FinalProject\ui\ValueReporting\ValueReporting.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1255, 821)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1271, 781))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\TMĐT\\Programming Technique\\ProTech\\FinalProject\\ui\\ValueReporting\\../../images/img_bg1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1261, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("UTM Eremitage")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonReturn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonReturn.setGeometry(QtCore.QRect(10, 700, 111, 41))
        self.pushButtonReturn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.965174 rgba(0, 0, 139, 255));")
        self.pushButtonReturn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\TMĐT\\Programming Technique\\ProTech\\FinalProject\\ui\\ValueReporting\\../../images/icon_return.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonReturn.setIcon(icon)
        self.pushButtonReturn.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonReturn.setObjectName("pushButtonReturn")
        self.groupBoxRevenue = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxRevenue.setGeometry(QtCore.QRect(10, 80, 651, 601))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxRevenue.setFont(font)
        self.groupBoxRevenue.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBoxRevenue.setObjectName("groupBoxRevenue")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBoxRevenue)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.groupBoxExpenses = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxExpenses.setGeometry(QtCore.QRect(670, 80, 571, 601))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxExpenses.setFont(font)
        self.groupBoxExpenses.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBoxExpenses.setObjectName("groupBoxExpenses")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBoxExpenses)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1255, 26))
        self.menubar.setObjectName("menubar")
        self.menuSystem = QtWidgets.QMenu(parent=self.menubar)
        self.menuSystem.setObjectName("menuSystem")
        self.menuImport = QtWidgets.QMenu(parent=self.menuSystem)
        self.menuImport.setObjectName("menuImport")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExcel_File = QtGui.QAction(parent=MainWindow)
        self.actionExcel_File.setObjectName("actionExcel_File")
        self.actionExcel_File_2 = QtGui.QAction(parent=MainWindow)
        self.actionExcel_File_2.setObjectName("actionExcel_File_2")
        self.actionDocument = QtGui.QAction(parent=MainWindow)
        self.actionDocument.setObjectName("actionDocument")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExcel_File_Revenue = QtGui.QAction(parent=MainWindow)
        self.actionExcel_File_Revenue.setObjectName("actionExcel_File_Revenue")
        self.actionExit_2 = QtGui.QAction(parent=MainWindow)
        self.actionExit_2.setShortcut("")
        self.actionExit_2.setObjectName("actionExit_2")
        self.menuImport.addAction(self.actionExcel_File)
        self.menuImport.addAction(self.actionExcel_File_Revenue)
        self.menuSystem.addAction(self.menuImport.menuAction())
        self.menuSystem.addAction(self.actionExit_2)
        self.menubar.addAction(self.menuSystem.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">HUMAN RESOURCES MANAGEMENT</span></p></body></html>"))
        self.groupBoxRevenue.setTitle(_translate("MainWindow", "REVENUE:"))
        self.groupBoxExpenses.setTitle(_translate("MainWindow", "EXPENSES:"))
        self.menuSystem.setTitle(_translate("MainWindow", "System"))
        self.menuImport.setTitle(_translate("MainWindow", "Import"))
        self.actionExcel_File.setText(_translate("MainWindow", "Excel File Expenses"))
        self.actionExcel_File_2.setText(_translate("MainWindow", "Excel File"))
        self.actionDocument.setText(_translate("MainWindow", "Document"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExcel_File_Revenue.setText(_translate("MainWindow", "Excel File Revenue"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
