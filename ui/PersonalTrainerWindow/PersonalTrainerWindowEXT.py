import json
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from FinalProject.ui.PersonalTrainerWindow.PersonalTrainerWindow import Ui_MainWindow

CLIENT_FILE = r"D:/TMĐT/Programming Technique/ProTech/FinalProject/dataset/client.json"
PT_FILE = r"D:/TMĐT/Programming Technique/ProTech/FinalProject/dataset/personaltrainer.json"


class PersonalTrainerWindowEXT(Ui_MainWindow):
    def __init__(self, pt):
        super().__init__()
        self.all_pt = self.load_json(PT_FILE)
        self.all_clients = self.load_json(CLIENT_FILE)
        self.current_regis_id = pt.RegisID
        print(f"Current RegisID: {self.current_regis_id}")
        self.selected_client = None
        self.day_mapping = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5,
                            "Sunday": 6}
        self.time_mapping = {"Morning": 0, "Afternoon": 1, "Evening": 2}

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        self.load_client_list()
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def load_client_list(self):
        self.tableWidgetClient.setRowCount(0)
        print(f"All clients loaded: {self.all_clients}")
        if not self.all_clients:
            QMessageBox.warning(self.MainWindow, "Thông báo", "Không có dữ liệu Client!")
            return

        filtered_clients = [c for c in self.all_clients if c.get("RegisID") == self.current_regis_id]
        print(f"Filtered clients: {filtered_clients}")
        for client in filtered_clients:
            row = self.tableWidgetClient.rowCount()
            self.tableWidgetClient.insertRow(row)

            # Tạo các item cho từng cột theo thứ tự mới
            item_id = QTableWidgetItem(client["ID"])
            item_name = QTableWidgetItem(client.get("Full_Name", "N/A"))
            item_username = QTableWidgetItem(client.get("Username", "N/A"))
            item_phone = QTableWidgetItem(client.get("Phone", "N/A"))
            item_type = QTableWidgetItem(client.get("TypeofPT", "N/A"))  # Cột 4: TypeofPT
            item_regis_id = QTableWidgetItem(client.get("RegisID", "N/A"))  # Cột 5: RegisID
            item_email = QTableWidgetItem(client.get("Email", "N/A"))
            item_branch = QTableWidgetItem(client.get("Branch", "N/A"))

            # Tô màu xanh nhạt nếu TypeofPT là "newbie"
            if client.get("TypeofPT", "").lower() == "newbie":
                light_blue = QColor(173, 216, 230)  # Màu xanh biển nhạt
                item_id.setBackground(light_blue)
                item_name.setBackground(light_blue)
                item_username.setBackground(light_blue)
                item_phone.setBackground(light_blue)
                item_type.setBackground(light_blue)
                item_regis_id.setBackground(light_blue)
                item_email.setBackground(light_blue)
                item_branch.setBackground(light_blue)

            # Gán các item vào bảng theo thứ tự mới
            self.tableWidgetClient.setItem(row, 0, item_id)  # ID
            self.tableWidgetClient.setItem(row, 1, item_name)  # Full_Name
            self.tableWidgetClient.setItem(row, 2, item_username)  # Username
            self.tableWidgetClient.setItem(row, 3, item_phone)  # Phone
            self.tableWidgetClient.setItem(row, 4, item_type)  # TypeofPT (cột 5 trong giao diện)
            self.tableWidgetClient.setItem(row, 5, item_regis_id)  # RegisID
            self.tableWidgetClient.setItem(row, 6, item_email)  # Email
            self.tableWidgetClient.setItem(row, 7, item_branch)  # Branch

    def show_client_details(self):
        selected_row = self.tableWidgetClient.currentRow()
        print(f"Selected row: {selected_row}")
        if selected_row < 0:
            return

        client_id = self.tableWidgetClient.item(selected_row, 0).text()
        self.selected_client = next((c for c in self.all_clients if c["ID"] == client_id), None)
        print(f"Selected client: {self.selected_client}")

        if not self.selected_client:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Không tìm thấy thông tin Client!")
            return

        self.set_text_safe(self.lineEditID, self.selected_client.get("ID", "N/A"))
        self.set_text_safe(self.lineEditFullName, self.selected_client.get("Full_Name", "N/A"))
        self.set_text_safe(self.lineEditType, self.selected_client.get("TypeofPT", "Chưa đăng ký"))
        self.set_text_safe(self.lineEditTelephone, self.selected_client.get("Phone", "N/A"))
        self.set_text_safe(self.lineEditEmail, self.selected_client.get("Email", "Chưa đăng ký"))
        self.set_text_safe(self.lineEditEmail_2, self.selected_client.get("Branch", "Chưa đăng ký"))

        # Thêm code để cập nhật radioButton dựa trên Gender
        gender = self.selected_client.get("Gender", "")
        if gender == "Nam":
            self.radioButtonMale.setChecked(True)
            self.radioButtonFemale.setChecked(False)
        elif gender == "Nữ":
            self.radioButtonMale.setChecked(False)
            self.radioButtonFemale.setChecked(True)
        else:
            # Nếu không có dữ liệu Gender hoặc giá trị không phải "Nam" hoặc "Nữ"
            self.radioButtonMale.setChecked(False)
            self.radioButtonFemale.setChecked(False)

        self.load_client_schedule(self.selected_client.get("Schedule", []))

    def load_client_schedule(self, schedule_data):
        self.clear_schedule_table()
        print(f"Schedule data: {schedule_data}, Type: {type(schedule_data)}")
        if not schedule_data:
            return

        if isinstance(schedule_data, str):
            schedule_list = schedule_data.split(",")
        elif isinstance(schedule_data, list):
            schedule_list = schedule_data
        else:
            return

        for schedule in schedule_list:
            if isinstance(schedule, str):
                schedule = schedule.replace(" ", "_")
                day_time = schedule.split("_")
                if len(day_time) == 2 and day_time[0] in self.day_mapping and day_time[1] in self.time_mapping:
                    self.mark_schedule_in_table(day_time[0], day_time[1],QColor(255, 250, 0))
                else:
                    print(f"Invalid schedule format: {schedule}")

    def mark_schedule_in_table(self, day, time, color):
        if day in self.day_mapping and time in self.time_mapping:
            row = self.time_mapping[time]
            col = self.day_mapping[day]
            item = self.tableWidgetSchedule.item(row, col)
            if not item:
                item = QTableWidgetItem()
                self.tableWidgetSchedule.setItem(row, col, item)
            item.setBackground(color)

    def clear_schedule_table(self):
        for row in range(3):
            for col in range(7):
                item = self.tableWidgetSchedule.item(row, col)
                if not item:
                    item = QTableWidgetItem()
                    self.tableWidgetSchedule.setItem(row, col, item)
                item.setBackground(QColor(173, 216, 230))

    def set_text_safe(self, widget, text):
        if widget:
            widget.setText(text)

    def setupSignalAndSlot(self):
        self.pushButtonReturn.clicked.connect(self.process_return)
        self.tableWidgetClient.itemSelectionChanged.connect(self.show_client_details)
        self.pushButtonDelete.clicked.connect(self.process_delete)
        self.pushButtonClear.clicked.connect(self.process_clear)
        self.lineEditFullName.setFont(QFont("Times New Roman", 12))
        self.lineEditTelephone.setFont(QFont("Times New Roman", 12))
        self.lineEditType.setFont(QFont("Times New Roman", 12))
        self.lineEditEmail_2.setFont(QFont("Times New Roman", 12))
        self.lineEditEmail.setFont(QFont("Times New Roman", 12))
        self.lineEditID.setFont(QFont("Times New Roman", 12))

    def process_clear(self):
        # Xóa nội dung trên các lineEdit
        self.set_text_safe(self.lineEditID, "")
        self.set_text_safe(self.lineEditFullName, "")
        self.set_text_safe(self.lineEditType, "")
        self.set_text_safe(self.lineEditTelephone, "")
        self.set_text_safe(self.lineEditEmail, "")
        self.set_text_safe(self.lineEditEmail_2, "")

        # Tắt tính năng độc quyền của radioButton để có thể bỏ chọn cả hai
        self.radioButtonMale.setAutoExclusive(False)
        self.radioButtonFemale.setAutoExclusive(False)

        # Đặt lại các radioButton về trạng thái không chọn
        self.radioButtonMale.setChecked(False)
        self.radioButtonFemale.setChecked(False)

        # Bật lại tính năng độc quyền sau khi xóa
        self.radioButtonFemale.setAutoExclusive(True)
        self.radioButtonFemale.setAutoExclusive(True)

        # Làm mới bảng lịch trình về trạng thái mặc định
        self.clear_schedule_table()

        # Đặt lại selected_client về None
        self.selected_client = None

    def process_return(self):
        from FinalProject.ui.LoginPT.LoginPTEXT import LoginPTEXT
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = LoginPTEXT()
        self.myui.setupUi(self.mainwindow)
        self.mainwindow.show()

    def load_json(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def process_delete(self):
        if not self.selected_client:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Không có Client nào được chọn để hủy đăng ký PT!")
            return
        if self.selected_client.get("RegisID") != self.current_regis_id:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Bạn chỉ có thể hủy đăng ký Client do bạn quản lý!")
            return
        reply = QMessageBox.question(
            self.MainWindow, "Xác nhận hủy đăng ký",
            f"Bạn có chắc chắn muốn hủy đăng ký PT cho Client {self.selected_client.get('Full_Name', 'N/A')} không?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.No:
            return
        for client in self.all_clients:
            if client["ID"] == self.selected_client["ID"]:
                client["RegisID"] = None
        with open(CLIENT_FILE, "w", encoding="utf-8") as file:
            json.dump(self.all_clients, file, indent=4, ensure_ascii=False)
        QMessageBox.information(self.MainWindow, "Thành công", "Đã hủy đăng ký PT cho Client!")
        self.load_client_list()