import json
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow

from FinalProject.ui.SendEmail.SendEmail import Ui_MainWindow


class SendEmailEXT(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.login_window = None  # Thêm thuộc tính để lưu LoginClientEXT
        self.setupSignalAndSlot()
        self.otp = None


    def setupSignalAndSlot(self):
        # Kết nối các nút bấm
        self.pushButtonSendOTP.clicked.connect(self.send_otp_email)
        self.pushButtonReturn.clicked.connect(self.process_return)

    def check_email_exists(self, email):
        print(f"📌 Kiểm tra email: {email}")
        email = email.strip().lower()
        all_emails = set()  # Sử dụng set để tránh trùng lặp

        # Kiểm tra file client.json
        try:
            with open(r"../dataset/client.json", "r", encoding="utf-8") as f:
                users = json.load(f)
            client_emails = [user.get("Email", "").strip().lower() for user in users if user.get("Email")]
            all_emails.update(client_emails)
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(self, "Error", "File client.json not found!")
            print("❌ Lỗi: File client.json không tồn tại")
        except json.JSONDecodeError:
            QtWidgets.QMessageBox.warning(self, "Error", "Error reading client.json!")
            print("❌ Lỗi: File client.json không đúng định dạng JSON")

        # Kiểm tra file personaltrainer.json
        try:
            with open(r"../dataset/personaltrainer.json", "r", encoding="utf-8") as f:
                trainers = json.load(f)
            trainer_emails = [trainer.get("Email", "").strip().lower() for trainer in trainers if trainer.get("Email")]
            all_emails.update(trainer_emails)
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(self, "Error", "File personaltrainer.json not found!")
            print("❌ Lỗi: File personaltrainer.json không tồn tại")
        except json.JSONDecodeError:
            QtWidgets.QMessageBox.warning(self, "Error", "Error reading personaltrainer.json!")
            print("❌ Lỗi: File personaltrainer.json không đúng định dạng JSON")

        print("📌 Email nhập vào:", email)
        return email in all_emails

    def send_otp_email(self):
        try:
            from FinalProject.ui.OTP.OTPEXT import OTPEXT
        except ImportError:
            QtWidgets.QMessageBox.critical(self.MainWindow, "Error", "Không thể import OTPWindow. Kiểm tra đường dẫn!")
            print("❌ Lỗi: Không tìm thấy file OTPWindow")
            return

        email = self.lineEditEmail.text().strip()

        if not email:
            QtWidgets.QMessageBox.warning(self.MainWindow, "Error", "Bạn chưa nhập email!")
            print("⚠ LỖI: Email nhập vào bị rỗng!")
            return

        if not self.check_email_exists(email):
            QtWidgets.QMessageBox.warning(self.MainWindow, "Error", "Email không tồn tại trong hệ thống!")
            print("⚠ LỖI: Email không tồn tại trong cơ sở dữ liệu")
            return

        self.otp = random.randint(100000, 999999)
        sender_email = "nhatkhoaledang@gmail.com"
        sender_password = "bhbt xmvw jiig ealw"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = "OTP Verification Code"
        msg.attach(MIMEText(f"Your OTP code is: {self.otp}", 'plain'))

        otp_file = r"../dataset/otp_data.json"
        try:
            with open(otp_file, "r", encoding="utf-8") as f:
                otp_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            otp_data = {}
            print("📌 File otp_data.json không tồn tại hoặc lỗi, tạo mới")

        otp_data[email] = self.otp
        with open(otp_file, "w", encoding="utf-8") as f:
            json.dump(otp_data, f, indent=4, ensure_ascii=False)

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, msg.as_string())
            server.quit()
            QtWidgets.QMessageBox.information(self.MainWindow, "Success", f"OTP đã gửi đến {email}!")
        except smtplib.SMTPAuthenticationError:
            QtWidgets.QMessageBox.warning(self.MainWindow, "Error", "Xác thực email thất bại. Kiểm tra email/mật khẩu!")
            print("❌ Lỗi: Thông tin đăng nhập email không đúng")
            return
        except Exception as e:
            QtWidgets.QMessageBox.warning(self.MainWindow, "Error", f"Gửi OTP thất bại! Lỗi: {str(e)}")
            print(f"❌ Lỗi khi gửi email: {e}")
            return

        # Đóng cửa sổ hiện tại
        self.MainWindow.close()

        # Tạo và hiển thị OTPWindow
        self.otp_mainwindow = QtWidgets.QMainWindow()  # Tạo QMainWindow mới
        self.otp_window = OTPEXT()  # Tạo instance của OTPWindow
        self.otp_window.setupUi(self.otp_mainwindow)  # Gắn giao diện vào QMainWindow
        self.otp_window.setForgotWindow(self)  # Truyền ForgotPasswordWindow
        self.otp_window.setOTP(self.otp, email)  # Truyền OTP và email
        self.otp_mainwindow.show()  # Hiển thị cửa sổ
    def process_return(self):
        self.MainWindow.close()
        if self.login_window:  # Kiểm tra xem login_window có tồn tại không
            self.mainwindow = QtWidgets.QMainWindow()  # Tạo QMainWindow mới
            self.login_window.setupUi(self.mainwindow)  # Sử dụng lại instance LoginClientEXT
            self.mainwindow.show()
        else:
            # Trường hợp dự phòng: nếu login_window không được truyền
            from FinalProject.ui.LoginClient.LoginClientEXT import LoginClientEXT
            self.mainwindow = QtWidgets.QMainWindow()
            self.myui = LoginClientEXT()
            self.myui.setupUi(self.mainwindow)
            self.mainwindow.show()