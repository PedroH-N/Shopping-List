from Product_file import Product


class Predefinition:

    def __init__(self):
        self.predefinition_list = list()

    def fill(self, predef_file_name: str):
        with open(predef_file_name, "r") as predef_file:
            for line in predef_file:
                name, quantity, price, space = line.split(";")
                self.predefinition_list.append(
                    {"name": name, "quantity": quantity, "price": price})

    def show(self):
        print("\nThis is your predefinition list:\n")
        if self.predefinition_list:
            for item in self.predefinition_list:
                print(
                    f"Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}"
                )
        else:
            print("There's nothing in your list.")

    def add(self, name: str = None, quantity=None, price=0):

        if name and quantity:
            self.predefinition_list.append(
                {"name": name, "quantity": quantity, "price": price})

        else:
            name = Product.get_product()
            quantity = Product.get_quantity()
            price = Product.get_price_optional()
            self.predefinition_list.append(
                {"name": name, "quantity": quantity, "price": price})

    def remove(self, name: str):
        item_is_in = False
        for item in self.predefinition_list:
            if item["name"] == name:
                self.predefinition_list.remove(item)
                item_is_in = True
        
        if not item_is_in:
            print("Item not found in the predefinition list.")

    def clear(self):
        self.predefinition_list.clear()

    def write_txt(self):
        with open("predefinition.txt", "w") as file:
            for item in self.predefinition_list:
                file.write(f"{item['name']};{item['quantity']};{item['price']};")

    # start_checkmode()

    # check_item()

    # uncheck_item()
