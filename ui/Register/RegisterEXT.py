import json
import os
import traceback

from PyQt6.QtWidgets import QMainWindow, QMessageBox

from FinalProject.libs.DataConnector import DataConnector
from FinalProject.models.Location import Location
from FinalProject.ui.Register.Register import Ui_MainWindow


class RegisterEXT(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.dc = DataConnector()
        self.setupSignalAndSlot()
        self.pushButtonRegister.setEnabled(False)  # Vô hiệu hóa nút Sign Up ban đầu

        # Chỉ gọi một phương thức để load địa điểm
        self.locations = self.dc.get_all_location()
        if not self.locations or len(self.locations) == 0:
            # Nếu DataConnector không có dữ liệu, thử tải từ file
            self.populate_location_combobox()
        else:
            # Nếu DataConnector có dữ liệu, hiển thị từ dữ liệu đó
            self.load_locations_from_data()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.lineEditName.setStyleSheet(
            "QLineEdit { background: transparent; border: none; border-bottom: 1px solid white; color: white; }")
        self.lineEditUserName.setStyleSheet(
            "QLineEdit { background: transparent; border: none; border-bottom: 1px solid white; color: white; }")
        self.lineEditPassword.setStyleSheet(
            "QLineEdit { background: transparent; border: none; border-bottom: 1px solid white; color: white; }")
        self.lineEditEmail.setStyleSheet(
            "QLineEdit { background: transparent; border: none; border-bottom: 1px solid white; color: white; }")
        self.lineEditPhone.setStyleSheet(
            "QLineEdit { background: transparent; border: none; border-bottom: 1px solid white; color: white; }")
        self.pushButtonRegister.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);")
        self.pushButtonReturn.clicked.connect(self.process_return_to_sign_in)
        self.pushButtonRegister.clicked.connect(self.process_sign_up_new)
        self.checkBoxTSandPP.stateChanged.connect(self.toggle_signup_button)

    def process_return_to_sign_in(self):
        from FinalProject.ui.LoginClient.LoginClientEXT import LoginClientEXT
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = LoginClientEXT()
        self.myui.setupUi(self.mainwindow)
        self.mainwindow.show()

    def load_locations_from_data(self):
        """Hiển thị danh sách địa điểm từ dữ liệu đã tải"""
        try:
            # Xóa dữ liệu cũ trong QComboBox
            self.comboBoxBranch.clear()
            self.comboBoxBranch.addItem("Chọn địa điểm")  # Thêm tùy chọn mặc định

            # Nếu không có dữ liệu, hiển thị thông báo
            if not self.locations:
                QMessageBox.warning(self.MainWindow, "Lỗi", "Không có dữ liệu địa điểm.")
                return

            # Duyệt qua danh sách và thêm vào ComboBox
            for location in self.locations:
                branch = location.Branch if hasattr(location, 'Branch') else "Không rõ"
                address = location.Address if hasattr(location, 'Address') else "Không rõ"
                display_text = f"{branch} - {address}"  # Hiển thị Branch - Address
                self.comboBoxBranch.addItem(display_text)

            print("Danh sách địa điểm đã được tải vào ComboBox!")

        except Exception as e:
            print(f"Lỗi khi hiển thị địa điểm: {e}")
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Đã xảy ra lỗi: {str(e)}")

    def populate_location_combobox(self):
        """Hiển thị danh sách địa điểm trong ComboBox từ location.json"""
        self.comboBoxBranch.clear()
        self.comboBoxBranch.addItem("Chọn địa điểm")  # Thêm tùy chọn mặc định

        try:
            # Tìm đường dẫn tệp location.json theo nhiều cách khác nhau
            # Cách 1: Sử dụng đường dẫn tương đối từ thư mục hiện tại
            script_dir = os.path.dirname(os.path.abspath(__file__))
            location_paths = [
                # Đường dẫn tương đối từ thư mục hiện tại
                os.path.join(script_dir, "..", "..", "dataset", "location.json"),
                # Đường dẫn tương đối từ thư mục gốc của dự án
                os.path.join(script_dir, "..", "..", "..", "dataset", "location.json"),
                # Đường dẫn tuyệt đối (sửa lại sử dụng raw string)
                r"D:\TMĐT\Programming Technique\ProTech\FinalProject\dataset\location.json"
            ]

            # In ra tất cả các đường dẫn để debug
            print("Đang tìm file location.json ở các vị trí:")
            for path in location_paths:
                print(f"- {path} (Tồn tại: {os.path.exists(path)})")

            # Thử từng đường dẫn cho đến khi tìm thấy file
            location_file = None
            for path in location_paths:
                if os.path.exists(path):
                    location_file = path
                    print(f"Đã tìm thấy file location.json tại: {path}")
                    break

            # Nếu không tìm thấy file ở bất kỳ vị trí nào
            if not location_file:
                error_msg = "Không tìm thấy tệp location.json ở bất kỳ vị trí nào được kiểm tra."
                print(error_msg)
                QMessageBox.critical(self.MainWindow, "Lỗi", error_msg)
                return

            # Mở tệp JSON và đọc dữ liệu
            with open(location_file, "r", encoding="utf-8") as file:
                locations_data = json.load(file)

            if not locations_data:
                QMessageBox.warning(self.MainWindow, "Lỗi", "Không có địa điểm nào để hiển thị.")
                return

            # Chuyển dữ liệu JSON thành danh sách đối tượng Location
            self.locations = [Location(loc["Address"], loc["Branch"]) for loc in locations_data]

            # Thêm dữ liệu vào ComboBox
            for loc in self.locations:
                display_text = f"{loc.Branch} - {loc.Address}"  # Hiển thị Branch - Address
                self.comboBoxBranch.addItem(display_text, loc)  # Lưu cả đối tượng Location

            print("Đã tải danh sách địa điểm vào ComboBox.")

        except FileNotFoundError as e:
            error_msg = f"Không tìm thấy tệp location.json! Chi tiết: {str(e)}"
            print(error_msg)
            QMessageBox.critical(self.MainWindow, "Lỗi", error_msg)
        except json.JSONDecodeError:
            QMessageBox.critical(self.MainWindow, "Lỗi", "Tệp Location.json không đúng định dạng JSON!")
        except Exception as e:
            print(f"Lỗi khi tải địa điểm: {str(e)}")
            traceback.print_exc()
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Đã xảy ra lỗi: {str(e)}")

    def toggle_signup_button(self):
        """Bật / tắt nút Sign Up dựa vào checkBoxAgreement"""
        self.pushButtonRegister.setEnabled(self.checkBoxTSandPP.isChecked())

    def process_sign_up_new(self):
        """Lưu thông tin đăng ký vào Client.json sau khi kiểm tra username trùng lặp"""
        try:
            full_name = self.lineEditName.text().strip()
            email = self.lineEditEmail.text().strip()
            phone = self.lineEditPhone.text().strip()
            username = self.lineEditUserName.text().strip()
            password = self.lineEditPassword.text().strip()
            branch = self.comboBoxBranch.currentText().strip()
            gender = "Nam" if self.radioButtonMale.isChecked() else "Nữ"  # Sửa thành tiếng Anh để khớp với format

            if not all([full_name, email, phone, username, password, branch]):
                self.show_error_message("Vui lòng nhập đầy đủ thông tin!")
                return

            if branch == "Chọn địa điểm":
                self.show_error_message("Vui lòng chọn chi nhánh!")
                return

            # Xác định đường dẫn tệp JSON
            script_dir = os.path.dirname(os.path.abspath(__file__))
            client_paths = [
                os.path.join(script_dir, "..", "..", "dataset", "client.json"),
                os.path.join(script_dir, "..", "..", "..", "dataset", "client.json"),
                r"D:\TMĐT\Programming Technique\ProTech\FinalProject\dataset\client.json"
            ]

            # Tìm file client.json
            client_file = None
            for path in client_paths:
                if os.path.exists(path):
                    client_file = path
                    break

            # Nếu không tìm thấy, tạo file mới ở vị trí đầu tiên
            if not client_file:
                client_file = client_paths[0]
                os.makedirs(os.path.dirname(client_file), exist_ok=True)
                clients = []
            else:
                # Đọc dữ liệu hiện tại từ Client.json
                try:
                    with open(client_file, "r", encoding="utf-8") as file:
                        clients = json.load(file)
                except (FileNotFoundError, json.JSONDecodeError):
                    clients = []

                # Kiểm tra username trùng lặp
                for client in clients:
                    if client.get("Username") == username:
                        self.show_error_message("Username đã tồn tại! Vui lòng chọn username khác.")
                        return

            # Tạo ID mới
            new_id = f"C{len(clients) + 1:03d}"  # Format ID với padding số 0

            # Lấy Branch từ chuỗi hiển thị (ví dụ: "Hà Nội - 1" -> "Hà Nội")
            branch_name = branch.split(" - ")[0] if " - " in branch else branch

            # Tạo đối tượng Client mới
            new_client = {
                "ID": new_id,
                "Full_Name": full_name,
                "Gender": gender,
                "Username": username,
                "Password": password,
                "Branch": branch_name,
                "RegisID": None,
                "Email": email,
                "Phone": phone,
                "Schedule": None
            }
            # Thêm vào danh sách Client và ghi lại file JSON
            clients.append(new_client)
            with open(client_file, "w", encoding="utf-8") as file:
                json.dump(clients, file, indent=4, ensure_ascii=False)

            self.show_info_message("Đăng ký thành công!")
            self.return_to_login()

        except Exception as e:
            print(f"Lỗi trong quá trình đăng ký: {e}")
            traceback.print_exc()
            self.show_error_message(f"Đã xảy ra lỗi: {e}")

    def show_error_message(self, message):
        """Hiển thị thông báo lỗi"""
        msg = QMessageBox(self.MainWindow)
        msg.setText(message)
        msg.setWindowTitle("Lỗi")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.exec()

    def show_info_message(self, message):
        """Hiển thị thông báo thành công"""
        msg = QMessageBox(self.MainWindow)
        msg.setText(message)
        msg.setWindowTitle("Thông báo")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def return_to_login(self):
        """Quay trở lại giao diện LoginClient khi nhấn Sign Up hoặc Back"""
        try:
            from FinalProject.ui.LoginClient.LoginClientEXT import LoginClientEXT
            self.MainWindow.close()
            self.mainwindow = QMainWindow()
            self.myui = LoginClientEXT()
            self.myui.setupUi(self.mainwindow)
            self.mainwindow.show()
        except Exception as e:
            print(f"Lỗi khi mở LoginClientEXT: {e}")
            self.show_error_message(f"Không thể quay lại trang đăng nhập: {e}")