import traceback

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication

from FinalProject.libs.DataConnector import DataConnector
from FinalProject.ui.LoginPT.LoginPT import Ui_MainWindow
from FinalProject.ui.PersonalTrainerWindow.PersonalTrainerWindowEXT import PersonalTrainerWindowEXT


class LoginPTEXT(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
        self.login_attempts = 0
        self.max_attempts = 3
        self.login_window = None

    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.lineEdit.setStyleSheet(
            "QLineEdit { background: transparent; border: none; border-bottom: 1px solid white; color: white; }")
        self.lineEdit_2.setStyleSheet(
            "QLineEdit { background: transparent; border: none; border-bottom: 1px solid white; color: white; }")
        self.pushButtonReturn.clicked.connect(self.process_return_to_login)
        self.pushButton.clicked.connect(self.process_login)
        self.pushButton_2.clicked.connect(self.process_change_password)
    def process_return_to_login(self):
        self.MainWindow.close()
        if self.login_window:  # Kiểm tra xem login_window có tồn tại không
            self.mainwindow = QtWidgets.QMainWindow()  # Tạo QMainWindow mới
            self.login_window.setupUi(self.mainwindow)  # Sử dụng lại instance LoginClientEXT
            self.mainwindow.show()
        else:
            # Trường hợp dự phòng: nếu login_window không được truyền
            from FinalProject.ui.LoginScreen.LoginScreenEXT import LoginScreenEXT
            self.mainwindow = QtWidgets.QMainWindow()
            self.myui = LoginScreenEXT()
            self.myui.setupUi(self.mainwindow)
            self.mainwindow.show()

    def process_login(self):
        try:
            dc = DataConnector()
            uid = self.lineEdit.text()
            pwd = self.lineEdit_2.text()

            # Add some debug print statements

            user = dc.login_personal_trainer(uid, pwd)

            if user:
                self.login_attempts = 0
                self.MainWindow.close()
                self.mainwindow = QMainWindow()
                self.myui = PersonalTrainerWindowEXT(user)  # Pass the user object here
                self.myui.setupUi(self.mainwindow)

                # This line is likely not needed anymore since we're passing user to the constructor
                # self.myui.current_client = user

                self.mainwindow.show()
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
    def process_change_password(self):
        from FinalProject.ui.SendEmail.SendEmailEXT import SendEmailEXT
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = SendEmailEXT()
        self.myui.setupUi(self.mainwindow)
        self.myui.login_window = self  # Truyền instance của LoginClientEXT
        self.mainwindow.show()
