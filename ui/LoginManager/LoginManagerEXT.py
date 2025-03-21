import traceback

from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication

from FinalProject.libs.DataConnector import DataConnector
from FinalProject.ui.LoginManager.LoginManager import Ui_MainWindow

class LoginManagerEXT(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        # Đảm bảo rằng UI đã được khởi tạo đầy đủ trước khi thiết lập signal và slot
        self.setupSignalAndSlot()
        self.login_attempts = 0
        self.max_attempts = 3

    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.lineEditUserName.setStyleSheet(
            "QLineEdit { background: transparent; border: none; border-bottom: 1px solid white; color: white; }")
        self.lineEditPassword.setStyleSheet(
            "QLineEdit { background: transparent; border: none; border-bottom: 1px solid white; color: white; }")
        self.pushButtonReturn.clicked.connect(self.process_return_to_login)
        self.pushButton.clicked.connect(self.process_login)

    def process_return_to_login(self):
        from FinalProject.ui.LoginScreen.LoginScreenEXT import LoginScreenEXT
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = LoginScreenEXT()
        self.myui.setupUi(self.mainwindow)
        self.mainwindow.show()

    def process_login(self):
        from FinalProject.ui.ManagerWindow.ManagerWindowEXT import ManagerWindowEXT
        try:
            dc = DataConnector()
            uid = self.lineEditUserName.text()
            pwd = self.lineEditPassword.text()

            # Add some debug print statements
            print(f"Attempting login with username: {uid}")

            user = dc.login_manager(uid, pwd)

            if user:
                self.login_attempts = 0
                print("Login successful!")
                self.MainWindow.close()
                self.mainwindow = QMainWindow()
                self.myui = ManagerWindowEXT()
                self.myui.setupUi(self.mainwindow)
                self.mainwindow.show()
                # Set the current_client attribute
                self.myui.current_client = user
            else:
                self.login_attempts += 1
                remaining_attempts = self.max_attempts - self.login_attempts
                if self.login_attempts >= self.max_attempts:
                    self.show_error_message("Bạn đã nhập sai quá 3 lần. Chương trình sẽ đóng.")
                    QApplication.instance().quit()
                else:
                    self.show_error_message(
                        f"Tên đăng nhập hoặc mật khẩu không đúng! Bạn còn {remaining_attempts} lần thử.")
        except Exception as e:
            # Enhanced error reporting
            print(f"Login error: {str(e)}")
            traceback.print_exc()
            self.show_error_message(f"Đã xảy ra lỗi trong quá trình đăng nhập: {str(e)}")

    def show_error_message(self, message):
        """Hiển thị thông báo lỗi"""
        msg = QMessageBox(self.MainWindow)
        msg.setText(message)
        msg.setWindowTitle("Lỗi")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.exec()