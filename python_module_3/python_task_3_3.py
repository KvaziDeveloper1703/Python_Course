'''
Программа сдвигает все элементы массива вправо на заданное количество позиций, при этом последние элементы переходят в начало, сохраняя общую длину массива.
'''

def rotate_right(given_array, k):
    N = len(given_array)

    if N == 0:
        return given_array

    k = k % N

    rotated = []

    for i in range(N - k, N):
        rotated.append(given_array[i])

    for i in range(N - k):
        rotated.append(given_array[i])

    return rotated

original = [1, 2, 3, 4, 5]
rotated = rotate_right(original, 2)
print(rotated)