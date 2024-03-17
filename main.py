from Product import Product
from Predefinition import Predefinition
from Interface import Interface
from CheckMode import CheckMode

predefinition = Predefinition()


def product_in_list_check_assignments(instance: object):
    new_values_return = Interface.product_in_list_check(instance.name, predefinition)

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
        answer_menu_1 = Interface.menu_questions_main()

        match answer_menu_1:
            case {"question_number": 1, "answer": 1}:
                predefinition.show()
            case {"question_number": 1, "answer": 3}:
                CheckMode.start_checkmode(predefinition)
            case {"question_number": 1, "answer": 4}:
                break

        if (
            answer_menu_1["question_number"] == 0
            and answer_menu_1["answer"] == "other_function"
        ):
            while True:
                answer_change_list = Interface.menu_question_change_list()
                match answer_change_list:
                    case 1:
                        product_inst = Product(
                            Product.get_product(),
                            Product.get_quantity(),
                            Product.get_price_optional(),
                        )
                        to_remove_name = product_in_list_check_assignments(product_inst)
                        predefinition.remove(to_remove_name)
                        predefinition.add(
                            product_inst.name, product_inst.quantity, product_inst.price
                        )
                    case 2:
                        predefinition.remove(Product.get_product)
                    case 3:
                        predefinition.clear()
                    case 4:
                        break


if __name__ == "__main__":
    main()
    predefinition.write_txt()
