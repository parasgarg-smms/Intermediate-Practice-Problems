a = "AAA"
b = "BBA"
m = len(a)
n = len(b)


def LSA(a, b, m, n):
    result = 0
    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                result += 1
                break
    return result


if __name__ == '__main__':
    print(LSA(a, b, m, n))
