from PIL.ImImagePlugin import number
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem

from MainWindowListProduct import Ui_MainWindow


class MainWindowListProductEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def showWindow(self):
        self.MainWindow.show()
    def load_products(self,lp):
        self.tableWidget.setRowCount(0)
        for i in range(0,len(lp.products)):
            p=lp.products[i]
            number_row=self.tableWidget.rowCount()
            self.tableWidget.insertRow(number_row)
            self.tableWidget.setItem(number_row,0,QTableWidgetItem(p.id))
            self.tableWidget.setItem(number_row, 1, QTableWidgetItem(p.name))
            self.tableWidget.setItem(number_row, 2, QTableWidgetItem(p.quantity))
            self.tableWidget.setItem(number_row, 3, QTableWidgetItem(p.price))