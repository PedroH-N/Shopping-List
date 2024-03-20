import re
from Product import Product


class User_input_prompter:

    @staticmethod
    def menu_question_change_list():
        while True:
            print(
                "Choose one of the options to change the predefinition list:\n"
                "[1] Add an item\n[2] Remove an item\n[3] Clear the list\n[4] Go back"
            )

            match answer2 := input():
                case "1":
                    return int(answer2)
                case "2":
                    return int(answer2)
                case "3":
                    return int(answer2)
                case "4":
                    return int(answer2)
                case _:
                    print(
                        "Invalid answer, please reanswer typing just one of the numbers."
                    )

    @staticmethod
    def menu_questions_main():
        while True:
            print(
                15 * "-",
                "SHOPPING LIST",
                15 * "-",
                "\n"
                "This is a program that stores and manages a shopping list. The predefinition list is\n"
                "a list that is stored in memory that stays the same even when you turn off the program.\n"
                "Choose one of the options:\n[1] See your predefinition list\n[2] Change your predefinition list\n[3] Start check mode (not available yet)\n[4] Exit",
            )

            match answer := input():
                case "1" | "3" | "4":
                    return dict({"question_number": 1, "answer": int(answer)})
                case "2":
                    return dict({"question_number": 0, "answer": "other_function"})
                case _:
                    print(
                        "Invalid answer, please reanswer typing just one of the numbers."
                    )

    @staticmethod
    def write_over_choice_function(name, quantity, price=None):
        while True:
            write_over_choice = input(
                "What do you want to update the product?\n[1] Just the name\n[2] Just the quantity\n[3] Just the price\n[4] Everything\n[5] Nothing\n"
            )

            is_ok = User_input_prompter.write_over_choice_input_verification(
                write_over_choice
            )

            if is_ok:
                break

        if int(write_over_choice) != 5:
            match int(write_over_choice):
                case 1:
                    name = Product.get_product()
                case 2:
                    quantity = Product.get_quantity()
                case 3:
                    price = Product.get_price_normal()
                case 4:
                    name = Product.get_product()
                    quantity = Product.get_quantity()
                    price = Product.get_price_normal()
                case 5:
                    return {
                        "name": name,
                        "quantity": quantity,
                        "price": price,
                        "exit": 1,
                    }

        question_continue = input(
            "Do you want to change something more about the item? (Y/N)"
        )

        digit, digit_yes, digit_no = Product.yes_or_no_checkings(question_continue)

        if digit_no and len(digit) == 1:
            return {"name": name, "quantity": quantity, "price": price, "exit": 1}

        if digit_yes and len(digit) == 1:
            return {"name": name, "quantity": quantity, "price": price, "exit": 0}

    @staticmethod
    def product_in_list_check(name, predefinition: object):
        for product in predefinition.predefinition_list:
            if product["name"] == name:

                return_value_write_over = None
                flag_first_time = True

                while True:
                    User_input_prompter.product_in_list_check_question_interface(
                        product,
                        flag_first_time,
                        return_value_write_over,
                    )

                    if not flag_first_time:
                        product["name"] = return_value_write_over["name"]
                        product["price"] = return_value_write_over["price"]
                        product["quantity"] = return_value_write_over["quantity"]

                    flag_first_time = False

                    return_value_write_over = (
                        User_input_prompter.write_over_choice_function(
                            product["name"], product["quantity"], product["price"]
                        )
                    )

                    if (
                        isinstance(return_value_write_over, dict)
                        and return_value_write_over["exit"] == 1
                    ):
                        return [
                            return_value_write_over["name"],
                            return_value_write_over["quantity"],
                            return_value_write_over["price"],
                        ]

        return None

    # ----

    @staticmethod
    def write_over_choice_input_verification(write_over_choice):
        digits = re.findall("[^12345]", write_over_choice, re.IGNORECASE)
        if digits:
            print("\nInvalid answer, it's just accepted number from 1 to 5.\n")
        if not digits:
            return True

    @staticmethod
    def product_in_list_check_question_interface(
        product: dict, flag_first_time: bool, return_value_write_over: object
    ):
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
