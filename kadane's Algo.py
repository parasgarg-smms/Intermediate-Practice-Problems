a = [1, 2, -1, 2, 1, -1, 1]


def find_max_subarray():
    max_global = a[0]
    max_current = a[0]
    for i in range(1, len(a)):
        max_current = max(max_current + a[i], a[i])
        if max_global < max_current:
            max_global = max_current
    return max_global


if __name__ == '__main__':
    print(find_max_subarray())
