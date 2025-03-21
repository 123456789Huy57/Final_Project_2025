import json
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow
from FinalProject.libs.DataConnector import DataConnector
from FinalProject.ui.SignUp.SignUp import Ui_MainWindow

CLIENT_FILE = "D:/TMĐT/Programming Technique/ProTech/FinalProject/dataset/client.json"

class SignUpEXT(Ui_MainWindow):
    def __init__(self, username=""):
        super().__init__()
        self.username = username
        self.dc = DataConnector()
        self.all_PT = self.dc.get_all_personaltrainer()
        self.all_Client = self.dc.get_all_client()
        self.Signedup_PT = []
        self.current_client = None
        self.selected_list_PT = None
        self.selected_signedup_PT = None
        self.MainWindow = None

    def setupUi(self, MainWindow, client_username=None):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        client_username = client_username or self.username

        if client_username:
            self.setup_client(client_username)

        self.show_all_PT()
        self.show_signedup_PT()
        self.setupSignalAndSlot()

    def setupSignalAndSlot(self):
        self.pushButtonSignUp.clicked.connect(self.process_signup_PT)
        self.pushButtonCancel.clicked.connect(self.process_cancel_PT)
        self.pushButtonVerify.clicked.connect(self.process_confirm_signup)
        self.pushButtonReturnSignUpPT.clicked.connect(self.process_return_to_client_window)
        self.tableWidgetPT.itemSelectionChanged.connect(self.process_select_list_PT)
        self.tableWidgetPT2.itemSelectionChanged.connect(self.process_select_signedup_PT)

    def setup_client(self, client_username):
        matched_client = next((c for c in self.all_Client if c.Username == client_username), None)
        if not matched_client:
            matched_client = next((c for c in self.all_Client if c.Full_Name == client_username), None)
        if not matched_client:
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Client không tồn tại trong hệ thống!")
            return False

        self.current_client = matched_client
        self.username = client_username
        # Load PT đã đăng ký từ RegisID trong client.json
        if self.current_client.RegisID and self.current_client.RegisID != "None":
            pt = next((p for p in self.all_PT if p.RegisID == self.current_client.RegisID), None)
            if pt:
                self.Signedup_PT = [pt]
        return True

    def show_all_PT(self):
        self.tableWidgetPT.setRowCount(0)
        for pt in self.all_PT:
            row = self.tableWidgetPT.rowCount()
            self.tableWidgetPT.insertRow(row)
            self.tableWidgetPT.setItem(row, 0, QTableWidgetItem(pt.ID))
            self.tableWidgetPT.setItem(row, 1, QTableWidgetItem(pt.Full_Name))
            self.tableWidgetPT.setItem(row, 2, QTableWidgetItem(pt.Gender))
            self.tableWidgetPT.setItem(row, 3, QTableWidgetItem(pt.Experience))
            self.tableWidgetPT.setItem(row, 4, QTableWidgetItem(pt.TypeofPT))
            self.tableWidgetPT.setItem(row, 5, QTableWidgetItem(pt.Branch))

    def process_select_list_PT(self):
        index = self.tableWidgetPT.currentRow()
        if index < 0:
            return
        self.tableWidgetPT2.clearSelection()
        self.selected_signedup_PT = None
        self.selected_list_PT = self.all_PT[index]

    def process_select_signedup_PT(self):
        index = self.tableWidgetPT2.currentRow()
        if index < 0:
            return
        self.tableWidgetPT.clearSelection()
        self.selected_list_PT = None
        self.selected_signedup_PT = self.Signedup_PT[index]

    def process_signup_PT(self):
        if not self.selected_list_PT:
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng chọn PT để đăng ký!")
            return
        if self.Signedup_PT:
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Bạn đã đăng ký một PT. Hãy sử dụng nút 'Verify' để thay đổi!")
            return

        self.Signedup_PT = [self.selected_list_PT]
        self.update_client_data(self.selected_list_PT)
        self.show_all_PT()
        self.show_signedup_PT()
        QMessageBox.information(self.MainWindow, "Thành công", f"Bạn đã đăng ký PT {self.selected_list_PT.Full_Name} thành công!")
        self.tableWidgetPT.clearSelection()
        self.selected_list_PT = None

    def process_cancel_PT(self):
        if not self.selected_signedup_PT:
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng chọn PT đã đăng ký để hủy!")
            return

        reply = QMessageBox.question(
            self.MainWindow, "Xác nhận hủy đăng ký",
            f"Bạn có chắc chắn muốn hủy đăng ký PT {self.selected_signedup_PT.Full_Name} không?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.No:
            return

        self.Signedup_PT.clear()
        self.update_client_data(None)
        self.show_all_PT()
        self.show_signedup_PT()
        QMessageBox.information(self.MainWindow, "Thành công", "Bạn đã hủy đăng ký PT thành công!")

    def process_confirm_signup(self):
        if not self.selected_list_PT:
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng chọn PT để thay đổi!")
            return
        if not self.Signedup_PT:
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Bạn chưa đăng ký PT nào. Hãy sử dụng nút 'Sign Up' để đăng ký!")
            return

        new_pt = self.selected_list_PT
        current_PT = self.Signedup_PT[0]
        if new_pt.ID == current_PT.ID:
            QMessageBox.information(self.MainWindow, "Thông báo", "Bạn đã đăng ký PT này rồi!")
            return

        reply = QMessageBox.question(
            self.MainWindow, "Xác nhận thay đổi PT",
            f"Bạn đã đăng ký PT {current_PT.Full_Name}. Bạn có muốn thay đổi sang {new_pt.Full_Name} không?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.No:
            return

        self.Signedup_PT = [new_pt]
        self.update_client_data(new_pt)
        self.show_all_PT()
        self.show_signedup_PT()
        QMessageBox.information(self.MainWindow, "Thành công", f"Bạn đã đổi sang PT {new_pt.Full_Name} thành công!")

    def show_signedup_PT(self):
        if not hasattr(self, 'tableWidgetPT2'):
            QMessageBox.critical(self.MainWindow, "Lỗi", "Giao diện chưa khởi tạo đầy đủ!")
            return
        self.tableWidgetPT2.setRowCount(0)
        for pt in self.Signedup_PT:
            row = self.tableWidgetPT2.rowCount()
            self.tableWidgetPT2.insertRow(row)
            self.tableWidgetPT2.setItem(row, 0, QTableWidgetItem(pt.ID))
            self.tableWidgetPT2.setItem(row, 1, QTableWidgetItem(pt.Full_Name))
            self.tableWidgetPT2.setItem(row, 2, QTableWidgetItem(pt.Gender))
            self.tableWidgetPT2.setItem(row, 3, QTableWidgetItem(pt.Experience))
            self.tableWidgetPT2.setItem(row, 4, QTableWidgetItem(pt.TypeofPT))
            self.tableWidgetPT2.setItem(row, 5, QTableWidgetItem(pt.Branch))

    def update_client_data(self, pt=None):
        """Cập nhật dữ liệu RegisID và TypeofPT trong client.json"""
        if not self.current_client:
            return False

        try:
            with open(CLIENT_FILE, "r", encoding="utf-8") as file:
                clients = json.load(file)

            for client in clients:
                if client.get("Username") == self.current_client.Username or client.get("ID") == self.current_client.ID:
                    if pt:  # Nếu có PT được chọn (đăng ký hoặc thay đổi)
                        client["RegisID"] = pt.RegisID
                        client["TypeofPT"] = pt.TypeofPT
                    else:  # Nếu hủy PT
                        client["RegisID"] = "None"
                        client["TypeofPT"] = None
                    break

            with open(CLIENT_FILE, "w", encoding="utf-8") as file:
                json.dump(clients, file, indent=4, ensure_ascii=False)

            # Cập nhật đối tượng current_client
            if pt:
                self.current_client.RegisID = pt.RegisID
                self.current_client.TypeofPT = pt.TypeofPT
            else:
                self.current_client.RegisID = "None"
                self.current_client.TypeofPT = None

            # Cập nhật all_Client trong DataConnector
            self.all_Client = self.dc.get_all_client()
            return True

        except Exception as e:
            print(f"Lỗi khi cập nhật client.json: {str(e)}")
            return False

    def process_return_to_client_window(self):
        from FinalProject.ui.ClientWindow.ClientWindowEXT import ClientWindowEXT

        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = ClientWindowEXT()
        self.myui.setupUi(self.mainwindow)

        # Tải lại dữ liệu từ file
        dc = DataConnector()
        all_clients_refreshed = dc.get_all_client()
        refreshed_client = next((c for c in all_clients_refreshed if c.Username == self.current_client.Username), None)

        if refreshed_client:
            self.myui.current_client = refreshed_client
            self.myui.setClientInfo(refreshed_client)
        else:
            self.myui.current_client = self.current_client
            self.myui.setClientInfo(self.current_client)

        self.mainwindow.show()