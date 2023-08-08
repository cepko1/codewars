def parse_int(string):

    # def parse_ten(string):
    #     if '-' in string:
    #         tens = (string.split('-'))
    #         number = numbers[tens[0]] + numbers[tens[1]]
    #     return number

    number = 0
    numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
               'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
               'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
               'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}
    if string in numbers:
        return numbers[string]

    elif not ' ' in string:
        if '-' in string:
            tens = (string.split('-'))
        return  numbers[tens[0]] + numbers[tens[1]]
    elif ' ' in string:
        lst_string = string.split()
        temp_n = 0
        for numb in lst_string:
            # print(numb)

            if numb in numbers:
                temp_n += numbers[numb]
            elif numb == 'hundred':
                temp_n *= 100
                # temp_n = 0
            elif numb == 'thousand':
                number += temp_n*1000
                temp_n = 0
            elif numb == 'million':
                number = temp_n * 1000000
                temp_n = 0
            elif '-' in numb:
                tens = (numb.split('-'))
                temp_n += numbers[tens[0]] + numbers[tens[1]]
            # print(temp_n)
        if temp_n:
            number += temp_n
        return number
    else:
        pass


    return number


print(parse_int('twenty-one'))
print(parse_int('two hundred forty-six'))
print(parse_int('one thousand three hundred and thirty-seven'))
print(parse_int('five hundred thousand three hundred'))
print(parse_int('one hundred and one'))