class Product:
    def __init__(self, product_id, product_name, premium_amount):
        self.product_id = product_id
        self.product_name = product_name
        self.premium_amount = premium_amount
        self.status = "Active"

    def suspend_product(self):
        self.status = "Suspended"
        print(f"Product '{self.product_name}' has been suspended.")

    def display_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.product_name}")
        print(f"Premium Amount: {self.premium_amount}")
        print(f"Status: {self.status}")
