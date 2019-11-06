'''
print the count of the negative numbers in a 2D Matrix where all the elements in a row are in ascending sort
'''
def count_values(arr):
    result = 0
    for i in arr:
        for element in i:
            if element < 0:
                result += 1
            else:
                break
    return result


if __name__ == '__main__':
    arr = [
        [-3, -2, -1, 0],
        [-3, 0, 1, 2],
        [0, 1, 4, 6],
        [-2, 0, 1, 2],
        [-3, -1, 0, 2]
    ]
    result = count_values(arr)
    print(result)