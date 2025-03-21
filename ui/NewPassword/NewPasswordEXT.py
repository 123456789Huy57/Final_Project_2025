import json
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt6 import QtWidgets
from FinalProject.ui.NewPassword.NewPassword import Ui_MainWindow
from FinalProject.ui.LoginClient.LoginClientEXT import LoginClientEXT  # Import để mở lại LoginClientEXT


class NewPasswordEXT(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.email = None
        self.login_window = None
        self.setupSignalAndSlot()

    def setEmail(self, email):
        self.email = email

    def setLoginWindow(self, login_window):
        self.login_window = login_window

    def setupSignalAndSlot(self):
        self.pushButtonUpdate.clicked.connect(self.update_password)
        self.pushButtonReturn.clicked.connect(self.process_return)

    def update_password(self):
        new_password = self.lineEditNewPassword.text().strip()
        confirm_password = self.lineEditConfirmNewPassword.text().strip()

        if not new_password or not confirm_password:
            QtWidgets.QMessageBox.warning(self.MainWindow, "Error", "Vui lòng nhập đầy đủ mật khẩu!")
            return

        if new_password != confirm_password:
            QtWidgets.QMessageBox.warning(self.MainWindow, "Error", "Mật khẩu xác nhận không khớp!")
            return

        # Cập nhật mật khẩu vào cả client.json và personaltrainer.json
        email_lower = self.email.lower()
        updated = False  # Theo dõi xem có cập nhật thành công không

        # Cập nhật client.json
        try:
            with open(r"../dataset/client.json", "r", encoding="utf-8") as f:
                users = json.load(f)
            for user in users:
                if user.get("Email", "").strip().lower() == email_lower:
                    user["Password"] = new_password
                    updated = True
                    print(f"📌 Đã cập nhật mật khẩu cho {email_lower} trong client.json")
                    break
            with open(r"../dataset/client.json", "w", encoding="utf-8") as f:
                json.dump(users, f, indent=4, ensure_ascii=False)
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(self.MainWindow, "Error", "File client.json not found!")
            print("❌ Lỗi: File client.json không tồn tại")
        except json.JSONDecodeError:
            QtWidgets.QMessageBox.warning(self.MainWindow, "Error", "Error reading client.json!")
            print("❌ Lỗi: File client.json không đúng định dạng JSON")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self.MainWindow, "Error", f"Cập nhật client.json thất bại! Lỗi: {str(e)}")
            print(f"❌ Lỗi khi cập nhật client.json: {e}")

        # Cập nhật personaltrainer.json
        try:
            with open(r"../dataset/personaltrainer.json", "r", encoding="utf-8") as f:
                trainers = json.load(f)
            for trainer in trainers:
                if trainer.get("Email", "").strip().lower() == email_lower:
                    trainer["Password"] = new_password
                    updated = True
                    print(f"📌 Đã cập nhật mật khẩu cho {email_lower} trong personaltrainer.json")
                    break
            with open(r"../dataset/personaltrainer.json", "w", encoding="utf-8") as f:
                json.dump(trainers, f, indent=4, ensure_ascii=False)
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(self.MainWindow, "Error", "File personaltrainer.json not found!")
            print("❌ Lỗi: File personaltrainer.json không tồn tại")
        except json.JSONDecodeError:
            QtWidgets.QMessageBox.warning(self.MainWindow, "Error", "Error reading personaltrainer.json!")
            print("❌ Lỗi: File personaltrainer.json không đúng định dạng JSON")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self.MainWindow, "Error",
                                          f"Cập nhật personaltrainer.json thất bại! Lỗi: {str(e)}")
            print(f"❌ Lỗi khi cập nhật personaltrainer.json: {e}")

        if updated:
            QtWidgets.QMessageBox.information(self.MainWindow, "Success", "Mật khẩu đã được cập nhật thành công!")
            # Ngay lập tức mở lại LoginClientEXT sau khi cập nhật thành công
            self.MainWindow.close()
            self.mainwindow = QMainWindow()
            if self.login_window:
                self.login_window.setupUi(self.mainwindow)  # Sử dụng login_window đã truyền
            else:
                # Nếu không có login_window (trường hợp hiếm), tạo mới LoginClientEXT
                new_login_ui = LoginClientEXT()
                new_login_ui.setupUi(self.mainwindow)
            self.mainwindow.show()
            print("📌 Đã mở lại LoginClientEXT")
        else:
            QtWidgets.QMessageBox.warning(self.MainWindow, "Error", "Email không tồn tại trong hệ thống!")
            print(f"❌ Lỗi: Không tìm thấy {email_lower} trong cả client.json và personaltrainer.json")

    def process_return(self):
        self.MainWindow.close()
        if self.login_window:  # Kiểm tra xem login_window có tồn tại không
            self.mainwindow = QtWidgets.QMainWindow()  # Tạo QMainWindow mới
            self.login_window.setupUi(self.mainwindow)  # Sử dụng lại instance LoginClientEXT
            self.mainwindow.show()
        else:
            # Trường hợp dự phòng: nếu login_window không được truyền
            from FinalProject.ui.SendEmail.SendEmailEXT import ForgotPasswordWindow
            self.mainwindow = QtWidgets.QMainWindow()
            self.myui = ForgotPasswordWindow()
            self.myui.setupUi(self.mainwindow)
            self.mainwindow.show()


