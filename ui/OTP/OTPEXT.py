from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt6 import QtWidgets
from FinalProject.ui.OTP.OTP import Ui_MainWindow  # Điều chỉnh theo file UI thực tế


class OTPEXT(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.forgot_window = None
        self.correct_otp = None
        self.email = None
        self.setupSignalAndSlot()

    def setForgotWindow(self, forgot_window):
        self.forgot_window = forgot_window

    def setOTP(self, otp, email):
        self.correct_otp = str(otp)
        self.email = email

    def setupSignalAndSlot(self):
        self.pushButtonSendOTP.clicked.connect(self.verify_otp)  # Giả định nút Confirm là pushButtonSendOTP
        self.pushButtonReturn.clicked.connect(self.process_return)

    def verify_otp(self):
        input_otp = self.lineEditOTP.text().strip()  # Giả định có lineEditOTP trong UI
        if input_otp == self.correct_otp:
            QtWidgets.QMessageBox.information(self.MainWindow, "Success", "OTP xác thực thành công!")
            self.MainWindow.close()
            from FinalProject.ui.NewPassword.NewPasswordEXT import NewPasswordEXT
            self.mainwindow = QMainWindow()
            self.new_password_ui = NewPasswordEXT()
            self.new_password_ui.setupUi(self.mainwindow)
            self.new_password_ui.setEmail(self.email)  # Truyền email để cập nhật mật khẩu
            self.new_password_ui.setLoginWindow(self.forgot_window.login_window)  # Truyền login_window để quay lại
            self.mainwindow.show()
        else:
            QtWidgets.QMessageBox.warning(self.MainWindow, "Error", "OTP không đúng!")

    def process_return(self):
        self.MainWindow.close()
        if self.forgot_window:
            self.mainwindow = QMainWindow()
            self.forgot_window.setupUi(self.mainwindow)
            self.mainwindow.show()


