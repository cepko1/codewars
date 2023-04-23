def queue_time(customers, n):
    threads = {}
    for i in range(n):
        threads[i+1] = 0
    for customer in customers:
        min = 1
        for number, count in threads.items():
            if count < threads[min]:
                min = number
        threads[min] += customer
    max = 1
    for number, count in threads.items():
        if count > threads[max]:
            max = number
    return threads[max]

print(queue_time([1,2,3,4,5], 1))