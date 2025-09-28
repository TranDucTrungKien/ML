from PyQt6.QtWidgets import QApplication, QMainWindow
from review.MainWindowListProductEx import MainWindowListProductEx
from review.product import Product
from review.products import ListProduct

app=QApplication([])
qmain=QMainWindow()
my_window=MainWindowListProductEx()
my_window.setupUi(qmain)

lp=ListProduct()
lp.add_products(Product("p1","coca",15,35))
lp.add_products(Product("p2","pepsi",14,25))
lp.add_products(Product("p3","sting",20,32))
lp.print_products()
my_window.load_products(lp)
my_window.showWindow()
app.exec()