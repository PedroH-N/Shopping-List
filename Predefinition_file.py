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
        for item in self.predefinition_list:
            print(
                f"Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}"
            )

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

    # remove_predef()

    # clear_predef()

    # start_checkmode()

    # check_item()

    # uncheck_item()
    ...
