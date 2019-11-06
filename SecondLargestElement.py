'''
Find the second largest from an array
input:
2 3 5 6 7 -1 -8 8
'''
if __name__ == '__main__':
    arr = list(map(int, input().split()))
    max_marks = arr[0]
    runner_up = float("-Inf")
    for i in arr:
        if i > max_marks:
            runner_up = max_marks
            max_marks = i
        elif i > runner_up and i != max_marks:
            runner_up = i
    print(runner_up,)
