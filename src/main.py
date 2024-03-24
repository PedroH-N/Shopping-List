from src.entities.product import Product
from src.entities.predefinition import Predefinition
from src.helpers.user_input_prompter import User_input_prompter
from src.entities.checkmode import CheckMode

predefinition = Predefinition()


def product_in_list_check_assignments(instance: object):
    new_values_return = User_input_prompter.product_in_list_check(
        instance.name, predefinition
    )

    if isinstance(new_values_return, list):
        to_delete_name = instance.name
        instance.name = new_values_return[0]
        instance.quantity = new_values_return[1]
        instance.price = new_values_return[2]
        return to_delete_name


def main():
    global predefinition
    predefinition.fill("predefinition.txt")

    while True:
        answer_menu_1 = User_input_prompter.menu_questions_main()

        match answer_menu_1:
            case {"question_number": 1, "answer": 1}:
                predefinition.show()
            case {"question_number": 0, "answer": "other_function"}:
                chosen_action_from_menu_2()
                predefinition.write_txt()
            case {"question_number": 1, "answer": 3}:
                CheckMode.start_checkmode(predefinition)
            case {"question_number": 1, "answer": 4}:
                break


def chosen_action_from_menu_2():
    while True:
        answer_change_list = User_input_prompter.menu_question_change_list()
        match answer_change_list:
            case 1:
                product_inst = Product(
                    Product.get_product(),
                    Product.get_quantity(),
                    Product.get_price_optional(),
                )
                to_remove_name = product_in_list_check_assignments(product_inst)
                if to_remove_name:
                    predefinition.remove(to_remove_name)
                predefinition.add(
                    product_inst.name, product_inst.quantity, product_inst.price
                )
            case 2:
                predefinition.remove(Product.get_product())
            case 3:
                predefinition.clear()
            case 4:
                break


if __name__ == "__main__":
    main()
