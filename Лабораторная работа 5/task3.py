import random as rand


def get_unique_list_numbers() -> list[int]:
    unique_list_ = list()
    while len(unique_list_) != 15:
        val = rand.randrange(-10, 11)
        if val not in unique_list_:
            unique_list_.append(val)
    return unique_list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
