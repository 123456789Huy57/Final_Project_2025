import json
import sys
import datetime
import webbrowser

import matplotlib.pyplot as plt
import matplotlib.dates
from matplotlib import patheffects
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (QMainWindow, QTableWidgetItem, QLineEdit, QMessageBox)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import traceback
from FinalProject.libs.JsonFileFactory import JsonFileFactory
from FinalProject.ui.ClientWindow.ClientWindow import Ui_MainWindow
from FinalProject.libs.DataConnector import DataConnector
from FinalProject.ui.SignUp.SignUpEXT import SignUpEXT
from PyQt6.QtCore import QTimer, QDateTime
import numpy as np
import os

B_NAME = "../dataset/bmi_data.json"
CLIENT_DATA_PATH = "../dataset/client.json"


class ClientWindowEXT(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.current_client = None
        self.dc = DataConnector()
        self.jff = JsonFileFactory()
        self.all_Client = self.dc.get_all_client()
        self.client_data = {}
        self.clients = []
        self.username = ""
        self.initSchedule()
        self.load_clients()
        self.create_bmi_file()
        self.setupSignalAndSlot()
        self.canvas = FigureCanvas(plt.figure(figsize=(10, 6)))
        self.horizontalLayout_29.addWidget(self.canvas)
        self.disable_bmi_calculator()

    def create_bmi_file(self):
        """Initialize the BMI data file if it doesn't exist."""
        if not os.path.exists(B_NAME):
            with open(B_NAME, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=4)

    def load_clients(self):
        """Load client data from DataConnector and sync with client.json."""
        try:
            # Đọc dữ liệu trực tiếp từ client.json để đảm bảo dữ liệu mới nhất
            with open(CLIENT_DATA_PATH, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)

            # Cập nhật dữ liệu trong DataConnector
            self.all_Client = self.dc.get_all_client()

            # Đồng bộ dữ liệu từ client.json
            self.client_data = {}
            for client in raw_data:
                self.client_data[client["Username"]] = client
        except Exception as e:
            self.all_Client = []

    def setup_client(self):
        if not hasattr(self, "username") or not self.username:
            print("Chưa có thông tin username.")
            return False
        if self.username in self.client_data:
            print(f"Đã tìm thấy thông tin người dùng: {self.client_data[self.username]}")
            return True
        for key, client in self.client_data.items():
            if client.get("Client_Name") == self.username:
                print(f"Đã tìm thấy thông tin người dùng qua Client_Name: {client}")
                return True
        print("Không tìm thấy người dùng.")
        return False

    def process_show_trainer_detail(self, client_window, regis_id):
        """Display PersonalTrainer info based on RegisID."""
        try:
            trainers = self.dc.get_pt_by_regisID(regis_id)
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
                    client_window.radioButtonFemalePT.setChecked(False)
                elif gender == 'nữ':
                    client_window.radioButtonFemalePT.setChecked(True)
                    client_window.radioButtonMalePT.setChecked(False)
                else:
                    client_window.radioButtonMalePT.setChecked(False)
                    client_window.radioButtonFemalePT.setChecked(False)
                print(f"Đã hiển thị thông tin PT: {trainer.Full_Name}")
            else:
                client_window.lineEditIDPT.setText('')
                client_window.lineEditFullNamePT.setText('')
                client_window.lineEditTelephone_3.setText('')
                client_window.lineEditEmail_2.setText('')
                client_window.lineEditEXP.setText('')
                client_window.lineEditType.setText('')
                client_window.lineEditBranch_2.setText('')
                client_window.radioButtonMalePT.setChecked(False)
                client_window.radioButtonFemalePT.setChecked(False)
                print(f"Không tìm thấy PT với RegisID={regis_id}")
        except Exception as e:
            print(f"Lỗi khi hiển thị thông tin PT: {str(e)}")
            traceback.print_exc()

    def get_client_details(self, username):
        """Get client details by username."""
        client = self.client_data.get(username, {})
        if client:
            return f"Username: {client.get('username', client.get('Client_Name', 'Unknown'))}\nRegisID: {client.get('RegisID', 'N/A')}"
        return "No details found."

    def process_sign_up(self):
        """Switch to SignUp interface if Username exists."""
        if self.current_client and self.current_client.Username:
            self.MainWindow.close()
            self.mainwindow = QMainWindow()
            self.myui = SignUpEXT(self.current_client.Username)
            self.myui.setupUi(self.mainwindow)
            self.mainwindow.show()
        else:
            QMessageBox.warning(None, "Cảnh báo", "Không thể xác định thông tin người dùng!")
            self.process_return_to_login_client()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.tabWidget.setCurrentIndex(0)
        """Connect signals and slots, including BMI functionality."""
        self.pushButtonReturn.clicked.connect(self.process_return_to_login_client)
        self.pushButtonReturn2.clicked.connect(self.process_return_to_login_client)
        self.pushButtonReturn3.clicked.connect(self.process_return_to_login_client)
        self.pushButtonUpdate.clicked.connect(self.process_schedule)
        self.pushButtonSignUp.clicked.connect(self.process_sign_up)
        self.pushButtonGymPackage.clicked.connect(self.process_package)
        self.pushButtonAdvice.clicked.connect(self.process_advice)

        self.pushButtonCalculate.clicked.connect(self.calculate_bmi)
        self.pushButtonCalculate.clicked.connect(self.save_data)

        self.lineEditIDClient.setStyleSheet(
            "font-family: 'Times New Roman'; font-size: 12pt; background: transparent; border: 1px solid white;")
        self.lineEditFullNameClient.setStyleSheet(
            "font-family: 'Times New Roman'; font-size: 12pt; background: transparent; border: 1px solid white;")
        self.lineEditUserName.setStyleSheet(
            "font-family: 'Times New Roman'; font-size: 12pt; background: transparent; border: 1px solid white;")
        self.lineEditPassword.setStyleSheet(
            "font-family: 'Times New Roman'; font-size: 12pt; background: transparent; border: 1px solid white;")
        self.lineEditEmail.setStyleSheet(
            "font-family: 'Times New Roman'; font-size: 12pt; background: transparent; border: 1px solid white;")
        self.lineEditTelephone.setStyleSheet(
            "font-family: 'Times New Roman'; font-size: 12pt; background: transparent; border: 1px solid white;")
        self.lineEditBranch.setStyleSheet(
            "font-family: 'Times New Roman'; font-size: 12pt; background: transparent; border: 1px solid white;")
        self.lineEditIDPT.setStyleSheet(
            "font-family: 'Times New Roman'; font-size: 12pt; background: transparent; border: 1px solid white;")
        self.lineEditFullNamePT.setStyleSheet(
            "font-family: 'Times New Roman'; font-size: 12pt; background: transparent; border: 1px solid white;")
        self.lineEditTelephone_3.setStyleSheet(
            "font-family: 'Times New Roman'; font-size: 12pt; background: transparent; border: 1px solid white;")
        self.lineEditEmail_2.setStyleSheet(
            "font-family: 'Times New Roman'; font-size: 12pt; background: transparent; border: 1px solid white;")
        self.lineEditBranch_2.setStyleSheet(
            "font-family: 'Times New Roman'; font-size: 12pt; background: transparent; border: 1px solid white;")
        self.lineEditEXP.setStyleSheet(
            "font-family: 'Times New Roman'; font-size: 12pt; background: transparent; border: 1px solid white;")
        self.lineEditType.setStyleSheet(
            "font-family: 'Times New Roman'; font-size: 12pt; background: transparent; border: 1px solid white;")
        self.lineEditWeight.setStyleSheet(
            "font-family: 'Times New Roman'; font-size: 12pt; background: transparent; border: 1px solid white;")
        self.lineEditHeight.setStyleSheet(
            "font-family: 'Times New Roman'; font-size: 12pt; background: transparent; border: 1px solid white;")
        self.lineEditResult.setStyleSheet(
            "font-family: 'Times New Roman'; font-size: 12pt; background: transparent; border: 1px solid white;")
        self.lineEditRemainingdays.setStyleSheet(
            "font-family: 'Times New Roman'; font-size: 12pt; background: transparent; border: 1px solid white; color: green;")

    # Chỉ hiển thị phần thay đổi trong setClientInfo
    def setClientInfo(self, client):
        self.current_client = client
        self.username = client.Username if hasattr(client, 'Username') else ""
        if self.current_client:
            self.lineEditIDClient.setText(self.current_client.ID or '')
            self.lineEditFullNameClient.setText(self.current_client.Full_Name or '')
            self.lineEditUserName.setText(self.current_client.Username or '')
            self.lineEditTelephone.setText(self.current_client.Phone or '')
            self.lineEditEmail.setText(self.current_client.Email or '')
            self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)
            self.lineEditBranch.setText(self.current_client.Branch or '')
            self.lineEditPassword.setText(self.current_client.Password or '')
            gender = (self.current_client.Gender or '').lower()
            if gender == 'nam':
                self.radioButtonMale.setChecked(True)
            elif gender == 'nữ':
                self.radioButtonFemale.setChecked(True)
            if hasattr(self.current_client,
                       'RegisID') and self.current_client.RegisID and self.current_client.RegisID != "None":
                self.process_show_trainer_detail(self, self.current_client.RegisID)
            else:
                # Xóa thông tin PT nếu không có RegisID
                self.lineEditIDPT.setText('')
                self.lineEditFullNamePT.setText('')
                self.lineEditTelephone_3.setText('')
                self.lineEditEmail_2.setText('')
                self.lineEditEXP.setText('')
                self.lineEditType.setText('')
                self.lineEditBranch_2.setText('')
                self.radioButtonMalePT.setChecked(False)
                self.radioButtonFemalePT.setChecked(False)
            remaining_days = getattr(self.current_client, 'Remaining_days', 0)
            if remaining_days is None or remaining_days <= 0:
                self.lineEditRemainingdays.setText("Hết hạn tập")
            else:
                self.lineEditRemainingdays.setText(str(remaining_days))
            self.load_schedule()
            self.enable_bmi_calculator()
            self.update_graph()

    def process_advice(self):
        path = r"D:\TMĐT\Programming Technique\ProTech\FinalProject\dataset\camnang.pdf"
        webbrowser.open_new(path)

    def process_return_to_login_client(self):
        """Return to login interface."""
        from FinalProject.ui.LoginClient.LoginClientEXT import LoginClientEXT
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = LoginClientEXT()
        self.myui.setupUi(self.mainwindow)
        self.mainwindow.show()

    def initSchedule(self):
        """Initialize training schedule."""
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.times = ["Morning", "Afternoon", "Evening"]
        self.time_prefixes = {"Morning": "Mor", "Afternoon": "After", "Evening": "Eve"}
        self.checkboxes = {}
        for day_index, day in enumerate(self.days, start=2):
            for time in self.times:
                prefix = self.time_prefixes[time]
                checkbox_name = f"checkBox{prefix}{day_index}"
                checkbox = getattr(self, checkbox_name, None)
                if checkbox:
                    self.checkboxes[(day, time)] = checkbox

    def load_schedule(self):
        """Load saved schedule."""
        print("Bắt đầu load_schedule...")
        for row in range(len(self.times)):
            for col in range(len(self.days)):
                item = self.tableWidget.item(row, col)
                if not item:
                    item = QTableWidgetItem()
                    self.tableWidget.setItem(row, col, item)
                item.setBackground(QColor(173, 216, 230))
        for (day, time), checkbox in self.checkboxes.items():
            checkbox.setChecked(False)
        if self.current_client and hasattr(self.current_client, 'Schedule') and self.current_client.Schedule:
            for schedule in self.current_client.Schedule:
                try:
                    day, time = schedule.split()
                    if day in self.days and time in self.times:
                        self.checkboxes[(day, time)].setChecked(True)
                        row = self.times.index(time)
                        col = self.days.index(day)
                        item = self.tableWidget.item(row, col)
                        if not item:
                            item = QTableWidgetItem()
                            self.tableWidget.setItem(row, col, item)
                        item.setBackground(QColor(255, 250, 0))
                except Exception as e:
                    print(f"Lỗi khi tải lịch {schedule}: {e}")

    def process_schedule(self):
        """Update schedule and save to client.json."""
        for row in range(len(self.times)):
            for col in range(len(self.days)):
                item = self.tableWidget.item(row, col)
                if not item:
                    item = QTableWidgetItem()
                    self.tableWidget.setItem(row, col, item)
                item.setBackground(QColor(173, 216, 230))
        new_schedule = []
        for (day, time), checkbox in self.checkboxes.items():
            if checkbox.isChecked():
                schedule_entry = f"{day} {time}"
                new_schedule.append(schedule_entry)
                row = self.times.index(time)
                col = self.days.index(day)
                item = self.tableWidget.item(row, col)
                if not item:
                    item = QTableWidgetItem()
                    self.tableWidget.setItem(row, col, item)
                item.setBackground(QColor(255, 250, 0))
        schedule_value = new_schedule if new_schedule else None
        if self.current_client:
            self.current_client.Schedule = schedule_value
            success = False
            for client in self.all_Client:
                if client.Username == self.current_client.Username:
                    client.Schedule = schedule_value
                    success = True
                    break
            if success:
                try:
                    self.jff.write_data(self.all_Client, CLIENT_DATA_PATH)
                    QMessageBox.information(self.MainWindow, "Thành công",
                                            "Lịch tập đã được cập nhật và lưu thành công!")
                except Exception as e:
                    print(f"Lỗi khi ghi client.json: {e}")
                    QMessageBox.warning(self.MainWindow, "Lỗi", f"Không thể lưu lịch: {str(e)}")
            else:
                QMessageBox.warning(self.MainWindow, "Lỗi", "Không tìm thấy thông tin client để cập nhật!")

    def disable_bmi_calculator(self):
        """Disable BMI calculator functionality."""
        self.lineEditWeight.setEnabled(False)
        self.lineEditHeight.setEnabled(False)
        self.lineEditResult.setEnabled(False)
        self.pushButtonCalculate.setEnabled(False)
        self.pushButtonAdvice.setEnabled(False)

    def enable_bmi_calculator(self):
        """Enable BMI calculator functionality."""
        self.lineEditWeight.setEnabled(True)
        self.lineEditHeight.setEnabled(True)
        self.lineEditResult.setEnabled(True)
        self.pushButtonCalculate.setEnabled(True)
        self.pushButtonAdvice.setEnabled(True)

    def calculate_bmi(self):
        """Calculate BMI based on input."""
        if not self.current_client:
            QMessageBox.warning(self.MainWindow, "Login Required", "Please login first!")
            return
        try:
            weight_text = self.lineEditWeight.text().strip()
            height_text = self.lineEditHeight.text().strip()
            if not weight_text or not height_text:
                raise ValueError("Please enter both weight and height.")
            weight = float(weight_text)
            height = float(height_text)
            if height <= 0 or weight <= 0:
                raise ValueError("Height and weight must be positive numbers.")
            bmi = round(weight / (height ** 2), 2)
            self.lineEditResult.setText(f"{bmi}")
        except ValueError as e:
            QMessageBox.warning(self.MainWindow, "Input Error", str(e))

    def update_graph(self):
        """Update BMI graph with professional styling and comprehensive health tracking."""
        if not self.current_client:
            self.canvas.figure.clear()
            self.canvas.draw()
            return

        try:
            # Load BMI data from JSON file
            with open(B_NAME, 'r', encoding='utf-8') as f:
                all_data = json.load(f)

            # Filter data for current user
            data = [record for record in all_data if record["username"] == self.current_client.Username]

            if not data:
                self.canvas.figure.clear()
                fig = self.canvas.figure
                fig.set_facecolor('#1a1a1a')
                ax = fig.add_subplot(111)
                ax.set_facecolor('#2d2d2d')
                ax.text(0.5, 0.5,
                        'Welcome to Elite Fitness Tracking\nStart your journey by adding your first measurement',
                        ha='center', va='center', color='#FFD700', fontsize=12, fontweight='bold')
                ax.set_xticks([])
                ax.set_yticks([])
                fig.tight_layout()
                self.canvas.draw()
                return

            # Sort data by date
            data.sort(key=lambda x: x["date"])

            dates = [datetime.datetime.strptime(record["date"], "%Y-%m-%d") for record in data]
            bmi_values = [record["bmi"] for record in data]
            weights = [record["weight"] for record in data]
            heights = [record["height"] for record in data]

            # Create figure with custom style
            self.canvas.figure.clear()
            fig = self.canvas.figure
            fig.set_facecolor('#1a1a1a')

            # Create main BMI plot with adjusted size
            ax = fig.add_subplot(111)
            ax.set_facecolor('#2d2d2d')

            # Plot BMI zones with professional colors and labels
            zone_colors = {
                'Severe Underweight': '#FF5252',
                'Underweight': '#FF7F50',
                'Normal': '#66BB6A',
                'Overweight': '#FFA726',
                'Obese': '#E53935',
                'Severe Obese': '#C62828'
            }

            # Add zones with reduced alpha for better text visibility
            ax.axhspan(0, 16, color=zone_colors['Severe Underweight'], alpha=0.08)
            ax.axhspan(16, 18.5, color=zone_colors['Underweight'], alpha=0.08)
            ax.axhspan(18.5, 24.9, color=zone_colors['Normal'], alpha=0.08)
            ax.axhspan(24.9, 29.9, color=zone_colors['Overweight'], alpha=0.08)
            ax.axhspan(29.9, 34.9, color=zone_colors['Obese'], alpha=0.08)
            ax.axhspan(34.9, 40, color=zone_colors['Severe Obese'], alpha=0.08)

            # Plot BMI line
            line = ax.plot(dates, bmi_values, '-', linewidth=2.5, color='#00E5FF', zorder=5)

            # Add points with custom styling and enable picking
            scatter = ax.scatter(dates, bmi_values,
                                 c=bmi_values,
                                 cmap='RdYlGn_r',
                                 s=80,
                                 zorder=6,
                                 edgecolor='white',
                                 linewidth=1.5,
                                 picker=True,  # Enable picking
                                 pickradius=5)  # Set pick radius

            # Store data points for click event
            self.scatter_points = list(zip(dates, bmi_values, weights, heights))

            # Add click event handler
            def on_pick(event):
                if event.artist != scatter:
                    return

                ind = event.ind[0]
                date = dates[ind]
                bmi = bmi_values[ind]
                weight = weights[ind]
                height = heights[ind]

                # Get BMI category
                bmi_category = "Unknown"
                if bmi < 16:
                    bmi_category = "Severe Underweight"
                elif bmi < 18.5:
                    bmi_category = "Underweight"
                elif bmi < 24.9:
                    bmi_category = "Normal Weight"
                elif bmi < 29.9:
                    bmi_category = "Overweight"
                elif bmi < 34.9:
                    bmi_category = "Obese"
                else:
                    bmi_category = "Severe Obese"

                # Create detailed info box
                info_text = (
                    f"Date: {date.strftime('%Y-%m-%d')}\n"
                    f"BMI: {bmi:.1f}\n"
                    f"Weight: {weight:.1f} kg\n"
                    f"Height: {height:.2f} m\n"
                    f"Category: {bmi_category}"
                )

                # Remove previous info box if exists
                for txt in ax.texts:
                    if hasattr(txt, 'is_info_box'):
                        txt.remove()

                # Calculate position for info box (top right corner)
                # Add new info box at fixed position in top right
                info_box = ax.text(0.98, 0.95, info_text,
                                   transform=ax.transAxes,
                                   fontsize=10,
                                   color='white',
                                   bbox=dict(facecolor='#2d2d2d',
                                             edgecolor='#00E5FF',
                                             boxstyle='round,pad=0.5',
                                             alpha=0.95),
                                   ha='right',
                                   va='top',
                                   zorder=10)
                info_box.is_info_box = True  # Mark as info box

                # Highlight selected point
                scatter.set_sizes([80 if i != ind else 150 for i in range(len(dates))])
                scatter.set_edgecolors(['white' if i != ind else '#00E5FF' for i in range(len(dates))])
                scatter.set_linewidths([1.5 if i != ind else 2.5 for i in range(len(dates))])

                # Store the currently selected point index
                self.selected_point_index = ind

                fig.canvas.draw_idle()

            # Add click anywhere to close info box
            def on_click(event):
                if event.inaxes != ax:  # Click outside the plot
                    # Remove info box
                    for txt in ax.texts:
                        if hasattr(txt, 'is_info_box'):
                            txt.remove()
                    # Reset point sizes and colors
                    scatter.set_sizes([80] * len(dates))
                    scatter.set_edgecolors(['white'] * len(dates))
                    scatter.set_linewidths([1.5] * len(dates))
                    # Reset selected point index
                    if hasattr(self, 'selected_point_index'):
                        del self.selected_point_index
                    fig.canvas.draw_idle()
                elif hasattr(self, 'selected_point_index'):
                    # If clicking on the plot but not on a point, check if we're near the selected point
                    x, y = event.xdata, event.ydata
                    if x is not None and y is not None:
                        selected_date = dates[self.selected_point_index]
                        selected_bmi = bmi_values[self.selected_point_index]
                        # Convert date to matplotlib number for comparison
                        selected_x = matplotlib.dates.date2num(selected_date)
                        # Calculate distance from click to selected point
                        dx = abs(selected_x - x)
                        dy = abs(selected_bmi - y)
                        # If click is far from the selected point, close the info box
                        if dx > 5 or dy > 2:  # Adjust these thresholds as needed
                            for txt in ax.texts:
                                if hasattr(txt, 'is_info_box'):
                                    txt.remove()
                            scatter.set_sizes([80] * len(dates))
                            scatter.set_edgecolors(['white'] * len(dates))
                            scatter.set_linewidths([1.5] * len(dates))
                            del self.selected_point_index
                            fig.canvas.draw_idle()

            # Connect both events
            fig.canvas.mpl_connect('pick_event', on_pick)
            fig.canvas.mpl_connect('button_press_event', on_click)

            # Customize grid
            ax.grid(True, linestyle='--', alpha=0.15, color='#ffffff')

            # Customize axes
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_color('#ffffff')
            ax.spines['bottom'].set_color('#ffffff')

            # Set labels and title with adjusted spacing
            ax.set_xlabel("Timeline", fontsize=10, fontweight='bold', color='#ffffff', labelpad=15)
            ax.set_ylabel("BMI Index", fontsize=10, fontweight='bold', color='#ffffff', labelpad=15)

            title = f"FITNESS PROGRESS TRACKING\n{self.current_client.Full_Name}"
            ax.set_title(title,
                         fontsize=14,
                         fontweight='bold',
                         color='#ffffff',
                         pad=25)

            # Customize ticks with rotation for better spacing
            ax.tick_params(axis='both', colors='#ffffff', labelsize=8)
            plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

            # Add BMI zone labels with adjusted positioning
            y_pos = [8, 17.25, 21.7, 27.4, 32.4, 37.45]
            labels = ['Severe\nUnderweight', 'Underweight', 'Normal\nWeight', 'Overweight', 'Obese', 'Severe\nObese']

            # Position labels to the right of the plot
            for yp, label, color in zip(y_pos, labels, zone_colors.values()):
                ax.text(1.02, yp / 40,  # Normalize y-position and place outside plot
                        label,
                        color='white',
                        fontsize=8,
                        transform=ax.transAxes,
                        verticalalignment='center',
                        bbox=dict(facecolor='#2d2d2d',
                                  edgecolor=color,
                                  alpha=0.7,
                                  boxstyle='round,pad=0.3'))

            # Add stats box with adjusted position and spacing
            latest_bmi = bmi_values[-1]
            latest_weight = weights[-1]
            stats_text = (
                f"Latest BMI: {latest_bmi:.1f}\n"
                f"Latest Weight: {latest_weight:.1f}kg\n"
                f"Total Records: {len(data)}\n"
                f"Days Tracked: {(dates[-1] - dates[0]).days}"
            )

            # Position stats box in top left with padding
            ax.text(0.02, 0.98, stats_text,
                    transform=ax.transAxes,
                    fontsize=9,
                    color='white',
                    verticalalignment='top',
                    bbox=dict(facecolor='#2d2d2d',
                              edgecolor='#00E5FF',
                              boxstyle='round,pad=0.5',
                              alpha=0.9))

            # Add trend analysis with adjusted position
            if len(bmi_values) > 1:
                trend = bmi_values[-1] - bmi_values[0]
                trend_text = f"Overall Trend: {'↑' if trend > 0 else '↓'} {abs(trend):.1f}"
                trend_color = '#FF5252' if trend > 0 else '#66BB6A'

                # Position trend box in bottom right
                ax.text(0.98, 0.02, trend_text,
                        transform=ax.transAxes,
                        fontsize=9,
                        color=trend_color,
                        horizontalalignment='right',
                        verticalalignment='bottom',
                        bbox=dict(facecolor='#2d2d2d',
                                  edgecolor=trend_color,
                                  boxstyle='round,pad=0.3',
                                  alpha=0.9))

            # Add latest BMI annotation with offset to prevent overlap
            ax.annotate(f'{latest_bmi:.1f}',
                        (dates[-1], bmi_values[-1]),
                        xytext=(10, 10),
                        textcoords='offset points',
                        color='white',
                        fontsize=9,
                        bbox=dict(facecolor='#00E5FF',
                                  edgecolor='none',
                                  alpha=0.7,
                                  boxstyle='round,pad=0.3'),
                        arrowprops=dict(arrowstyle='->',
                                        color='#00E5FF',
                                        alpha=0.6))

            # Set y-axis limits with padding
            y_min = max(0, min(bmi_values) - 3)
            y_max = min(42, max(bmi_values) + 3)
            ax.set_ylim(y_min, y_max)

            # Add watermark with reduced opacity
            fig.text(0.98, 0.02, 'GYM MANAGEMENT PRO',
                     fontsize=8,
                     color='#ffffff',
                     alpha=0.2,
                     ha='right',
                     va='bottom')

            # Adjust layout to make room for info box
            fig.subplots_adjust(right=0.85, left=0.12, top=0.9, bottom=0.15)

            self.canvas.draw()
        except Exception as e:
            print(f"Lỗi khi cập nhật đồ thị: {str(e)}")

    def save_data(self):
        """Save BMI data and update graph."""
        if not self.current_client:
            QMessageBox.warning(self.MainWindow, "Login Required", "Please login first!")
            return
        try:
            weight_text = self.lineEditWeight.text().strip()
            height_text = self.lineEditHeight.text().strip()
            if not weight_text or not height_text:
                raise ValueError("Please enter both weight and height.")
            weight = float(weight_text)
            height = float(height_text)
            if height <= 0 or weight <= 0:
                raise ValueError("Height and weight must be positive numbers.")
            bmi = round(weight / (height ** 2), 2)

            # Load existing data
            try:
                with open(B_NAME, 'r', encoding='utf-8') as f:
                    bmi_data = json.load(f)
            except:
                bmi_data = []

            # Add new record
            new_record = {
                "date": datetime.date.today().strftime("%Y-%m-%d"),
                "weight": weight,
                "height": height,
                "bmi": bmi,
                "username": self.current_client.Username
            }
            bmi_data.append(new_record)

            # Save updated data
            with open(B_NAME, 'w', encoding='utf-8') as f:
                json.dump(bmi_data, f, ensure_ascii=False, indent=4)

            self.lineEditResult.setText(f"{bmi}")
            self.update_graph()
            QMessageBox.information(self.MainWindow, "Success", "BMI data saved and chart updated!")
        except ValueError as e:
            QMessageBox.warning(self.MainWindow, "Input Error", str(e))

    def remove_all_data(self):
        """Remove all BMI data for the current user."""
        if not self.current_client:
            QMessageBox.warning(self.MainWindow, "Login Required", "Please login first!")
            return
        reply = QMessageBox.question(self.MainWindow, "Confirm Deletion",
                                     "Are you sure you want to delete all your BMI records?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            try:
                # Load existing data
                with open(B_NAME, 'r', encoding='utf-8') as f:
                    bmi_data = json.load(f)

                # Filter out current user's data
                bmi_data = [record for record in bmi_data if record["username"] != self.current_client.Username]

                # Save updated data
                with open(B_NAME, 'w', encoding='utf-8') as f:
                    json.dump(bmi_data, f, ensure_ascii=False, indent=4)

                # Clear input fields
                self.lineEditWeight.clear()
                self.lineEditHeight.clear()
                self.lineEditResult.clear()

                # Reset the graph to welcome state
                self.canvas.figure.clear()
                fig = self.canvas.figure
                fig.set_facecolor('#1a1a1a')
                ax = fig.add_subplot(111)
                ax.set_facecolor('#2d2d2d')
                ax.text(0.5, 0.5,
                        'Welcome to Elite Fitness Tracking\nStart your journey by adding your first measurement',
                        ha='center', va='center', color='#FFD700', fontsize=12, fontweight='bold')
                ax.set_xticks([])
                ax.set_yticks([])
                fig.tight_layout()
                self.canvas.draw()

                QMessageBox.information(self.MainWindow, "Success", "All BMI data removed!")
            except Exception as e:
                QMessageBox.warning(self.MainWindow, "Error", f"Failed to remove data: {str(e)}")

    def process_package(self):
        from FinalProject.ui.GymPackage.GymPackageEXT import GymPackageEXT
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = GymPackageEXT(self.current_client)
        self.myui.setupUi(self.mainwindow)
        self.mainwindow.show()

    def calculate_remaining_days(self, package):
        # Không cần tính lại, chỉ dùng để kiểm tra định dạng
        try:
            print(f"Package value received: {package}")
            if not package:
                return "N/A"
            if isinstance(package, str) and "day" in package.lower():
                days = int(package.split()[0])
                return str(days)
            else:
                print(f"Package format invalid: {package}")
                return "N/A"
        except Exception as e:
            print(f"Error calculating remaining days: {e}")
            return "N/A"

    def start_countdown(self, client):
        """Đếm ngược số ngày tập theo thời gian thực dựa trên ngày đăng ký"""
        if not hasattr(client, 'Package_Registration_Date') or not client.Package_Registration_Date:
            print("No package registration date found.")
            self.lineEditRemainingdays.setText("Hết hạn tập")
            return

        # Tạo timer để cập nhật mỗi ngày (86400 giây = 1 ngày)
        self.timer = QTimer(self.MainWindow)
        self.timer.timeout.connect(lambda: self.update_remaining_days(client))
        self.timer.start(1000)  # Cập nhật mỗi giây để kiểm tra thời gian thực

    def update_remaining_days(self, client):
        """Cập nhật số ngày còn lại dựa trên thời gian thực"""
        reg_date_str = client.Package_Registration_Date
        reg_date = QDateTime.fromString(reg_date_str, "yyyy-MM-dd HH:mm:ss")
        current_date = QDateTime.currentDateTime()

        # Tính số ngày đã trôi qua kể từ ngày đăng ký
        days_passed = reg_date.daysTo(current_date)
        remaining_days = client.Remaining_days - days_passed

        if remaining_days <= 0:
            self.lineEditRemainingdays.setText("Hết hạn tập")
            self.timer.stop()  # Dừng timer khi hết hạn
        else:
            self.lineEditRemainingdays.setText(str(remaining_days))