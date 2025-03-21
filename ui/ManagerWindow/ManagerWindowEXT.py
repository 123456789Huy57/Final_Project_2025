import json
import traceback

from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QMainWindow, QListWidgetItem, QTableWidgetItem, QMessageBox, QInputDialog
from FinalProject.ui.LoginManager.LoginManagerEXT import LoginManagerEXT
from FinalProject.ui.ManagerWindow.ManagerWindow import Ui_MainWindow

CLIENT_FILE = "../dataset/client.json"
TRAINER_FILE = "../dataset/personaltrainer.json"

class ManagerWindowEXT(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.clients = self.load_clients()
        self.personaltrainers = self.load_personal_trainers()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.show_clients_ui()
        self.show_personaltrainers_ui()
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonReturn.clicked.connect(self.process_return)
        self.tableWidget.itemSelectionChanged.connect(self.display_client_info)  # Khi chọn Client
        self.listWidgetPT.itemSelectionChanged.connect(self.process_filter_clients)
        self.listWidgetPT.itemSelectionChanged.connect(self.display_trainer_info)
        self.pushButtonClear.clicked.connect(self.clear_client_fields)
        self.pushButtonSave.clicked.connect(self.save_or_update_client)
        self.pushButtonDelete.clicked.connect(self.delete_client)
        self.pushButtonRemovePT.clicked.connect(self.remove_PT)
        self.pushButtonValueReporting.clicked.connect(self.report_value)
        self.pushButtonClear_2.clicked.connect(self.clear_pt_fields)
        self.pushButtonAddAccount.clicked.connect(self.new_pt)

    def save_or_update_client(self):
        """Lưu thông tin client đã chỉnh sửa vào file client.json"""
        selected_row = self.tableWidget.currentRow()
        if selected_row < 0:
            QMessageBox.warning(None, "Cảnh báo", "Vui lòng chọn một khách hàng để chỉnh sửa!")
            return

        try:
            # Lấy thông tin từ các trường nhập liệu
            client_id = self.lineEditIDClient.text().strip()
            full_name = self.lineEditFullName.text().strip()
            phone = self.lineEditTelephone.text().strip()
            email = self.lineEditEMail.text().strip()
            branch = self.lineEditBranch_2.text().strip()
            type_of_pt = self.lineEditType.text().strip()

            # Xác định giới tính từ radio buttons
            gender = "Nam" if self.radioButtonMale.isChecked() else "Nữ" if self.radioButtonFemale.isChecked() else ""

            # Lấy remaining_days và xử lý giá trị
            remaining_days_text = self.lineEditRemainingDays.text().strip()
            if remaining_days_text == "Hết hạn tập":
                remaining_days = 0
            else:
                try:
                    remaining_days = int(remaining_days_text)
                except ValueError:
                    QMessageBox.warning(None, "Lỗi", "Số ngày còn lại phải là một số nguyên!")
                    return

            # Kiểm tra dữ liệu đầu vào
            if not all([client_id, full_name, phone, email, branch, type_of_pt, gender]):
                QMessageBox.warning(None, "Lỗi", "Vui lòng điền đầy đủ tất cả các trường!")
                return

            # Tải toàn bộ danh sách client từ file
            all_clients = self.load_clients()

            # Tìm và cập nhật thông tin client
            client_found = False
            for i, client in enumerate(all_clients):
                if client["ID"] == client_id:
                    all_clients[i].update({
                        "Full_Name": full_name,
                        "Gender": gender,
                        "Phone": phone,
                        "Email": email,
                        "Branch": branch,
                        "TypeofPT": type_of_pt,
                        "Remaining_days": remaining_days
                    })
                    client_found = True
                    break

            if not client_found:
                QMessageBox.warning(None, "Lỗi", f"Không tìm thấy khách hàng với ID {client_id}!")
                return

            # Ghi lại toàn bộ danh sách vào file
            with open(CLIENT_FILE, "w", encoding="utf-8") as file:
                json.dump(all_clients, file, indent=4, ensure_ascii=False)

            # Cập nhật danh sách trong bộ nhớ và giao diện
            self.clients = all_clients
            self.show_clients_ui()

            QMessageBox.information(None, "Thành công", "Thông tin khách hàng đã được cập nhật thành công!")

        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Đã xảy ra lỗi khi lưu dữ liệu: {str(e)}")
            traceback.print_exc()

    def process_return(self):

        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = LoginManagerEXT()
        self.myui.setupUi(self.mainwindow)
        self.mainwindow.show()

    def load_clients(self):
        """Tải dữ liệu khách hàng từ Client.json"""
        try:
            with open(CLIENT_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception as e:
            print(f"Lỗi khi tải dữ liệu khách hàng: {e}")
            return []

    def load_personal_trainers(self):
        """Tải dữ liệu huấn luyện viên từ PersonalTrainer.json"""
        try:
            with open(TRAINER_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception as e:
            print(f"Lỗi khi tải dữ liệu huấn luyện viên: {e}")
            return []

    def show_clients_ui(self):
        """Hiển thị danh sách khách hàng trong tableWidgetClient"""
        self.tableWidget.setRowCount(0)

        for client in self.clients:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)

            # Tạo các item cho từng cột
            item_id = QTableWidgetItem(client["ID"])
            item_name = QTableWidgetItem(client["Full_Name"])
            item_username = QTableWidgetItem(client["Username"])
            item_phone = QTableWidgetItem(client["Phone"])
            item_type = QTableWidgetItem(client["TypeofPT"])
            # Thêm cột Remaining days
            remaining_days = client.get("Remaining_days", 0)
            item_remaining_days = QTableWidgetItem("Hết hạn tập" if remaining_days <= 0 else str(remaining_days))
            item_branch = QTableWidgetItem(client["Branch"])

            # Kiểm tra nếu TypeofPT là "newbie" thì tô màu xanh biển nhạt
            if client["TypeofPT"].lower() == "newbie":
                light_blue = QColor(173, 216, 230)  # Màu xanh biển nhạt (Light Blue)
                item_id.setBackground(light_blue)
                item_name.setBackground(light_blue)
                item_username.setBackground(light_blue)
                item_phone.setBackground(light_blue)
                item_type.setBackground(light_blue)
                item_remaining_days.setBackground(light_blue)
                item_branch.setBackground(light_blue)

            # Gán các item vào bảng
            self.tableWidget.setItem(row, 0, item_id)
            self.tableWidget.setItem(row, 1, item_name)
            self.tableWidget.setItem(row, 2, item_username)
            self.tableWidget.setItem(row, 3, item_phone)
            self.tableWidget.setItem(row, 4, item_type)
            self.tableWidget.setItem(row, 5, item_remaining_days)  # Cột Remaining days
            self.tableWidget.setItem(row, 6, item_branch)  # Cột Branch



    def show_personaltrainers_ui(self):
        """Hiển thị danh sách huấn luyện viên trong listWidgetPT"""
        self.listWidgetPT.clear()
        for trainer in self.personaltrainers:
            item = QListWidgetItem(trainer["Full_Name"])
            self.listWidgetPT.addItem(item)

    def display_client_info(self):
        try:
            # Chuyển đến tab Client (giả sử tab Client là tab thứ 1)
            self.tabWidget.setCurrentIndex(1)

            # Hiển thị thông tin Client khi chọn dòng trong bảng
            selected_row = self.tableWidget.currentRow()
            if selected_row < 0:
                return

            selected_client = self.clients[selected_row]
            self.lineEditIDClient.setText(selected_client["ID"])
            self.lineEditFullName.setText(selected_client["Full_Name"])
            self.lineEditTelephone.setText(selected_client["Phone"])
            self.lineEditEMail.setText(selected_client["Email"])
            self.lineEditBranch_2.setText(selected_client["Branch"])
            self.lineEditType.setText(selected_client["TypeofPT"])

            # Hiển thị Remaining_days trong lineEditRemainingDays
            remaining_days = selected_client.get("Remaining_days", 0)
            if remaining_days is None or remaining_days <= 0:
                self.lineEditRemainingDays.setText("Hết hạn tập")
                self.lineEditRemainingDays.setStyleSheet(
                    "background-color: rgba(0, 0, 0, 100); border: 1.5px solid white; color: red; font: 12pt 'Times New Roman';"
                )
            else:
                self.lineEditRemainingDays.setText(str(remaining_days))
                self.lineEditRemainingDays.setStyleSheet(
                    "background-color: rgba(0, 0, 0, 100); border: 1.5px solid white; color: green; font: 12pt 'Times New Roman';"
                )

            gender = selected_client["Gender"].lower()
            if gender == "nam":
                self.radioButtonMale.setChecked(True)
            elif gender == "nữ":
                self.radioButtonFemale.setChecked(True)
        except:
            traceback.print_exc()

    def process_filter_clients(self):
        selected_row = self.listWidgetPT.currentRow()
        if selected_row < 0:
            return
        selected_trainer = self.personaltrainers[selected_row]
        trainer_regis_id = selected_trainer["RegisID"]
        self.clients = [client for client in self.load_clients() if client.get("RegisID") == trainer_regis_id]
        self.show_clients_ui()

    def display_trainer_info(self):
        # Chuyển đến tab PT (giả sử tab PT là tab thứ 1)
        self.tabWidget.setCurrentIndex(0)

        selected_row = self.listWidgetPT.currentRow()
        if selected_row < 0:
            return
        selected_trainer = self.personaltrainers[selected_row]
        self.lineEditID.setText(selected_trainer.get("ID", ""))
        self.lineEditQuantity.setText(selected_trainer.get("Full_Name", ""))
        self.lineEditName.setText(selected_trainer.get("Phone", ""))
        self.lineEditPrice.setText(selected_trainer.get("Email", ""))
        self.lineEditBranch.setText(selected_trainer.get("Branch", ""))
        self.lineEditQuantity_2.setText(selected_trainer.get("Experience", ""))
        self.lineEditQuantity_5.setText(selected_trainer.get("TypeofPT", ""))
        gender = selected_trainer.get("Gender", "").lower()
        if gender == "nam":
            self.radioButtonOfficial.setChecked(True)
        elif gender == "nữ":
            self.radioButtonNon.setChecked(True)

    def clear_client_fields(self):
        """Xóa dữ liệu trên các ô nhập"""
        self.lineEditIDClient.clear()
        self.lineEditFullName.clear()
        self.lineEditTelephone.clear()
        self.lineEditEMail.clear()
        self.lineEditBranch_2.clear()
        self.lineEditType.clear()
        self.radioButtonMale.setChecked(False)
        self.radioButtonFemale.setChecked(False)
        # Tắt tính năng độc quyền của radioButton để có thể bỏ chọn cả hai
        self.radioButtonMale.setAutoExclusive(False)
        self.radioButtonFemale.setAutoExclusive(False)

        # Đặt lại các radioButton về trạng thái không chọn
        self.radioButtonMale.setChecked(False)
        self.radioButtonFemale.setChecked(False)

    def clear_pt_fields(self):
        """Xóa dữ liệu trên các ô nhập"""
        self.lineEditID.clear()
        self.lineEditQuantity.clear()
        self.lineEditName.clear()
        self.lineEditPrice.clear()
        self.lineEditBranch.clear()
        self.lineEditQuantity_2.clear()
        self.lineEditQuantity_5.clear()
        self.radioButtonOfficial.setChecked(False)
        self.radioButtonNon.setChecked(False)

        # Tắt tính năng độc quyền của radioButton để có thể bỏ chọn cả hai
        self.radioButtonOfficial.setAutoExclusive(False)
        self.radioButtonNon.setAutoExclusive(False)

        # Đặt lại các radioButton về trạng thái không chọn
        self.radioButtonOfficial.setChecked(False)
        self.radioButtonNon.setChecked(False)

    def delete_client(self):
        """Xóa Client khỏi danh sách với hộp thoại xác nhận"""
        selected_row = self.tableWidget.currentRow()
        if selected_row < 0:
            return

        selected_client = self.clients[selected_row]
        client_id = selected_client["ID"]

        # Hộp thoại xác nhận xóa
        confirm_dialog = QMessageBox()
        confirm_dialog.setIcon(QMessageBox.Icon.Warning)
        confirm_dialog.setWindowTitle("Xác nhận xóa")
        confirm_dialog.setText(f"Bạn có chắc muốn xóa khách hàng có ID {client_id}?")
        confirm_dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        result = confirm_dialog.exec()
        if result == QMessageBox.StandardButton.Yes:
            try:
                # Tải lại danh sách đầy đủ từ Client.json để không mất dữ liệu
                all_clients = self.load_clients()

                # Xóa khách hàng được chọn khỏi danh sách gốc
                all_clients = [client for client in all_clients if client["ID"] != client_id]

                # Ghi lại danh sách đầy đủ vào file JSON
                with open(CLIENT_FILE, "w", encoding="utf-8") as file:
                    json.dump(all_clients, file, indent=4, ensure_ascii=False)

                # Cập nhật danh sách khách hàng trong bộ nhớ
                self.clients = all_clients

                # Cập nhật danh sách đã lọc (nếu đang lọc theo PT)
                self.process_filter_clients()

                # Cập nhật giao diện
                self.show_clients_ui()
                self.clear_client_fields()
                QMessageBox.information(None, "Thành công", "Khách hàng đã bị xóa thành công.")
            except Exception as e:
                QMessageBox.critical(None, "Lỗi", f"Đã xảy ra lỗi khi xóa khách hàng: {str(e)}")

    def remove_PT(self):
        current_row=self.listWidgetPT.currentRow()
        if current_row>=0:
            item=self.listWidgetPT.item(current_row)
            msg = QMessageBox()
            msg.setText(f"Are you sure you want to remove {item.text()}?")
            msg.setWindowTitle("Removing Confirmation")
            msg.setIcon(QMessageBox.Icon.Question)
            buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            msg.setStandardButtons(buttons)
            result = msg.exec()
            if result == QMessageBox.StandardButton.Yes:
             current_item=self.listWidgetPT.takeItem(current_row)
             del current_item

    def report_value(self):
        from FinalProject.ui.ValueReporting.ValueReportingEXT import ValueReportingEXT
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = ValueReportingEXT()
        self.myui.setupUi(self.mainwindow)
        self.mainwindow.show()

    def new_pt(self):
        from FinalProject.ui.RegisterPT.RegisterPTEXT import RegisterPTEXT
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = RegisterPTEXT()
        self.myui.setupUi(self.mainwindow)
        self.mainwindow.show()





