def count_change(money, coins):
    combination = {}
    summa = 0
    flag = False
    for i in range(money):
        combination[i+1] = 0
    for coin in coins:
        combination[coin] = 1
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
                    combination[key + coin] = combination[key + coin] + 1 if combination[key + coin] else current
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


            # if key + coin in combination.keys():
            #     combination[key + coin] += 1
            # else:
            #     combination[key + coin] = 1

                # if key + coin in combination.keys():
                #     print('kkk')
                #     combination[key + coin] +=1
                # else:
                #     print('ttt')
                #     combination[key + coin] = 1

        #          # print('Key exist')
        #         if summa - coin in combination.keys():
        #             print('1111')
        #             combination[coin + summa] = 1 + combination[summa - coin]
        #         else:
        #             print('2222',summa)
        #             combination[coin + summa] += 1
        #     else:
        #          # print('New key')
        #         if summa - coin in combination.keys():
        #             print('3333')
        #             combination[coin + summa] = 1 + combination[summa - coin]
        #         else:
        #             print('4444')
        #             combination[coin + summa] = 1
        #     print(coin,combination)
        # summa +=1
    # for i in range(len(coins)`):
    #     count = 0
    #     print(i, coins[i], money)
    #     if money - coins[i] > 0:
    #         print('Recurs', coins[i:], money - coins[i])
    #         return 0 + count_change(money - coins[i], coins[i:])
    #     elif money - coins[i] == 0:
    #         print('Bingo')
    #         count += 1
    #     elif money - coins[i] < 0:
    #         print('Fail')
    #         continue
    #
    #     else:
    #         print('achtung')
    #         continue
    # return count



print(count_change(4, [1,2]))

print(count_change(10, [5,2,3]))

print(count_change(11, [5,7]))