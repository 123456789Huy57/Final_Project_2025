# Form implementation generated from reading ui file 'D:\TMĐT\Programming Technique\ProTech\FinalProject\ui\SendEmail\SendEmail.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 505)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\TMĐT\\Programming Technique\\ProTech\\FinalProject\\ui\\SendEmail\\../../images/img_bg5.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 121, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("D:\\TMĐT\\Programming Technique\\ProTech\\FinalProject\\ui\\SendEmail\\../../images/logo_2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("UTM Eremitage")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 180, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 220, 801, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.lineEditEmail = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_2)
        self.lineEditEmail.setMinimumSize(QtCore.QSize(500, 40))
        self.lineEditEmail.setStyleSheet("background-color: rgba(0, 0, 0, 100);\n"
"border: 1.5px solid white;\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 5px;\n"
"font: 12pt \"Times New Roman\";")
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.horizontalLayout_2.addWidget(self.lineEditEmail)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pushButtonReturn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonReturn.setGeometry(QtCore.QRect(20, 390, 111, 41))
        self.pushButtonReturn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.965174 rgba(0, 0, 139, 255));")
        self.pushButtonReturn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\TMĐT\\Programming Technique\\ProTech\\FinalProject\\ui\\SendEmail\\../../images/icon_return.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonReturn.setIcon(icon)
        self.pushButtonReturn.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonReturn.setObjectName("pushButtonReturn")
        self.pushButtonSendOTP = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSendOTP.setGeometry(QtCore.QRect(330, 300, 111, 41))
        font = QtGui.QFont()
        font.setFamily("UTM Bebas")
        font.setPointSize(14)
        self.pushButtonSendOTP.setFont(font)
        self.pushButtonSendOTP.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.965174 rgba(0, 0, 139, 255));")
        self.pushButtonSendOTP.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonSendOTP.setObjectName("pushButtonSendOTP")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "FORGOT THE PASSWORD ?"))
        self.label_4.setText(_translate("MainWindow", "Enter your email address:"))
        self.pushButtonSendOTP.setText(_translate("MainWindow", "SEND OTP"))
