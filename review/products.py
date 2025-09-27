class ListProduct:
    def __init__(self):
        self.products=[]
    def add_products(self,p):
        self.products.append(p)
    def print_products(self):
        for p in self.products:
            print(p)
    def arrange_products(self):
        disc=self.products.sort()