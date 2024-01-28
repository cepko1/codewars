def sum_strings(x, y):
    minimum = min(len(x),len(y))
    maximum = max(len(x),len(y))
    res = ''
    ten = 0
    for i in range(1,minimum+1):
        suma = int(x[-i]) + int(y[-i]) + ten
        print(x[-i], y[-i])
        res = str(suma % 10) + res
        ten = 1 if suma > 9 else 0
        print(suma, res,ten)
    if minimum == maximum and ten:
        print('aaaa')
        res = '1' + res
    if minimum != maximum:
        additional_str = ''
        for i in range (minimum,maximum):
            suma = int(x[-i-1]) + ten if len(x) > len(y) else int(y[-i-1]) + ten
            additional_str = str((int(x[-i-1]) + ten) % 10) + additional_str if len(x) > len(y) else str((int(y[-i-1]) + ten) % 10 )+ additional_str
            ten = 1 if suma > 9 else 0
            print(suma, additional_str, ten)
        res = additional_str + res
        if ten:
            res = '1' + res
        # res = str(int(x[-minimum - 1]) + next) + res if len(x) > len(y) else str(int(y[-minimum - 1]) + next) + res
        # res = x[0:maximum - minimum - 1] + res if len(x) > len(y) else y[0:maximum - minimum - 1] + res

    return res


print(sum_strings("2999", "302"))