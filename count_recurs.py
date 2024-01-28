"""https://www.codewars.com/kata/541af676b589989aed0009e7/train/python"""

def count_change(money, coins):
    if money < 0:  #If money-coin less than 0 - than that combination is wrong
        print('less 0')
        return 0
    elif money == 0:   #If money-coin equal 0 than combination is correct
        print(f'equal ')
        return 1
    else:

        print(money,coins)
        return sum((count_change(money - i, coins[coins.index(i):]) for i in coins))





print(count_change(4, [1, 2]))
print()
print(count_change(10, [5, 2, 3]))
print()
print(count_change(11, [5, 7]))