def parse_int(string):
    number = 0
    hundrets = 0
    thousants = 0
    numbers = {'one': 1, 'two': 2, 'three': 3, 'four': '4', 'five': 5, 'six': 6, 'seven': 7,
               'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'twenty': 20,
               'thirty': 30, 'fourty': 40, 'fivety': 50, 'sixty': 60, 'seventy': 70,
               'eighty': 80, 'ninety': 90}
    if string in numbers:
        return numbers[string]
    else:
        for part in string:
            if '-' in part:
                tens = (part.split('-'))
                print(tens)
        pass

    return


print(parse_int('eight'))