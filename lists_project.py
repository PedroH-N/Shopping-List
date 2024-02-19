from Product_file import Product
from Predefinition_file import Predefinition
import re

# shopping list
# store the predef list in a txt

predefinition = Predefinition()


def write_over_choice_function(name, quantity, price=None):
    while True:
        write_over_choice = input(
            "What do you want to update the product?\n[1] Just the name\n[2] Just the quantity\n[3] Just the price\n[4] Everything\n[5] Nothing\n"
        )

        digits = re.findall(
            "[^12345]", write_over_choice, re.IGNORECASE)

        if digits:
            print(
                "\nInvalid answer, it's just accepted number from 1 to 5.\n")

        if not digits and int(write_over_choice) == 5:
            return {"name": name, "quantity": quantity, "price": price, "exit": 1}

        if not digits:
            break

    if not digits and int(write_over_choice) != 5:
        write_over_choice = int(write_over_choice)

        if write_over_choice == 1:
            name = Product.get_product()

        elif write_over_choice == 2:
            quantity = Product.get_quantity()

        elif write_over_choice == 3:
            price = Product.get_price_normal()

        elif write_over_choice == 4:
            name = Product.get_product()
            quantity = Product.get_quantity()
            price = Product.get_price_normal()

    question_continue = input(
        "Do you want to change something more about the item? (Y/N)")

    digit = re.findall(
        "(y|n)", question_continue, re.IGNORECASE)

    digit_yes = re.search(
        "y", question_continue, re.IGNORECASE)

    digit_no = re.search(
        "n", question_continue, re.IGNORECASE)

    if len(digit) > 1:
        print("Invalid answer, type just one character\n")

    if not digit_yes and not digit_no:
        print(
            "Invalid answer, type Y or N (uppercase or lowercase)\n")

    if digit_no and len(digit) == 1:
        # break
        return {"name": name, "quantity": quantity, "price": price, "exit": 1}

    if digit_yes and len(digit) == 1:
        return {"name": name, "quantity": quantity, "price": price, "exit": 0}


def product_in_list_check(name):
    for product in predefinition.predefinition_list:
        if product["name"] == name:
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
                        f"Name: {return_value_write_over['name']}\nQuantity: {return_value_write_over['quantity']}\n"
                        f"Price: {return_value_write_over['price']}\n"
                    )
                    product['name'] = return_value_write_over['name']
                    product["price"] = return_value_write_over["price"]
                    product["quantity"] = return_value_write_over["quantity"]

                flag_first_time = False

                return_value_write_over = write_over_choice_function(
                    product["name"], product["quantity"], product["price"])

                # the function just return a dict when you answer no to the question "do you want to change anything more?"
                if isinstance(return_value_write_over, dict):
                    if return_value_write_over["exit"] == 1:
                        return [return_value_write_over["name"], return_value_write_over["quantity"], return_value_write_over["price"]]

    return None  # if the name isn't in the predefinition


def main():
    global predefinition

    product_inst = Product(Product.get_product(), Product.get_quantity(),
                           Product.get_price_optional())
    new_values_return = product_in_list_check(product_inst.name)

    if isinstance(new_values_return, list):
        product_inst.name = new_values_return[0]
        product_inst.quantity = new_values_return[1]
        product_inst.price = new_values_return[2]

    predefinition.fill("predefinition.txt")
    predefinition.show()
    predefinition.add(product_inst.name, product_inst.quantity, product_inst.price)
    predefinition.show()


if __name__ == "__main__":
    main()
