def get_count_char(str_):
    chars_to_count_ = dict()
    str_ = str_.lower()

    for char_ in str_:
        if not char_.isalpha():
            continue

        if char_ in chars_to_count_:
            chars_to_count_[char_] += 1
        else:
            chars_to_count_.update({char_: 1})

    return chars_to_count_


def get_count_char_in_p(dict_):
    sum_ = sum(dict_.values())

    ratio_to_percent_ = 100
    for char_ in dict_:
        dict_[char_] = str(round(dict_[char_] / sum_ * ratio_to_percent_, 2)) + "%"

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
