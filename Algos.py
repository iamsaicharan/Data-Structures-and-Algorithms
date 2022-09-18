def LinearSearch(numbersList, key):
    i = 0
    for i in range(0, len(numbersList)):
        if numbersList[i] == key:
            return i
    return -1



numbers = [2, 4, 7, 10, 11, 32, 45, 87]
print(LinearSearch(numbers, 10))
