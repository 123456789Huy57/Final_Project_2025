from PyQt6.QtWidgets import QApplication, QMainWindow

from FinalProject.ui.LoginScreen.LoginScreenEXT import LoginScreenEXT

app=QApplication([])
mainwindow=QMainWindow()
myui=LoginScreenEXT()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()