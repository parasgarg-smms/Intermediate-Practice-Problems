'''
Prints the all subsets of length 2(zip function)
'''

a = [1, 2, 3, 4, 5, 6]
b = a
counter = 0
i = 0
while (i < len(a)):  # 0<5
    print("{} {}".format(b[counter], a[i]))
    i += 1
    if i == len(a):
        i = 0
        counter += 1
    if counter == 6:
        exit()
