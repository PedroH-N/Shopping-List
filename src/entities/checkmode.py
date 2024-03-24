from src.entities.predefinition import Predefinition


class CheckMode(Predefinition):

    @classmethod
    def start_checkmode(cls, list_object: object):
        cls.main_initial_message()

        while True:

            cls.print_check_list(list_object)

            is_goto_uncheck = cls.check_item(list_object)

            if is_goto_uncheck:
                cls.uncheck_item(list_object)

            if cls.stop_checkmode(list_object):
                break

    # ------

    # main

    @classmethod
    def stop_checkmode(cls, list_object: object):
        if len(list_object.predefinition_list) == len(list_object.checked_items):
            cls.print_check_list(list_object)
            list_object.checked_items.clear()
            return True

    @staticmethod
    def main_initial_message():
        print(
            15 * "-",
            "CHECKMODE",
            15 * "-",
            "\n",
            "In this mode you can check the square brackets so that you stay\norganized in your shopping"
            "\nYou can exit this mode by checking all the items",
        )
        print(30 * "-", "\n")

    @staticmethod
    def print_check_list(list_object: object):
        print()
        for item in list_object.predefinition_list:
            is_checked = False
            for checked in list_object.checked_items:
                if item["name"] == checked["name"]:
                    is_checked = True
                    print(f"[X] {item['name']}, Quantity: {item['quantity']}")
            if is_checked == False:
                print(f"[ ] {item['name']}, Quantity: {item['quantity']}")

    # uncheck

    @classmethod
    def uncheck_item(cls, list_object: object):
        while True:

            uncheck = cls.uncheck_initial_message()

            is_unchecked = cls.item_uncheck_verification(list_object, uncheck)

            if is_unchecked:
                break

            if not is_unchecked and uncheck != "":
                cls.not_found_not_checked_error_message()

            else:
                break

    @classmethod
    def item_uncheck_verification(cls, list_object, uncheck):
        is_unchecked = bool()
        for item in list_object.checked_items:
            if item["name"] == uncheck:
                is_unchecked = True
                list_object.checked_items.remove(item)
        return is_unchecked

    @staticmethod
    def uncheck_initial_message():
        uncheck = (
            input(
                "\n(Don't write anything if you want to skip)\n"
                "Write the item's name you want to uncheck: "
            )
            .strip()
            .capitalize()
        )

        return uncheck

    @staticmethod
    def not_found_not_checked_error_message():
        print("\n***Item not checked or not found in the list.***\n")

    # check

    @classmethod
    def check_item(cls, list_object: object) -> bool:
        while True:
            item_to_check = cls.check_item_initial_message()

            to_uncheck = cls.item_to_check_add_to_checked(list_object, item_to_check)

            match to_uncheck:
                case False:
                    cls.not_found_error_message()
                case "uncheck":
                    return True
                case True:
                    return False

    @staticmethod
    def check_item_initial_message():
        item_to_check = input(
            "\n(Don't write anything if you want to uncheck some item)\n"
            "Write the item's name you want to check: "
        ).capitalize()

        return item_to_check

    @classmethod
    def item_to_check_verification(cls, list_object: object, item_to_check: str):
        is_to_check = bool()
        if item_to_check:
            for item in list_object.predefinition_list:
                if item["name"] == item_to_check:
                    is_to_check = True
        return is_to_check

    @staticmethod
    def not_found_error_message():
        print("\n***Item not found in the list.***\n")

    @classmethod
    def item_to_check_add_to_checked(cls, list_object: object, item: str):

        if ok := cls.item_to_check_verification(list_object, item) and item:
            list_object.checked_items.append({"name": item})
            return True
        if not ok and item != "":
            return False
        if not ok and item == "":
            return "uncheck"
