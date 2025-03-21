from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtCore import QTimer, QDateTime
import json
import os
import pandas as pd
from FinalProject.ui.GymPackage.GymPackage import Ui_MainWindow
from FinalProject.libs.JsonFileFactory import JsonFileFactory
from FinalProject.libs.DataConnector import DataConnector
from FinalProject.ui.ClientWindow.ClientWindowEXT import ClientWindowEXT

# Đường dẫn file JSON và Excel
CLIENT_DATA_PATH = "../dataset/client.json"
REVENUE_EXCEL_PATH = "../dataset/revenue.xlsx"

class GymPackageEXT(Ui_MainWindow):
    def __init__(self, current_client=None):
        self.current_client = current_client
        self.package_days = 0  # Biến tạm để lưu số ngày của gói tập mới
        self.package_price = 0  # Biến lưu giá gói tập (3, 15, hoặc 27 triệu)
        self.package_name = ""  # Biến lưu tên gói tập (1 Month, 6 Months, 12 Months)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.dc = DataConnector()  # Khởi tạo DataConnector
        self.jff = JsonFileFactory()  # Khởi tạo JsonFileFactory
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonVerify.clicked.connect(self.process_verify)
        self.radioButton1Month.clicked.connect(self.process_register)
        self.radioButton6Months.clicked.connect(self.process_register)
        self.radioButton12Months.clicked.connect(self.process_register)
        self.pushButtonReturn.clicked.connect(self.process_return)

    def process_register(self):
        """Tạm lưu số ngày và giá của gói tập khi chọn radio button"""
        if not self.current_client:
            print("Error: Please login first!")
            return

        if self.radioButton1Month.isChecked():
            self.package_days = 30
            self.package_price = 3000000  # 3 triệu VND
            self.package_name = "1 Month"
        elif self.radioButton6Months.isChecked():
            self.package_days = 180
            self.package_price = 15000000  # 15 triệu VND
            self.package_name = "6 Months"
        elif self.radioButton12Months.isChecked():
            self.package_days = 360
            self.package_price = 27000000  # 27 triệu VND
            self.package_name = "12 Months"
        else:
            self.package_days = 0
            self.package_price = 0
            self.package_name = ""
            return

        print(f"Temporarily selected package: {self.package_name} - {self.package_days} days - {self.package_price} VND")

    def process_verify(self):
        if not self.current_client or self.package_days == 0:
            QMessageBox.warning(self.MainWindow, "Error", "Please select a package and login first!")
            return

        try:
            all_clients = self.dc.get_all_client()
            found = False
            for client in all_clients:
                if client.Username == self.current_client.Username:
                    # Cộng số ngày mới với số ngày hiện tại
                    client.Remaining_days = client.Remaining_days + self.package_days
                    # Cập nhật ngày đăng ký gói
                    client.Package_Registration_Date = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
                    # Lưu thông tin gói tập vào __dict__
                    client.__dict__.update({
                        "Package_Name": self.package_name,
                        "Package_Price": self.package_price
                    })

                    # Cập nhật current_client
                    self.current_client = client
                    found = True
                    break

            if not found:
                print(f"Client with Username {self.current_client.Username} not found in client.json")
                QMessageBox.warning(self.MainWindow, "Error", "Client not found!")
                return

            # Ghi lại vào client.json
            self.jff.write_data(all_clients, CLIENT_DATA_PATH)
            print(f"Updated Remaining_days for {self.current_client.Username} to {self.current_client.Remaining_days}")

            # Lưu giao dịch vào file Excel
            self.save_to_excel()

            QMessageBox.information(self.MainWindow, "Success",
                                    f"Package registered! Remaining days: {self.current_client.Remaining_days}")
            self.process_return()

        except Exception as e:
            print(f"Failed to save package: {str(e)}")
            QMessageBox.warning(self.MainWindow, "Error", f"Failed to save package: {str(e)}")

    def save_to_excel(self):
        """Lưu thông tin giao dịch vào file Excel và tính tổng doanh thu"""
        try:
            # Dữ liệu giao dịch
            transaction = {
                "Username": self.current_client.Username,
                "Package_Name": self.package_name,
                "Package_Price": self.package_price,
                "Registration_Date": self.current_client.Package_Registration_Date
            }

            # Đọc file Excel hiện có (nếu tồn tại)
            if os.path.exists(REVENUE_EXCEL_PATH):
                df = pd.read_excel(REVENUE_EXCEL_PATH, sheet_name="Transactions")
                df = pd.DataFrame(df)
            else:
                # Nếu file chưa tồn tại, tạo mới với các cột
                df = pd.DataFrame(columns=["Username", "Package_Name", "Package_Price", "Registration_Date"])

            # Thêm giao dịch mới
            new_row = pd.DataFrame([transaction])
            df = pd.concat([df, new_row], ignore_index=True)

            # Tính tổng doanh thu
            total_revenue = df["Package_Price"].sum()

            # Ghi lại vào file Excel
            with pd.ExcelWriter(REVENUE_EXCEL_PATH, engine="openpyxl", mode="w") as writer:
                # Ghi sheet Transactions
                df.to_excel(writer, sheet_name="Transactions", index=False)
                # Ghi sheet Summary để hiển thị tổng doanh thu
                summary_df = pd.DataFrame({"Total Revenue (VND)": [total_revenue]})
                summary_df.to_excel(writer, sheet_name="Summary", index=False)

            print(f"Saved transaction to {REVENUE_EXCEL_PATH}. Total Revenue: {total_revenue} VND")

        except Exception as e:
            print(f"Failed to save to Excel: {str(e)}")
            QMessageBox.warning(self.MainWindow, "Error", f"Failed to save to Excel: {str(e)}")

    def process_return(self):
        """Quay lại ClientWindowEXT và hiển thị số ngày còn lại"""
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = ClientWindowEXT()
        self.myui.setupUi(self.mainwindow)
        if self.current_client:
            self.myui.setClientInfo(self.current_client)
            self.myui.start_countdown(self.current_client)
        self.mainwindow.show()

