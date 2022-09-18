def LinearSearch(numbersList, key):
    i = 0
    for i in range(0, len(numbersList)):
        if numbersList[i] == key:
            return i
    return -1

def BinarySearch(numbersList, key):
    left = 0
    right = len(numbersList) - 1
    while right>=left:
        mid = (left + right)//2
        if numbersList[mid] < key:
            left = mid + 1
        elif numbersList[mid] > key:
            right = mid - 1
        else:
            return mid
    return -1
        



numbers = [2, 4, 7, 10, 11, 32, 45, 87]
print(LinearSearch(numbers, 45))
print(BinarySearch(numbers, 45))
