import random
import string


def generate_char(char_set: str) -> str:

    c = char_set[random.randint(0, len(char_set) - 1)]
    return c


def generate_char_set(grade: int) -> str:

    char_set = string.ascii_lowercase

    if grade > 0:
        char_set = char_set + string.ascii_uppercase

    if grade > 1:
        char_set = char_set + string.digits

    if grade > 2:
        char_set = char_set + string.punctuation

    return char_set
