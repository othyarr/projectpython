import json

class Product:
    def __init__(self, product_id, name, brand, price, quantity):
        self.product_id = product_id
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity

    def display_product(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Brand: {self.brand}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}\n")

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print("Product removed successfully.")
                return
        print("Product not found.")

    def update_product_quantity(self, product_id, new_quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.quantity = new_quantity
                print("Quantity updated successfully.")
                return
        print("Product not found.")

    def display_inventory(self):
        if not self.products:
            print("Inventory is empty.")
            return
        print("Current Inventory:")
        for product in self.products:
            product.display_product()

    def save_data(self, filename):
        with open(filename, 'w') as file:
            json.dump([vars(product) for product in self.products], file)

    def load_data(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.products = [Product(**product_data) for product_data in data]

class UserInterface:
    def __init__(self, inventory):
        self.inventory = inventory

    def display_menu(self):
        print("\n===== Inventory Management System Menu =====")
        print("1. View Inventory")
        print("2. Add Product")
        print("3. Remove Product")
        print("4. Update Product Quantity")
        print("5. Save Inventory Data")
        print("6. Load Inventory Data")
        print("7. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.inventory.display_inventory()
            elif choice == '2':
                self.add_product()
            elif choice == '3':
                self.remove_product()
            elif choice == '4':
                self.update_product_quantity()
            elif choice == '5':
                self.save_inventory_data()
            elif choice == '6':
                self.load_inventory_data()
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_product(self):
        product_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        brand = input("Enter Product Brand: ")
        price = float(input("Enter Product Price: "))
        quantity = int(input("Enter Product Quantity: "))
        product = Product(product_id, name, brand, price, quantity)
        self.inventory.add_product(product)
        print("Product added successfully.")

    def remove_product(self):
        product_id = input("Enter Product ID to remove: ")
        self.inventory.remove_product(product_id)

    def update_product_quantity(self):
        product_id = input("Enter Product ID to update quantity: ")
        new_quantity = int(input("Enter new quantity: "))
        self.inventory.update_product_quantity(product_id, new_quantity)

    def save_inventory_data(self):
        filename = input("Enter filename to save inventory data: ")
        self.inventory.save_data(filename)
        print("Inventory data saved successfully.")

    def load_inventory_data(self):
        filename = input("Enter filename to load inventory data: ")
        self.inventory.load_data(filename)
        print("Inventory data loaded successfully.")


# Main program
if __name__ == "__main__":
    inventory_system = Inventory()
    ui = UserInterface(inventory_system)
    ui.run()