a = "AAA"
b = "BB"
m = len(a)
n = len(b)


def LSA(a, b, m, n):
    if m == 0 or n == 0:
        return 0
    elif a[m - 1] == b[n - 1]:
        result = 1 + LSA(a, b, m - 1, n - 1)
    elif a[m - 1] != b[n - 1]:
        temp1 = LSA(a, b, m - 1, n)
        temp2 = LSA(a, b, m, n - 1)
        result = max(temp1, temp2)
    return result


if __name__ == '__main__':
    print(LSA(a, b, m, n))
