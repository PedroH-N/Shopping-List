import re
import src.helpers.input_helper as Input_Helper


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

            is_string = Input_Helper.is_alphabetical(digits)

            if product_name and is_string:
                break

        return product_name

    @classmethod
    def get_quantity(cls):
        while True:
            product_quantity = input("Quantity: ").strip()

            # g and k are accepted because equals gram or kilogram
            digits = re.findall("[^0-9kg.,]", product_quantity, re.IGNORECASE)

            is_int = Input_Helper.is_weight(digits)

            if product_quantity and is_int:
                break

        return product_quantity

    @classmethod
    def get_price_optional(cls):
        while True:

            product_price_yn = input("Do you wan't to put the price? (Y/N) ").strip()

            digit, digit_yes, digit_no = Input_Helper.yes_or_no_checkings(
                product_price_yn
            )

            if digit_no and len(digit) == 1:
                break

            if digit_yes and len(digit) == 1:
                return Product.get_price_normal()

    @classmethod
    def get_price_normal(cls):
        while True:
            product_price = input("Price (write just the number): ")

            digits = re.findall("[^0-9.,]", product_price, re.IGNORECASE)

            is_int = Input_Helper.is_int(digits)

            if product_price and is_int:
                return product_price
