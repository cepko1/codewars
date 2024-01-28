def increment_string(strng):
    if not strng:
        return '1'
    if not strng[-1].isdigit():
        return strng + '1'
    for i in range(len(strng)):
        if strng[-i - 1].isdigit():
            continue
        else:
            break
    sym = strng[:-i]
    digits = str(int(strng[-i:])+1)
    for i in range(len(strng) - len(sym) - len(digits)):
        digits = '0' + digits
    strng = sym + digits
    return strng

print(increment_string('asd09'))