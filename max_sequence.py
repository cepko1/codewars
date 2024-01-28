def max_sequence(arr):
    """ Return sum of max positive sequence"""
    summa = 0
    if not arr:
        return summa
    maximum = 0
    for i in arr:
        if not maximum and i < 0:
            continue
        else:
            maximum += i
        if maximum < 0:
            maximum = 0
        summa = max(maximum, summa)
    return summa



print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))