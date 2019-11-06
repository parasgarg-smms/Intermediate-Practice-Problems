'''
There are 2 types of chocolates in Chocoland denoted by A and B.

The cholates are lined up in a queue.You want to satisfy your friends by distributing some number of non-empty contiguous chocolates such that the ratio of number of type A chocolates to number of type B chocolates is same for all the friends.You have to distribute all the chocolates and satisfy maximum number of friends.
Therefore you have to find the maximum number of friends that can be satisfied.

Input Format

The first line of input contains the number of test cases T .
Each test case starts with one line containing an integer N which is the length of the description of a queue.

Each of the following N lines consists of an integer K and one of the characters A or B, meaning that K characters of the given type (A or B) follow next in the queue.

Output Format

For each test case, output a single line containing the maximum number of friends that can be satisfied.

For 1st Test Case:
Queue is ABBBAA
Distributions are AB, BBAA (Ratio 1:1)
For 2nd Test Case:
Queue is BBBBB
Distributions are B, B, B, B, B (Ratio 0:1)
'''


def abc(a, ratio):
    global RESULT
    for i in range(0, len(a)):
        if i == len(a) - 1:
            return 1
        str1 = a[0:i]
        str2 = a[i:]
        temp1 = str1.count('A')
        temp2 = str1.count('B')
        if temp1 == 0 or temp2 == 0:
            continue
        if temp1 / temp2 == ratio:
            RESULT = RESULT + 1
            return abc(str2, ratio)


a = "AABBBABA"
RESULT = 0

c = 0
if a.count('A') == 0:
    print(a.count('B'))
elif a.count('B') == 0:
    print(a.count('A'))
else:
    for i in range(0, len(a)):
        if i == len(a) - 1:
            print(1)
            exit()
        str1 = a[0:i]
        str2 = a[i:]
        temp1 = str1.count('A')
        temp2 = str1.count('B')
        temp3 = str2.count('A')
        temp4 = str2.count('B')
        if temp1 == 0 or temp2 == 0 or temp3 == 0 or temp4 == 0:
            continue
        if temp1 / temp2 == temp3 / temp4:
            ratio = temp1 / temp2
            RESULT = RESULT + 1
            c = abc(str2, ratio)
            print(RESULT + c)
            exit()
