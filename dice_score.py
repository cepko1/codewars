def score(dice):
    numbers = {}
    for i in range(10):
        numbers[i] = 0
    for n in dice:
        numbers[n] += 1
    result = 0
    threes = {1 : 1000, 6 : 600, 5 : 500, 4: 400, 3 : 300, 2 : 200}
    for k in threes.keys():
        if numbers[k] >= 3:
            result += threes[k]
            numbers[k] -=3
    result += 100 * numbers[1]
    result += 50 * numbers[5]
    return result

print(score( [2, 4, 4, 5, 4] ))