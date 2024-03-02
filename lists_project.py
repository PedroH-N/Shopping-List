from Product import Product
from Predefinition import Predefinition
from Interface import Interface
from Checkmode import Checkmode
import re

# shopping list
# store the predef list in a txt

predefinition = Predefinition()


def main():
    global predefinition
    predefinition.fill("predefinition.txt")

    while True:
        answer_menu_1 = Interface.menu_questions_main()

        match answer_menu_1["answer"]:
            case 1:
                predefinition.show()
            case 3:
                predefinition.start_checkmode()
            case 4:
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
    predefinition.write_txt()
