from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from DatasetViewer import Ui_MainWindow
import pandas as pd

class DatasetViewerEx(QMainWindow, Ui_MainWindow):
    def __init__(self, csv_path: str):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Dataset Viewer")
        self.csv_path = csv_path
        self.load_data()

    def load_data(self):
        """Đọc toàn bộ dataset và hiển thị trong tableWidget_Data."""
        try:
            df = pd.read_csv(self.csv_path)
            self.tableWidget_Data.setRowCount(len(df))
            self.tableWidget_Data.setColumnCount(len(df.columns))
            self.tableWidget_Data.setHorizontalHeaderLabels(df.columns)

            for i in range(len(df)):
                for j in range(len(df.columns)):
                    item = QTableWidgetItem(str(df.iat[i, j]))
                    self.tableWidget_Data.setItem(i, j, item)

            self.tableWidget_Data.resizeColumnsToContents()
            print(f"[INFO] Loaded {len(df)} rows and {len(df.columns)} columns from {self.csv_path}")
        except Exception as e:
            print(f"[ERROR] Failed to load dataset: {e}")
