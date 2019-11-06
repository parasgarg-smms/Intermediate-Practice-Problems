import timeit

print(timeit.timeit('''COMBO=(4,5,6)
decision=False
for i in range(10):
    if decision==True:
        break
    for j in range(10):
        if decision:
            break
        for k in range(10):
            if (i,j,k) == COMBO:
                decision=True 
                break''', number=10000))
# COMBO=(4,5,6)
# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             if (i,j,k) == COMBO:
#                 print("YEYE")
#                 print(i,j,k)
#                 exit()
#

print(timeit.timeit('''
COMBO=(4,5,6)
def combo():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                yield (i,j,k)
for i in combo():
    if i==COMBO: 
        break''',number=10000))
# COMBO=(4,5,6)
# def combo():
#     for i in range(10):
#         for j in range(10):
#             for k in range(10):
#                 yield (i,j,k)
# for i in combo():
#     if i==COMBO:
#         print(i)
#         break