# Form implementation generated from reading ui file 'D:\TMĐT\Programming Technique\ProTech\FinalProject\ui\PersonalTrainerWindow\PersonalTrainerWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1092, 852)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1101, 841))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("D:\\TMĐT\\Programming Technique\\ProTech\\FinalProject\\ui\\PersonalTrainerWindow\\../../images/img_bg5.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 70, 561, 301))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidgetClient = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.tableWidgetClient.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Times New Roman\";")
        self.tableWidgetClient.setObjectName("tableWidgetClient")
        self.tableWidgetClient.setColumnCount(8)
        self.tableWidgetClient.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetClient.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetClient.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetClient.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetClient.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetClient.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetClient.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetClient.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetClient.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetClient.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetClient.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetClient.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetClient.setHorizontalHeaderItem(7, item)
        self.verticalLayout_3.addWidget(self.tableWidgetClient)
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 380, 561, 101))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"")
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButtonClear = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.pushButtonClear.setGeometry(QtCore.QRect(170, 40, 101, 41))
        font = QtGui.QFont()
        font.setFamily("UTM Bebas")
        font.setPointSize(11)
        self.pushButtonClear.setFont(font)
        self.pushButtonClear.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.965174 rgba(0, 0, 139, 255));")
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.pushButtonDelete = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.pushButtonDelete.setGeometry(QtCore.QRect(280, 40, 101, 41))
        font = QtGui.QFont()
        font.setFamily("UTM Bebas")
        font.setPointSize(11)
        self.pushButtonDelete.setFont(font)
        self.pushButtonDelete.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.965174 rgba(0, 0, 139, 255));")
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.pushButtonReturn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonReturn.setGeometry(QtCore.QRect(40, 740, 111, 41))
        self.pushButtonReturn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.965174 rgba(0, 0, 139, 255));")
        self.pushButtonReturn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\TMĐT\\Programming Technique\\ProTech\\FinalProject\\ui\\PersonalTrainerWindow\\../../images/icon_return.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonReturn.setIcon(icon)
        self.pushButtonReturn.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonReturn.setObjectName("pushButtonReturn")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 480, 1051, 231))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.label_14 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(20, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.radioButtonMale = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioButtonMale.setGeometry(QtCore.QRect(120, 180, 95, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonMale.setFont(font)
        self.radioButtonMale.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButtonMale.setObjectName("radioButtonMale")
        self.lineEditFullName = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditFullName.setGeometry(QtCore.QRect(120, 90, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineEditFullName.setFont(font)
        self.lineEditFullName.setStyleSheet("background-color: rgba(0, 0, 0, 100);\n"
"border: 1.5px solid white;\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 5px;\n"
"")
        self.lineEditFullName.setObjectName("lineEditFullName")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(400, 40, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(400, 140, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.lineEditType = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditType.setGeometry(QtCore.QRect(120, 140, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineEditType.setFont(font)
        self.lineEditType.setStyleSheet("background-color: rgba(0, 0, 0, 100);\n"
"border: 1.5px solid white;\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 5px;\n"
"")
        self.lineEditType.setObjectName("lineEditType")
        self.radioButtonFemale = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioButtonFemale.setGeometry(QtCore.QRect(230, 180, 95, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonFemale.setFont(font)
        self.radioButtonFemale.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButtonFemale.setObjectName("radioButtonFemale")
        self.lineEditID = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditID.setGeometry(QtCore.QRect(120, 40, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineEditID.setFont(font)
        self.lineEditID.setStyleSheet("background-color: rgba(0, 0, 0, 100);\n"
"border: 1.5px solid white;\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 5px;\n"
"")
        self.lineEditID.setObjectName("lineEditID")
        self.label_18 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(20, 140, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_18.setObjectName("label_18")
        self.label_16 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(400, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(20, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.label_17 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(20, 40, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_17.setObjectName("label_17")
        self.lineEditTelephone = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditTelephone.setGeometry(QtCore.QRect(540, 40, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineEditTelephone.setFont(font)
        self.lineEditTelephone.setStyleSheet("background-color: rgba(0, 0, 0, 100);\n"
"border: 1.5px solid white;\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 5px;\n"
"")
        self.lineEditTelephone.setObjectName("lineEditTelephone")
        self.lineEditEmail = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditEmail.setGeometry(QtCore.QRect(540, 90, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineEditEmail.setFont(font)
        self.lineEditEmail.setStyleSheet("background-color: rgba(0, 0, 0, 100);\n"
"border: 1.5px solid white;\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 5px;\n"
"")
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditEmail_2 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditEmail_2.setGeometry(QtCore.QRect(540, 140, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineEditEmail_2.setFont(font)
        self.lineEditEmail_2.setStyleSheet("background-color: rgba(0, 0, 0, 100);\n"
"border: 1.5px solid white;\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 5px;\n"
"")
        self.lineEditEmail_2.setObjectName("lineEditEmail_2")
        self.groupBoxSchedule_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxSchedule_2.setGeometry(QtCore.QRect(590, 70, 481, 411))
        font = QtGui.QFont()
        font.setFamily("UTM Bebas")
        font.setPointSize(14)
        self.groupBoxSchedule_2.setFont(font)
        self.groupBoxSchedule_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBoxSchedule_2.setObjectName("groupBoxSchedule_2")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.groupBoxSchedule_2)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.tableWidgetSchedule = QtWidgets.QTableWidget(parent=self.groupBoxSchedule_2)
        self.tableWidgetSchedule.setStyleSheet("background: transparent;")
        self.tableWidgetSchedule.setObjectName("tableWidgetSchedule")
        self.tableWidgetSchedule.setColumnCount(7)
        self.tableWidgetSchedule.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetSchedule.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetSchedule.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetSchedule.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetSchedule.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetSchedule.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetSchedule.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetSchedule.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetSchedule.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetSchedule.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetSchedule.setHorizontalHeaderItem(6, item)
        self.horizontalLayout_29.addWidget(self.tableWidgetSchedule)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1091, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("UTM Eremitage")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1092, 26))
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
        self.groupBox_2.setTitle(_translate("MainWindow", "List of Client:"))
        item = self.tableWidgetClient.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidgetClient.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidgetClient.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidgetClient.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidgetClient.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidgetClient.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Full Name"))
        item = self.tableWidgetClient.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "UserName"))
        item = self.tableWidgetClient.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Telephone"))
        item = self.tableWidgetClient.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidgetClient.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "RegisID"))
        item = self.tableWidgetClient.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidgetClient.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Branch"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Function:"))
        self.pushButtonClear.setText(_translate("MainWindow", "Clear"))
        self.pushButtonDelete.setText(_translate("MainWindow", "Delete"))
        self.groupBox.setTitle(_translate("MainWindow", "Client\'s Detailed Information:"))
        self.label_14.setText(_translate("MainWindow", "Full Name:"))
        self.radioButtonMale.setText(_translate("MainWindow", "Male"))
        self.label_12.setText(_translate("MainWindow", "Telephone:"))
        self.label_15.setText(_translate("MainWindow", "Branch:"))
        self.radioButtonFemale.setText(_translate("MainWindow", "Female"))
        self.label_18.setText(_translate("MainWindow", "Type:"))
        self.label_16.setText(_translate("MainWindow", "Email:"))
        self.label_13.setText(_translate("MainWindow", "Gender"))
        self.label_17.setText(_translate("MainWindow", "ID:"))
        self.groupBoxSchedule_2.setTitle(_translate("MainWindow", "CLIENT\'S SCHEDULE:"))
        item = self.tableWidgetSchedule.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Morning"))
        item = self.tableWidgetSchedule.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Afternoon"))
        item = self.tableWidgetSchedule.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Evening"))
        item = self.tableWidgetSchedule.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mon"))
        item = self.tableWidgetSchedule.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tue"))
        item = self.tableWidgetSchedule.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Wed"))
        item = self.tableWidgetSchedule.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Thu"))
        item = self.tableWidgetSchedule.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Fri"))
        item = self.tableWidgetSchedule.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Sat"))
        item = self.tableWidgetSchedule.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sun"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">CLIENT MANAGEMENT</span></p></body></html>"))
