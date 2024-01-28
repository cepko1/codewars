def fibonacci(n):
    fib_pp = 0
    fib_p = 1
    numb = 2
    while numb < n + 1:
        fib = fib_pp + fib_p
        fib_pp = fib_p
        fib_p = fib
        numb += 1
    return fib


print(fibonacci(10000))
