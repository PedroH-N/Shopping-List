from Predefinition import Predefinition

def product_in_list_check( name): #need to cleancode this method
        for product in Predefinition.predefinition_list:
            if product["name"] == name:
                flag_first_time = True
                while True:
                    if flag_first_time:
                        print(
                            "\nThe item is already in the predefinition as:\n"
                            f"Name: {product['name']}\nQuantity: {
                                product['quantity']}\n"
                            f"Price: {product['price']}\n"
                        )

                    if not flag_first_time:
                        print(
                            "\nThe item is now set as:\n"
                            f"Name: {return_value_write_over['name']}\nQuantity: {
                                return_value_write_over['quantity']}\n"
                            f"Price: {return_value_write_over['price']}\n"
                        )
                        product['name'] = return_value_write_over['name']
                        product["price"] = return_value_write_over["price"]
                        product["quantity"] = return_value_write_over["quantity"]

                    flag_first_time = False

                    return_value_write_over = Interface.write_over_choice_function(
                        product["name"], product["quantity"], product["price"])

                    # the function just return a dict when you answer no to the question "do you want to change anything more?"
                    if isinstance(return_value_write_over, dict):
                        if return_value_write_over["exit"] == 1:
                            return [return_value_write_over["name"], return_value_write_over["quantity"], return_value_write_over["price"]]
