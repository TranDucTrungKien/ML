# File: Qt/MainWindowEx.py
from PyQt6.QtWidgets import (
    QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
)
from MainWindow import Ui_MainWindow
from FileUtil import FileUtil
from DatasetViewerEx import DatasetViewerEx
import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


class MainWindowEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("House Price Prediction - Qt Edition")

        # Biến toàn cục
        self.dataset_path = None
        self.df = None
        self.lm = None
        self.X_train, self.X_test, self.y_train, self.y_test = (None,) * 4

        # Gắn các sự kiện (signal-slot)
        self.pushButton_PickData.clicked.connect(self.pick_dataset)
        self.pushButton_ViewData.clicked.connect(self.view_dataset)
        self.pushButton_TrainModel.clicked.connect(self.train_model)
        self.pushButton_EvaluateModel.clicked.connect(self.evaluate_model)
        self.pushButton_SaveModel.clicked.connect(self.save_model)
        self.pushButton_LoadModel.clicked.connect(self.load_model)
        self.pushButton_Predict.clicked.connect(self.predict)

    # ------------------------------------------------------------
    # BƯỚC 1: PICK DATASET
    # ------------------------------------------------------------
    def pick_dataset(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select dataset file",
            "",
            "CSV Files (*.csv);;All Files (*)"
        )
        if file_path:
            self.lineEdit_Select.setText(file_path)
            self.dataset_path = file_path
            QMessageBox.information(self, "Dataset selected", f"Loaded dataset:\n{file_path}")

    # ------------------------------------------------------------
    # BƯỚC 2: VIEW DATASET
    # ------------------------------------------------------------
    def view_dataset(self):
        if not self.dataset_path:
            QMessageBox.warning(self, "Warning", "Please pick a dataset first.")
            return
        # Giữ tham chiếu để không bị thu hồi
        self.dataset_viewer = DatasetViewerEx(self.dataset_path)
        self.dataset_viewer.show()

    # ------------------------------------------------------------
    # BƯỚC 3: TRAIN MODEL
    # ------------------------------------------------------------
    def train_model(self):
        try:
            if not self.dataset_path:
                QMessageBox.warning(self, "Warning", "Please select a dataset first.")
                return

            self.df = pd.read_csv(self.dataset_path)
            train_rate = float(self.lineEdit_TrainingRate.text())
            ratio = train_rate / 100.0

            X = self.df[['Avg. Area Income',
                         'Avg. Area House Age',
                         'Avg. Area Number of Rooms',
                         'Avg. Area Number of Bedrooms',
                         'Area Population']]
            y = self.df['Price']

            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                X, y, test_size=1 - ratio, random_state=101
            )

            self.lm = LinearRegression()
            self.lm.fit(self.X_train, self.y_train)

            QMessageBox.information(self, "Training", "Model training completed successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Training failed:\n{e}")

    # ------------------------------------------------------------
    # BƯỚC 4: EVALUATE MODEL
    # ------------------------------------------------------------
    def evaluate_model(self):
        if self.lm is None:
            QMessageBox.warning(self, "Warning", "Please train or load a model first.")
            return
        try:
            predictions = self.lm.predict(self.X_test)

            # Ghi dữ liệu vào bảng Data
            self.tableWidget_Data.setRowCount(len(self.X_test))
            for i in range(len(self.X_test)):
                row_data = [
                    self.X_test.iloc[i, 0],
                    self.X_test.iloc[i, 1],
                    self.X_test.iloc[i, 2],
                    self.X_test.iloc[i, 3],
                    self.X_test.iloc[i, 4],
                    self.y_test.iloc[i],
                    predictions[i]
                ]
                for j, val in enumerate(row_data):
                    item = QTableWidgetItem(str(round(val, 4)))
                    self.tableWidget_Data.setItem(i, j, item)

            # Hiển thị hệ số
            coeff_df = pd.DataFrame(self.lm.coef_,
                                    self.X_train.columns,
                                    columns=['Coefficient'])
            self.tableWidget_Coeff.setRowCount(len(coeff_df))
            for i, (name, value) in enumerate(coeff_df.iterrows()):
                self.tableWidget_Coeff.setItem(i, 0, QTableWidgetItem(str(name)))
                self.tableWidget_Coeff.setItem(i, 1, QTableWidgetItem(str(round(value[0], 6))))

            # Tính các metrics
            mae = metrics.mean_absolute_error(self.y_test, predictions)
            mse = metrics.mean_squared_error(self.y_test, predictions)
            rmse = np.sqrt(mse)

            self.lineEdit_MAE.setText(str(round(mae, 4)))
            self.lineEdit_MSE.setText(str(round(mse, 4)))
            self.lineEdit_RMSE.setText(str(round(rmse, 4)))

            QMessageBox.information(self, "Evaluation", "Model evaluation completed successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Evaluation failed:\n{e}")

    # ------------------------------------------------------------
    # BƯỚC 5: SAVE MODEL
    # ------------------------------------------------------------
    def save_model(self):
        if self.lm is None:
            QMessageBox.warning(self, "Warning", "No model to save. Please train a model first.")
            return
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save Trained Model", "model/housingmodel.zip", "ZIP Files (*.zip);;All Files (*)"
        )
        if filename:
            success = FileUtil.save_model(self.lm, filename)
            if success:
                QMessageBox.information(self, "Save Model", f"Model saved successfully to:\n{filename}")
            else:
                QMessageBox.critical(self, "Error", "Failed to save model.")

    # ------------------------------------------------------------
    # BƯỚC 6: LOAD MODEL
    # ------------------------------------------------------------
    def load_model(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Load Trained Model", "model/", "ZIP Files (*.zip);;All Files (*)"
        )
        if filename:
            model = FileUtil.load_model(filename)
            if model:
                self.lm = model
                QMessageBox.information(self, "Load Model", f"Model loaded successfully from:\n{filename}")
            else:
                QMessageBox.critical(self, "Error", "Failed to load model.")

    # ------------------------------------------------------------
    # BƯỚC 7: PREDICT
    # ------------------------------------------------------------
    def predict(self):
        try:
            if self.lm is None:
                QMessageBox.warning(self, "Warning", "Please train or load a model first.")
                return

            vals = [
                float(self.lineEdit_Income.text()),
                float(self.lineEdit_HouseAge.text()),
                float(self.lineEdit_Rooms.text()),
                float(self.lineEdit_Bedrooms.text()),
                float(self.lineEdit_Population.text())
            ]

            result = self.lm.predict([vals])[0]
            self.lineEdit_Pred.setText(f"{result:,.2f}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Prediction failed:\n{e}")
