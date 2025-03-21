import pandas as pd
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget, QHBoxLayout, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

from FinalProject.ui.ManagerWindow.ManagerWindowEXT import ManagerWindowEXT
from FinalProject.ui.ValueReporting.ValueReporting import Ui_MainWindow


class ValueReportingEXT(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def setupSignalAndSlot(self):
        self.actionExcel_File.triggered.connect(self.process_expense)
        self.actionExcel_File_Revenue.triggered.connect(self.process_revenue)
        self.pushButtonReturn.clicked.connect(self.process_return)

    def process_expense(self):
        file_path = "../dataset/Expenses.xlsx"

        # Đọc dữ liệu từ Excel
        try:
            df = pd.read_excel(file_path)
        except Exception as e:
            print(f"Error reading Excel file: {e}")
            return

        # Kiểm tra dữ liệu
        if df.shape[1] < 2:
            print("Invalid data format in Excel file.")
            return

        # Lấy cột chi phí và giá trị
        expense_col = 'Expenses'
        value_col = 'Amount ( VND)'

        if expense_col not in df.columns or value_col not in df.columns:
            print("Required columns not found in Excel file.")
            return

        # Lấy danh mục trực tiếp bằng tiếng Anh (không dịch)
        categories = df[expense_col].tolist()
        expenses = df[value_col].tolist()

        # Vẽ biểu đồ 3D
        fig = plt.figure(figsize=(7, 6))  # Tăng kích thước để mở rộng không gian
        ax = fig.add_subplot(111, projection='3d')

        # Tùy chỉnh màu sắc tươi sáng
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e1e1', '#ffff99']

        # Dữ liệu cho biểu đồ 3D
        x_pos = np.arange(len(categories))
        y_pos = np.zeros(len(categories))
        z_pos = np.zeros(len(categories))
        dx = np.ones(len(categories)) * 0.4  # Giảm độ rộng của cột để tránh chồng chéo
        dy = np.ones(len(categories)) * 0.4  # Giảm độ sâu của cột
        dz = expenses  # Chiều cao của cột (giá trị chi phí)

        # Vẽ biểu đồ cột 3D
        ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color=colors, zsort='average')

        # Tùy chỉnh trục với khoảng cách chữ tốt hơn
        ax.set_xticks(x_pos)
        ax.set_xticklabels(categories, rotation=45, ha='right', fontsize=9, color='black', linespacing=1.8)  # Tăng khoảng cách và font size
        ax.set_zticks(np.linspace(0, max(expenses), 5))
        ax.set_zticklabels([f'{int(z):,}' for z in np.linspace(0, max(expenses), 5)], fontsize=9, color='black')
        ax.set_yticks([])  # Ẩn trục y

        # Tùy chỉnh tiêu đề bằng tiếng Anh
        ax.set_title("Expense Structure", fontsize=14, pad=20, color='black', weight='bold')

        # Mở rộng khu vực trắng sáng hơn
        fig.patch.set_facecolor('#ffffff')  # Nền trắng hoàn toàn
        ax.set_facecolor('#ffffff')  # Nền trắng cho axes

        # Điều chỉnh góc nhìn 3D để dễ nhìn hơn
        ax.view_init(elev=25, azim=35)  # Tùy chỉnh góc nhìn để tăng hiệu ứng 3D

        # Tạo canvas để hiển thị biểu đồ
        canvas = FigureCanvas(fig)

        # Tìm horizontalLayout_4 trong groupBoxExpenses
        layout = self.groupBoxExpenses.findChild(QHBoxLayout, "horizontalLayout_4")
        if layout is None:
            print("horizontalLayout_4 not found!")
            return

        # Xóa các widget cũ trong layout (nếu có)
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        # Tạo một widget chứa canvas và thêm vào layout
        chart_widget = QWidget()
        chart_layout = QVBoxLayout()
        chart_layout.addWidget(canvas)
        chart_widget.setLayout(chart_layout)

        # Thêm chart_widget vào horizontalLayout_4
        layout.addWidget(chart_widget)

    def process_revenue(self):
        file_path = "../dataset/revenue.xlsx"

        # Đọc dữ liệu từ Excel
        try:
            df = pd.read_excel(file_path, sheet_name="Transactions")
        except Exception as e:
            print(f"Error reading Excel file: {e}")
            return

        # Kiểm tra dữ liệu
        if df.shape[1] < 4:
            print("Invalid data format in Excel file.")
            return

        # Tính tổng doanh thu theo loại gói
        package_revenue = df.groupby('Package_Name')['Package_Price'].sum()

        # Đảm bảo có đủ 3 gói và sắp xếp theo thứ tự mong muốn
        packages = ['1 Month', '6 Months', '12 Months']
        package_revenue = package_revenue.reindex(packages, fill_value=0)

        # Tạo figure mới
        fig, ax = plt.subplots(figsize=(8, 5))

        # Sử dụng màu pastel cho từng gói
        colors = [
            {'left': '#FF9A9E', 'right': '#FAA0A0'},  # Gradient đỏ pastel
            {'left': '#FDFD96', 'right': '#F0E68C'},  # Gradient vàng pastel
            {'left': '#A5F1FF', 'right': '#87CEFA'}  # Gradient xanh pastel
        ]

        # Tạo các thanh ngang với màu gradient
        for i, (package, value) in enumerate(zip(packages, package_revenue.values)):
            # Tạo gradient bằng cách sử dụng nhiều thanh nhỏ
            num_segments = 50
            segment_width = value / num_segments

            for j in range(num_segments):
                start_pos = j * segment_width
                color_factor = j / num_segments

                # Trộn màu để tạo gradient
                r1, g1, b1 = int(colors[i]['left'][1:3], 16), int(colors[i]['left'][3:5], 16), int(
                    colors[i]['left'][5:7], 16)
                r2, g2, b2 = int(colors[i]['right'][1:3], 16), int(colors[i]['right'][3:5], 16), int(
                    colors[i]['right'][5:7], 16)

                r = r1 + (r2 - r1) * color_factor
                g = g1 + (g2 - g1) * color_factor
                b = b1 + (b2 - b1) * color_factor

                segment_color = f'#{int(r):02x}{int(g):02x}{int(b):02x}'

                ax.barh(package, segment_width, left=start_pos, height=0.5, color=segment_color, edgecolor=None)

        # Thêm text vào từng thanh
        for i, (package, value) in enumerate(zip(packages, package_revenue.values)):
            ax.text(value / 2, i, f'₫{int(value):,}', ha='center', va='center',
                    color='white', fontweight='bold', fontsize=10)

        # Loại bỏ các viền
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        # Ẩn các ticks trên trục x
        ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

        # Định dạng trục y đẹp hơn
        ax.tick_params(axis='y', which='both', labelsize=11, pad=10)

        # Thêm lưới ngang mờ
        ax.grid(axis='x', linestyle='--', alpha=0.2)

        # Thêm tiêu đề
        ax.set_title('Revenue by Package Type', fontsize=16, fontweight='bold', pad=15)

        # Thêm chú thích
        legend_labels = ['Monthly Package', 'Half-Year Package', 'Annual Package']
        legend_handles = [plt.Rectangle((0, 0), 1, 1, fc=colors[i]['left']) for i in range(3)]
        ax.legend(legend_handles, legend_labels, loc='lower right', frameon=False)

        # Thêm khoảng trống ở đầu và cuối của trục y
        ax.margins(y=0.15)

        # Đặt giới hạn trục x để đảm bảo không tràn màn hình
        ax.set_xlim(0, max(package_revenue.values) * 1.1)

        # Tối ưu khoảng cách
        plt.tight_layout(pad=2.0)

        # Tính tổng doanh thu
        total_revenue = package_revenue.sum()

        # Thêm text tổng doanh thu dưới biểu đồ
        fig.text(0.5, 0.01, f'Total Revenue: ₫{int(total_revenue):,}',
                 ha='center', fontsize=12, fontweight='bold')

        # Đặt phông nền màu trắng
        fig.patch.set_facecolor('white')
        ax.set_facecolor('white')

        # Tạo canvas để hiển thị biểu đồ
        canvas = FigureCanvas(fig)

        # Tìm horizontalLayout_2 trong groupBoxRevenue
        layout = self.groupBoxRevenue.findChild(QHBoxLayout, "horizontalLayout_2")
        if layout is None:
            print("horizontalLayout_2 not found!")
            return

        # Xóa các widget cũ trong layout (nếu có)
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        # Tạo một widget chứa canvas và thêm vào layout
        chart_widget = QWidget()
        chart_layout = QVBoxLayout()
        chart_layout.addWidget(canvas)
        chart_widget.setLayout(chart_layout)

        # Thêm chart_widget vào horizontalLayout_2
        layout.addWidget(chart_widget)

    def process_return(self):
        from FinalProject.ui.ManagerWindow.ManagerWindowEXT import ManagerWindowEXT
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = ManagerWindowEXT()
        self.myui.setupUi(self.mainwindow)
        self.mainwindow.show()