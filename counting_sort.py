a = [1, 0, 1, 1, 0, 2, 3, 1, 2, 3]
b = [0, ] * len(a)
for i in a:
    b[i] += 1

for i in range(1, len(b)):
    b[i] = b[i] + b[i - 1]

for i in range(len(b) - 1, 0, -1):
    b[i] = b[i - 1]
b[0] = 0
c = [0, ] * len(a)

for i in a:
    c[b[i]] = i
    b[i] += 1

for i in c:
    print(i)
