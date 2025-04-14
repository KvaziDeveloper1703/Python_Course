'''
Программа удаляет дубликаты из списка, при этом сохраняет порядок появления первых вхождений элементов.
'''

def sum_even_numbers(given_array):
    total = 0
    for number in given_array:
        if number % 2 == 0:
            total += number
    return total

numbers = [1, 2, 3, 4, 5, 6]

result = sum_even_numbers(numbers)
print(result)