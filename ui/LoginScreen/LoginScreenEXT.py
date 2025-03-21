import traceback

from PyQt6.QtWidgets import QMainWindow
from FinalProject.ui.LoginScreen.LoginScreen import Ui_MainWindow

class LoginScreenEXT(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonPT.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);")
        self.pushButtonClient.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);")
        self.pushButtonManager.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);")
        self.pushButtonClient.clicked.connect(self.process_client)
        self.pushButtonPT.clicked.connect(self.process_pt)
        self.pushButtonManager.clicked.connect(self.process_manager)

    def process_client(self):
        from FinalProject.ui.LoginClient.LoginClientEXT import LoginClientEXT
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = LoginClientEXT()
        self.myui.setupUi(self.mainwindow)
        self.mainwindow.show()

    def process_pt(self):
        from FinalProject.ui.LoginPT.LoginPTEXT import LoginPTEXT
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = LoginPTEXT()
        self.myui.setupUi(self.mainwindow)
        self.mainwindow.show()

    def process_manager(self):
        try:
            from FinalProject.ui.LoginManager.LoginManagerEXT import LoginManagerEXT
            self.MainWindow.close()
            self.mainwindow = QMainWindow()
            self.myui = LoginManagerEXT()
            # Đảm bảo rằng mainwindow được khởi tạo đúng cách trước khi gọi setupUi
            self.myui.setupUi(self.mainwindow)
            self.mainwindow.show()
        except Exception as e:
            print(f"Lỗi chi tiết: {str(e)}")
            traceback.print_exc()



