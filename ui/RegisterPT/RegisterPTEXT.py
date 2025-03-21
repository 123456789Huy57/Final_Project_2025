from PyQt6.QtWidgets import QMainWindow, QMessageBox
import json
import traceback

from FinalProject.libs.DataConnector import DataConnector
from FinalProject.ui.ManagerWindow.ManagerWindowEXT import ManagerWindowEXT
from FinalProject.ui.RegisterPT.RegisterPT import Ui_MainWindow

TRAINER_FILE = "../dataset/personaltrainer.json"

class RegisterPTEXT(Ui_MainWindow):
    def setupUi(self, MainWindow):
        try:
            super().setupUi(MainWindow)
            self.MainWindow = MainWindow
            self.dc = DataConnector()
            self.personaltrainers = self.load_personal_trainers()  # Tải danh sách PT hiện tại
            self.setupSignalAndSlot()
            self.pushButtonRegister.setEnabled(False)  # Vô hiệu hóa nút Register ban đầu

            # Load danh sách địa điểm (Branch)
            self.locations = self.dc.get_all_location()
            if not self.locations or len(self.locations) == 0:
                self.populate_location_combobox()
            else:
                self.load_locations_from_data()

            # Kiểm tra dữ liệu nhập để kích hoạt nút Register
            self.lineEditName.textChanged.connect(self.validate_input)
            self.lineEditPhone.textChanged.connect(self.validate_input)
            self.lineEditEmail.textChanged.connect(self.validate_input)
            self.lineEditUserName.textChanged.connect(self.validate_input)
            self.lineEditPassword.textChanged.connect(self.validate_input)
            self.lineEditExperience.textChanged.connect(self.validate_input)
            self.lineEditTypeoPT.textChanged.connect(self.validate_input)
            self.comboBoxBranch.currentTextChanged.connect(self.validate_input)

        except Exception as e:
            traceback.print_exc()
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể khởi tạo giao diện đăng ký PT: {str(e)}")

    def showWindow(self):
        try:
            self.MainWindow.show()
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể hiển thị giao diện đăng ký PT: {str(e)}")

    def setupSignalAndSlot(self):
        self.pushButtonReturn.clicked.connect(self.return_to_manager)
        self.pushButtonRegister.clicked.connect(self.add_new_pt)

    def load_personal_trainers(self):
        """Tải danh sách PT từ file personaltrainer.json"""
        try:
            with open(TRAINER_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception as e:
            print(f"Lỗi khi tải dữ liệu PT: {e}")
            return []

    def validate_input(self):
        """Kiểm tra các trường nhập liệu để kích hoạt nút Register"""
        required_fields = [
            self.lineEditName.text(),
            self.lineEditPhone.text(),
            self.lineEditEmail.text(),
            self.lineEditUserName.text(),
            self.lineEditPassword.text(),
            self.lineEditExperience.text(),
            self.lineEditTypeoPT.text(),
            self.comboBoxBranch.currentText()
        ]
        # Kiểm tra tất cả các trường có được điền không
        all_filled = all(field.strip() for field in required_fields)
        self.pushButtonRegister.setEnabled(all_filled)

    def generate_new_ids(self):
        """Tạo ID và RegisID mới không trùng với các PT hiện có"""
        existing_ids = {pt["ID"] for pt in self.personaltrainers}  # Ví dụ: {'P1', 'P2', ...}
        existing_regis_ids = {pt["RegisID"] for pt in self.personaltrainers}  # Ví dụ: {'R1', 'R2', ...}

        # Tìm ID lớn nhất (P1, P2, ...) và RegisID lớn nhất (R1, R2, ...)
        max_id_number = max([int(id[1:]) for id in existing_ids]) if existing_ids else 0
        max_regis_id_number = max([int(regis_id[1:]) for regis_id in existing_regis_ids]) if existing_regis_ids else 0

        # Tạo ID và RegisID mới
        new_id_number = max(max_id_number, max_regis_id_number) + 1
        new_id = f"P{new_id_number}"  # Ví dụ: P7
        new_regis_id = f"R{new_id_number}"  # Ví dụ: R7

        return new_id, new_regis_id

    def return_to_manager(self):
        """Quay lại ManagerWindowEXT"""
        try:
            self.MainWindow.close()
            self.mainwindow = QMainWindow()
            self.myui = ManagerWindowEXT()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể quay lại ManagerWindow: {str(e)}")

    def add_new_pt(self):
        """Thêm PT mới và lưu vào file JSON"""
        # Tạo ID và RegisID mới
        new_id, new_regis_id = self.generate_new_ids()

        # Tạo dictionary cho PT mới
        new_pt = {
            "ID": new_id,
            "Full_Name": self.lineEditName.text(),
            "Gender": "Nam" if self.radioButtonMale.isChecked() else "Nữ",
            "Username": self.lineEditUserName.text(),
            "Password": self.lineEditPassword.text(),
            "Experience": self.lineEditExperience.text(),
            "TypeofPT": self.lineEditTypeoPT.text(),
            "Branch": self.comboBoxBranch.currentText(),
            "Email": self.lineEditEmail.text(),
            "Phone": self.lineEditPhone.text(),
            "RegisID": new_regis_id
        }

        # Thêm PT mới vào danh sách hiện tại
        self.personaltrainers.append(new_pt)

        # Lưu danh sách PT mới vào file JSON
        try:
            with open(TRAINER_FILE, "w", encoding="utf-8") as file:
                json.dump(self.personaltrainers, file, indent=4, ensure_ascii=False)
            QMessageBox.information(self.MainWindow, "Thành công", "Đăng ký PT thành công!")
            self.return_to_manager()  # Quay lại ManagerWindowEXT để hiển thị PT mới
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể lưu PT mới: {str(e)}")

    def populate_location_combobox(self):
        """Giả lập dữ liệu địa điểm nếu DataConnector không có dữ liệu"""
        locations = ["Hà Nội", "Hồ Chí Minh", "Thủ Đức"]
        self.comboBoxBranch.addItems(locations)

    def load_locations_from_data(self):
        """Tải địa điểm từ DataConnector"""
        try:
            for location in self.locations:
                # Giả định Location có thuộc tính name hoặc tương tự, nếu không thì dùng str(location)
                location_name = getattr(location, 'name', str(location))  # Truy cập thuộc tính name, nếu không có thì chuyển sang str
                self.comboBoxBranch.addItem(location_name)
        except Exception as e:
            traceback.print_exc()
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể tải danh sách địa điểm: {str(e)}")