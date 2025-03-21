import traceback
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QApplication
from PyQt6.uic.properties import QtWidgets

from FinalProject.libs.DataConnector import DataConnector
from FinalProject.ui.ClientWindow.ClientWindowEXT import ClientWindowEXT
from FinalProject.ui.LoginClient.LoginClient import Ui_MainWindow

class LoginClientEXT(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.login_window = None  # Khởi tạo thuộc tính login_window
        self.setupSignalAndSlot()
        self.login_attempts = 0
        self.max_attempts = 3

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.lineEdit.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);")
        self.lineEdit_2.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);")
        self.lineEdit.setStyleSheet("QLineEdit { background: transparent; border: none; border-bottom: 1px solid white; color: white; }")
        self.lineEdit_2.setStyleSheet("QLineEdit { background: transparent; border: none; border-bottom: 1px solid white; color: white; }")
        self.pushButton.clicked.connect(self.process_register)
        self.pushButtonReturn.clicked.connect(self.process_return)
        self.pushButtonLogin.clicked.connect(self.process_login)
        self.pushButton_2.clicked.connect(self.process_change_password)
    def process_login(self):
        try:
            dc = DataConnector()
            uid = self.lineEdit.text()
            pwd = self.lineEdit_2.text()


            user = dc.login(uid, pwd)

            if user:
                self.login_attempts = 0
                print("Login successful!")
                self.MainWindow.close()
                self.mainwindow = QMainWindow()
                self.myui = ClientWindowEXT()
                self.myui.setupUi(self.mainwindow)

                # Set the current_client attribute
                self.myui.current_client = user
                self.myui.setClientInfo(user)  # Gọi setClientInfo để hiển thị thông tin

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
            print(f"Login error: {str(e)}")
            traceback.print_exc()
            self.show_error_message(f"Đã xảy ra lỗi trong quá trình đăng nhập: {str(e)}")

    def process_show_client_detail(self, client_window, user_data):
        """Hiển thị thông tin Client lên giao diện"""
        try:
            client_window.lineEditIDClient.setText(user_data.ID if user_data.ID else '')
            client_window.lineEditFullNameClient.setText(user_data.Full_Name if user_data.Full_Name else '')
            client_window.lineEditUserName.setText(user_data.Username if user_data.Username else '')
            client_window.lineEditTelephone.setText(user_data.Phone if user_data.Phone else '')
            client_window.lineEditEmail.setText(user_data.Email if user_data.Email else '')
            client_window.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)
            client_window.lineEditBranch.setText(user_data.Branch if user_data.Branch else '')
            client_window.lineEditPassword.setText(user_data.Password if user_data.Password else '')

            gender = user_data.Gender.lower() if user_data.Gender else ''
            if gender == 'nam':
                client_window.radioButtonMale.setChecked(True)
            elif gender == 'nữ':
                client_window.radioButtonFemale.setChecked(True)
        except Exception as e:
            traceback.print_exc()

    def process_show_trainer_detail(self, client_window, regis_id):
        """Hiển thị thông tin PersonalTrainer tương ứng với Client thông qua RegisID"""
        try:
            dc = DataConnector()
            trainers = dc.get_pt_by_regisID(regis_id)
            if trainers and isinstance(trainers, list):
                trainer = trainers[0]
                client_window.lineEditIDPT.setText(trainer.ID if trainer.ID else '')
                client_window.lineEditFullNamePT.setText(trainer.Full_Name if trainer.Full_Name else '')
                client_window.lineEditTelephone_3.setText(trainer.Phone if trainer.Phone else '')
                client_window.lineEditEmail_2.setText(trainer.Email if trainer.Email else '')
                client_window.lineEditEXP.setText(trainer.Experience if trainer.Experience else '')
                client_window.lineEditType.setText(trainer.TypeofPT if trainer.TypeofPT else '')
                client_window.lineEditBranch_2.setText(trainer.Branch if trainer.Branch else '')
                gender = trainer.Gender.lower() if trainer.Gender else ''
                if gender == 'nam':
                    client_window.radioButtonMalePT.setChecked(True)
                elif gender == 'nữ':
                    client_window.radioButtonFemalePT.setChecked(True)
        except Exception as e:
            traceback.print_exc()

    def show_error_message(self, message):
        """Hiển thị thông báo lỗi"""
        msg = QMessageBox(self.MainWindow)
        msg.setText(message)
        msg.setWindowTitle("Lỗi")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.exec()

    def process_sign_up_for_client(self):
        from FinalProject.ui.Register.RegisterEXT import RegisterEXT
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = RegisterEXT()
        self.myui.setupUi(self.mainwindow)
        self.mainwindow.show()

    def process_return(self):
        self.MainWindow.close()
        if self.login_window:  # Kiểm tra xem login_window có tồn tại không
            self.mainwindow = QMainWindow()  # Use QMainWindow from PyQt6.QtWidgets
            self.login_window.setupUi(self.mainwindow)  # Sử dụng lại instance LoginClientEXT
            self.mainwindow.show()
        else:
            # Trường hợp dự phòng: nếu login_window không được truyền
            from FinalProject.ui.LoginScreen.LoginScreenEXT import LoginScreenEXT
            self.mainwindow = QMainWindow()  # Use QMainWindow from PyQt6.QtWidgets
            self.myui = LoginScreenEXT()
            self.myui.setupUi(self.mainwindow)
            self.mainwindow.show()

    def process_register(self):
        from FinalProject.ui.Register.RegisterEXT import RegisterEXT
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = RegisterEXT()
        self.myui.setupUi(self.mainwindow)
        self.mainwindow.show()

    def process_change_password(self):
        from FinalProject.ui.SendEmail.SendEmailEXT import SendEmailEXT
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = SendEmailEXT()
        self.myui.setupUi(self.mainwindow)
        self.myui.login_window = self  # Truyền instance của LoginClientEXT
        self.mainwindow.show()