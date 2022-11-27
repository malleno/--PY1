import random as rand
import string


def get_random_password() -> str:
    str_chars_digits_ = string.digits + string.ascii_uppercase + string.ascii_lowercase
    return "".join(rand.sample(str_chars_digits_, 8))


print(get_random_password())
