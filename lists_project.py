
# shopping list
# store the predef list in a txt

import re

# class Predefinition:
# show_predef()

# add_predef()

# remove_predef()

# clear_predef()

# start_checkmode()

# check_item()

# uncheck_item()


class Product:

    # __init__():
    '''
    *add name, quant and price as instance variables
    input("Do you want to add it to predefinition? )
    if: it's already on the predefinition, do you want to write over or don't write?
    '''

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
            digits = re.findall("[a-fh-jl-z]", product_quantity, re.IGNORECASE)

            if not digits:
                is_int = True
            else:
                print("Invalid quantity, just accepts numbers and the letters K and G.\n")

            if product_quantity and is_int:
                break

        return product_quantity

    # get_price_optional()


Product.get_product()
Product.get_quantity()
