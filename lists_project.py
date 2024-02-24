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


def product_in_list_check_assignments(instance: object):
    new_values_return = product_in_list_check(instance.name)

    if isinstance(new_values_return, list):
        instance.name = new_values_return[0]
        instance.quantity = new_values_return[1]
        instance.price = new_values_return[2]
        # remove from list the old item, so that it don't duplicate


def menu_question_change_list():
    while True:
        print(
            "Choose one of the options to change the predefinition list:\n"
            "[1] Add an item\n[2] Remove an item\n[3] Clear the list\n[4] Go back"
        )
        answer2 = input()
        
        if answer2 == "1":
            return int(answer2)
        elif answer2 == "2":
            return int(answer2)
        elif answer2 == "3":
            return int(answer2)
        elif answer2 == "4":
            return int(answer2)
        else:
            print("Invalid answer, please reanswer typing just one of the numbers.")


def menu_questions_main():
    while True:
        print(
            15 * "-", "SHOPPING LIST", 15 * "-", "\n"
            "This is a program that stores and manages a shopping list. The predefinition list is\n"
            "a list that is stored in memory that stays the same even when you turn off the program.\n"
            "Choose one of the options:\n[1] See your predefinition list\n[2] Change your predefinition list\n[3] Start check mode (not available yet)\n[4] Exit"
        )

        answer = input()

        if answer == "1" or answer == "3" or answer == "4":
            return dict({"question_number": 1, "answer": int(answer)})

        if answer == "2":
            return dict({"question_number": 0, "answer": "other_function"})
        
        if answer == "3":
            return dict({"question_number": 1, "answer": int(answer)})

        if answer:
            print("Invalid answer, please reanswer typing just one of the numbers.")


def main():
    global predefinition
    predefinition.fill("predefinition.txt")

    while True:
        answer_menu_1 = menu_questions_main()

        if answer_menu_1["question_number"] == 1:
            if answer_menu_1["answer"] == 1:
                predefinition.show()
            elif answer_menu_1["answer"] == 4:
                break
            if answer_menu_1["answer"] == 3:
                predefinition.start_checkmode()

        elif answer_menu_1["question_number"] == 0 and answer_menu_1["answer"] == "other_function":
            while True:
                answer_change_list = menu_question_change_list()
                if answer_change_list == 1:
                    product_inst = Product(Product.get_product(), Product.get_quantity(),
                                        Product.get_price_optional())
                    predefinition.add(product_inst.name,
                                    product_inst.quantity, product_inst.price)
                elif answer_change_list == 2:
                    predefinition.remove(Product.get_product())
                elif answer_change_list == 3:
                    predefinition.clear()
                elif answer_change_list == 4:
                    break


if __name__ == "__main__":
    main()
    predefinition.write_txt()
