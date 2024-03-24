import re


def is_alphabetical(digits):
    is_string = False
    if not digits:
        is_string = True
    else:
        print("Invalid name, just accept alphabetical letters.\n")
    return is_string


def is_weight(digits):
    is_int = False
    if not digits:
        is_int = True
    else:
        print("Invalid quantity, just accepts numbers and the letters K and G.\n")
    return is_int


def yes_or_no_checkings(product_price_yn):
    digit = re.findall("(y|n)", product_price_yn, re.IGNORECASE)
    digit_yes = re.search("y", product_price_yn, re.IGNORECASE)
    digit_no = re.search("n", product_price_yn, re.IGNORECASE)

    if len(digit) > 1:
        print("Invalid answer, type just one character\n")
    if not digit_yes and not digit_no:
        print("Invalid answer, type Y or N (uppercase or lowercase)\n")
    return digit, digit_yes, digit_no


def is_int(digits):
    is_int = False
    if not digits:
        is_int = True
    else:
        print("Invalid price")
    return is_int
