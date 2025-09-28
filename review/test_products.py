from review.products import ListProduct
from review.product import Product

lp=ListProduct()
lp.add_products(Product("p1","coca",15,35))
lp.add_products(Product("p2","pepsi",14,25))
lp.add_products(Product("p3","sting",20,32))
lp.print_products()
lp.sort_desc_price()
print("List:")
lp.print_products()