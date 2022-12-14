def delete(list_, index=None):
    if index is None:
        return list_[:-1]

    if index < 0:
        index = len(list_) + index
    return list_[:index] + list_[index + 1:]
    ...  # TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
