first_list = []
second_list = []

def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)
    for number in unique_numbers:
        list_of_unique_numbers.append(number)
    return list_of_unique_numbers

for i in range(3):
    print('Введите', i+1, '-е число для первого списка: ', end='')
    i_first_list = int(input())
    first_list.append(i_first_list)

for i in range(7):
    print('Введите', i+1, '-е число для второго списка: ', end='')
    i_second_list = int(input())
    second_list.append(i_second_list)

first_list.extend(second_list)
print('Новый первый список с уникальными элементами: ', get_unique_numbers(first_list))

