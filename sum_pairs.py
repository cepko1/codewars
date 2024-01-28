def is_pair(ints, s):
    check_set = set(ints)
    numbers = []
    for number in check_set:
        if s - number in check_set:
            numbers.append(number)
    return numbers

def sum_pairs(ints, s):
    """ Found first pair in list wich equal number"""
    maximum = len(ints)
    checknumbers = is_pair(ints,s)
    if not checknumbers:
        return None
    maximum = len(ints)
    one = 0
    two = len(ints)
    for number in checknumbers:
        second = s - number
        print(number, second)
        if second in ints[ints.index(number) + 1:]:
            # print(ints[ints.index(number) + 1:])
            print(ints.index(second, ints.index(number) + 1))
            if ints.index(second, ints.index(number) + 1) < maximum:
                maximum = ints.index(second, ints.index(number) + 1)
                one = number
                two = second
                print(one, two)
    l = []
    l.append(one)
    l.append(two)
    return l


print(sum_pairs([10, 5, 2, 8, 11, 4, 3, 7, 5],10))