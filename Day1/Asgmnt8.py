def fib(terms):
    n1 = 0
    n2 = 1
    cnt = 0
    while (cnt < terms):
        print(n1, end=" , ")
        sum = n1 + n2
        n1 = n2
        n2 = sum
        cnt = int(cnt) + 1

fib(20)
