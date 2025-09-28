class ListProduct:
    def __init__(self):
        self.products=[]
    def add_products(self,p):
        self.products.append(p)
    def print_products(self):
        for p in self.products:
            print(p)
    def sort_desc_price(self):
        for i in range(0,len(self.products)):
            for j in range(i+1,len(self.products)):
                pi=self.products[i]
                pj=self.products[j]
