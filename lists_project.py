
# shopping list
# store the predef list in a txt

import re

predefinition_list = [
    {"name": "Banana", "quantity": "12", "price": "15"}
]

# class Predefinition:

# open_predef()

# show_predef()

# add_predef()

# remove_predef()

# clear_predef()

# start_checkmode()

# check_item()

# uncheck_item()


class Product:

    def __init__(self, name, quantity, price=None):
        global predefinition_list
        self.name = name
        self.quantity = quantity
        if price:
            self.price = price

        for product in predefinition_list:
            if product["name"] == self.name:
                flag_first_time = True
                while True:
                    if flag_first_time:
                        print(
                            "\nThe item is already in the predefinition as:\n"
                            f"Name: {product['name']}\nQuantity: {product['quantity']}\n"
                            f"Price: {product['price']}\n"
                        )

                    if not flag_first_time:
                        print(
                            "\nThe item is now set as:\n"
                            f"Name: {product['name']}\nQuantity: {product['quantity']}\n"
                            f"Price: {product['price']}\n"
                        )

                    # link instance variables among with the predefinitions
                    self.name = product["name"]
                    self.quantity = product["quantity"]
                    self.price = product["price"]

                    flag_first_time = False
                    write_over_choice = input(
                        "What do you want to update the product?\n[1] Just the name\n[2] Just the quantity\n[3] Just the price\n[4] Everything\n[5] Nothing\n"
                    )

                    digits = re.findall(
                        "[^12345]", write_over_choice, re.IGNORECASE)

                    if digits:
                        print(
                            "Invalid answer, it's just accepted number from 1 to 5.")

                    if not digits and int(write_over_choice) == 5:
                        break

                    if not digits and int(write_over_choice) != 5:
                        write_over_choice = int(write_over_choice)
                        if write_over_choice == 1:
                
                            product["name"] = Product.get_product()
                        elif write_over_choice == 2:
                            print(product["quantity"])
                            
                            product["quantity"] = Product.get_quantity()
                            print(product["quantity"])
                        elif write_over_choice == 3:
                            print(product["price"])
                            
                            product["price"] = Product.get_price_normal()
                            print(product["price"])
                        elif write_over_choice == 4:
                            product["name"] = Product.get_product()
                            product["quantity"] = Product.get_quantity()
                            product["price"] = Product.get_price_normal()

                        question_continue = input(
                            "Do you want to change something more about the item? (Y/N)")
                        digit = re.findall(
                            "(y|n)", question_continue, re.IGNORECASE)
                        digit_yes = re.search(
                            "y", question_continue, re.IGNORECASE)
                        digit_no = re.search(
                            "n", question_continue, re.IGNORECASE)

                        # link instance variables among with the predefinitions
                        self.name = product["name"]
                        self.quantity = product["quantity"]
                        self.price = product["price"]

                        if len(digit) > 1:
                            print("Invalid answer, type just one character\n")
                        if not digit_yes and not digit_no:
                            print(
                                "Invalid answer, type Y or N (uppercase or lowercase)\n")

                        if digit_no and len(digit) == 1:
                            break

    @classmethod
    def get_product(cls):
        while True:
            product_name = input("Product name: ").strip().capitalize()
            is_string = False

            '''
            try:
                float(product_name)
            except ValueError:
                is_string = True

            try:
                int(product_name)
            except ValueError:
                is_string = True
                
            the int verification is working, but the float one isn't
            so i change to the re.findall() because I didn't understand why it's not working
            '''
            digits = re.findall("[0-9]", product_name)  # re method

            if not digits:
                is_string = True  # help comment
            else:
                print("Invalid name, just accept alphabetical letters.\n")

            if product_name and is_string:
                break

        return product_name

    @classmethod
    def get_quantity(cls):
        while True:
            product_quantity = input("Quantity: ").strip()
            is_int = False

            # g and k are accepted because equals gram or kilogram
            digits = re.findall("[^0-9kg]", product_quantity, re.IGNORECASE)

            if not digits:
                is_int = True
            else:
                print(
                    "Invalid quantity, just accepts numbers and the letters K and G.\n")

            if product_quantity and is_int:
                break

        return product_quantity

    @classmethod
    def get_price_optional(cls):
        while True:
            can_exit = False

            product_price_yn = input(
                "Do you wan't to put the price? (Y/N) ").strip()

            digit = re.findall("(y|n)", product_price_yn, re.IGNORECASE)
            digit_yes = re.search("y", product_price_yn, re.IGNORECASE)
            digit_no = re.search("n", product_price_yn, re.IGNORECASE)

            if len(digit) > 1:
                print("Invalid answer, type just one character\n")
            if not digit_yes and not digit_no:
                print("Invalid answer, type Y or N (uppercase or lowercase)\n")

            if digit_no and len(digit) == 1:
                break

            if digit_yes and len(digit) == 1:

                return Product.get_price_normal()

    @classmethod
    def get_price_normal(cls):
        while True:
            product_price = input("Price (write just the number): ")

            is_int = False

            digits = re.findall("[^0-9]", product_price, re.IGNORECASE)

            if not digits:
                is_int = True
            else:
                print("Invalid price")

            if product_price and is_int:
                return product_price


def main():
    Product(Product.get_product(), Product.get_quantity(),
            Product.get_price_optional())


if __name__ == "__main__":
    main()
