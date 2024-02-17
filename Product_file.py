import re

class Product:

    def __init__(self, name, quantity, price=None):
        global predefinition_list
        self.name = name
        self.quantity = quantity
        self.price = price

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
            digits = re.findall("[^a-z]", product_name, re.IGNORECASE)  # re method

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
