from Product_file import Product


class Predefinition:

    def __init__(self):
        self.predefinition_list = list()
        self.checked_items = list()

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
                file.write(
                    f"{item['name']};{item['quantity']};{item['price']};\n")

    def start_checkmode(self):
        print(
            15 * "-", "CHECKMODE", 15 * "-", "\n",
            "In this mode you can check the square brackets so that you stay\norganized in your shopping"
            "\nYou can exit this mode by checking all the items"
        )

        def not_found():
            print("\n***Item not found in the list.***\n")

        while True:
            is_checked = False

            for item in self.predefinition_list:
                for checked in self.checked_items:
                    if item['name'] == checked['name']:
                        is_checked = True
                        print(
                            f"[X] {item['name']}, Quantity: {item['quantity']}")
                if is_checked == False:
                    print(f"[ ] {item['name']}, Quantity: {item['quantity']}")

            print(30*"-", "\n")

            is_to_check = False

            # the program is understanding ""/None as a "item not found", not as the trigger to go to uncheck part

            while True:
                item_to_check = input(
                    "(Don't write anything if you want to uncheck some item)\n"
                    "Write the item's name you want to check: "
                ).strip().capitalize()

                for item in self.predefinition_list:
                    if item['name'] == item_to_check:
                        is_to_check = True

                if item_to_check == "" or item_to_check == None:
                    is_to_check = True

                if not is_to_check:
                    not_found()

                if item_to_check and is_to_check:
                    self.checked_items.append({"name": item_to_check})
                    break

            if not item_to_check and not is_to_check:
                while True:
                    is_unchecked = False
                    uncheck = input(
                        "(Don't write anything if you want to skip)\n"
                        "Write the item's name you want to uncheck: "
                    ).strip().capitalize()
                    for item in self.checked_items:
                        if item['name'] == uncheck or uncheck == "":
                            is_unchecked = True
                            self.checked_items.remove(item)
                            break
                    if not is_unchecked:
                        not_found()

            if len(self.predefinition_list) == len(self.checked_items):
                self.checked_items.clear()
                break
