class Product:
    def input(self):
        self.product_no = int(input("Enter the product number: "))
        self.product_name = input("Enter the name: ")
        self.cost = int(input("Enter the cost: "))
        self.quantity = int(input("Enter the qty: "))

    def calculator(self):
        self.total_amount = self.cost * self.quantity

    def display(self):
        print("Product_no -", self.product_no)
        print("Product_name -", self.product_name)
        print("Cost -", self.cost)
        print("Quantity -", self.quantity)
        print("Total_amount -", self.total_amount)


pk = []
for i in range(5):
    print("Enter the product", i + 1)
    p = Product()
    p.input()
    p.calculator()
    pk.append(p)

high = pk[0]
for p in pk:
    if p.total_amount > high.total_amount:
        high = p

print("\nHighest cost:")
high.display()
