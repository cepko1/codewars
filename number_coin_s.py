def count_change(money, coins):
    combination = {}
    summa = 0
    flag = False
    for i in range(money):
        combination[i+1] = list()
    for coin in coins:
        combination[coin].append(coin)
    print(combination)
    while not flag:
        # for coin in coins:
        for key in combination.keys():
            current = combination[key]
            print(f'key = {key}')
            flag = 1
            for coin in coins:
                print(f'coin = {coin}')
                if key + coin > money:
                    flag *= 1
                else:
                    flag *= 0
                if key + coin in combination.keys() and current:
                    print(f'key{key} + coin{coin},    current = {current}')
                    if combination[key + coin]:
                        combination[key + coin].append(combination[key].append(coin))
                    else:
                        combination[key + coin].append(current)
                    # combination[key + coin] += 1
                else:
                    print('scip')
                    continue
            # print(f'flag = {flag}')
            print(combination)
    if money in combination.keys():
        return combination[money]
    else:
        return 0



print(count_change(4, [1,2]))

print(count_change(10, [5,2,3]))

print(count_change(11, [5,7]))