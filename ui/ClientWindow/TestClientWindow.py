from PyQt6.QtWidgets import QApplication, QMainWindow

from FinalProject.ui.ClientWindow.ClientWindowEXT import ClientWindowEXT


app=QApplication([])
mainwindow=QMainWindow()
myui=ClientWindowEXT()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()