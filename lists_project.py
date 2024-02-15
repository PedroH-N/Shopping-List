
# shopping list
from re import findall


class Product:

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
            digits = findall("[0-9]", product_name)  # re method

            if not digits:
                is_string = True

            if product_name and is_string:
                break

        return product_name


Product.get_product()
# product_name = input("Product name: ").strip().capitalize()
# print(float(product_name))
