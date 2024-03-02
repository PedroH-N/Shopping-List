import re


class Product:

    def __init__(self, name, quantity, price=None):
        self.name = name
        self.quantity = quantity
        self.price = price

    @classmethod
    def get_product(cls):
        while True:
            product_name = input("Product name: ").strip().capitalize()

            digits = re.findall("[^a-z]", product_name, re.IGNORECASE)

            is_string = cls.is_alphabetical(digits)

            if product_name and is_string:
                break

        return product_name

    @classmethod
    def is_alphabetical(cls, digits):
        is_accepted = False
        if not digits:
            is_accepted = True  # help comment
        else:
            print("Invalid answer, just accept alphabetical letters.\n")
        return is_accepted

    @classmethod
    def get_quantity(cls):
        while True:
            product_quantity = input("Quantity: ").strip()

            # g and k are accepted because equals gram or kilogram
            digits = re.findall("[^0-9kg.,]", product_quantity, re.IGNORECASE)

            is_int = cls.is_integer_or_kg(digits)

            if product_quantity and is_int:
                break

        return product_quantity

    @classmethod
    def is_integer_or_kg(cls, digits):
        is_int = False
        if not digits:
            is_int = True
        else:
            print("Invalid quantity, just accepts numbers and the letters K and G.\n")

        return is_int

    @classmethod
    def get_price_optional(cls):
        while True:

            product_price_yn = input("Do you wan't to put the price? (Y/N) ").strip()

            digit = re.findall("(y|n)", product_price_yn, re.IGNORECASE)
            digit_yes = re.search("y", product_price_yn, re.IGNORECASE)
            digit_no = re.search("n", product_price_yn, re.IGNORECASE)

            cls.is_yes_or_no_error_message(digit, digit_yes, digit_no)

            if digit_no and len(digit) == 1:
                break

            if digit_yes and len(digit) == 1:
                return Product.get_price_normal()

    @classmethod
    def is_yes_or_no_error_message(cls, digit, digit_yes, digit_no):
        if len(digit) > 1:
            print("Invalid answer, type just one character\n")
        if not digit_yes and not digit_no:
            print("Invalid answer, type Y or N (uppercase or lowercase)\n")

    @classmethod
    def get_price_normal(cls):
        while True:
            product_price = input("Price (write just the number): ")

            is_int = False

            digits = re.findall("[^0-9.,]", product_price, re.IGNORECASE)

            if not digits:
                is_int = True
            else:
                print("Invalid price")

            if product_price and is_int:
                return product_price
