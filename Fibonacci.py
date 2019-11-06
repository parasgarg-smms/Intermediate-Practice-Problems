def fib(n):
    sequence = [0] * n
    sequence[0] = sequence[1] = 1
    for i in range(2, n):
        sequence[i] = sequence[i - 1] + sequence[i - 2]
    return sequence[n - 1]


n = int(input("Please Enter the number"))
print(fib(n))
