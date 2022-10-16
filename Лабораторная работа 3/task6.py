list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

maxIndex_ = 0

for i in range(1, len(list_numbers)):
    if list_numbers[i] > list_numbers[maxIndex_]:
        maxIndex_ = i

tmp = list_numbers[maxIndex_]
list_numbers[maxIndex_] = list_numbers[-1]
list_numbers[-1] = tmp

print(list_numbers)
