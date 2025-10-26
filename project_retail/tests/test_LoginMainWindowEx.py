import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from PyQt6.QtWidgets import QApplication, QMainWindow
from project_retail.ui.LoginMainWindowEx import LoginMainWindowEx

app=QApplication([])
login_ui=LoginMainWindowEx()
login_ui.setupUi(QMainWindow())
login_ui.showWindow()
app.exec()