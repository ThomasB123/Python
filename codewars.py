def minimum_number(numbers):
    sum = 0
    for x in numbers:
        sum += x
        print('hi')
    print(sum)
    test = 0
    prime = False
    while not prime:
        print('test')
        prime = True
        for x in range(1,test+sum-1):
            if (test+sum) % x == 0:
                prime = False
        if prime:
            return test
        test += 1
    return test

print(minimum_number([3,1,2]))
