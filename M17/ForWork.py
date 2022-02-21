
# A = int(input('Левая граница: '))
# B = int(input('Правая граница: '))
# list_cube = [x ** 3 for x in range(A, B+1)]
# list_square = [x ** 2 for x in range(A, B+1)]
# print('Список кубов чисел в диапазоне от ',A, 'до ', B, ': ', list_cube)
# print(list_square)


# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
#
# positive_list = [x for x in original_prices if x > 0]
# print(positive_list)

# detachment1 = [77, 75, 76, 77, 76, 73, 57, 67, 76, 52]
# detachment2 = [53, 51, 31, 60, 49, 37, 31, 60, 37, 47]
#
# detachment3 = ['Погиб' if detachment1[i] + detachment2[i] > 100 else 'Выжил' for i in range(10)]
# print(detachment3)
#
# original_prices = [-12, 3, 5, -2, 1]
# new_prices = original_prices[:]

# for i in range(len(original_prices)):
#     if new_prices[i] < 0:
#         new_prices[i] = 0
#
# new_prices = [i for i in original_prices if i > 0]
#
# print(sum(original_prices))
# print(new_prices)
# print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))

# nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
#
# print(nums[:5])
# print(nums[:-2])
# print(nums[::2])
# print(nums[1::2])
# print(nums[::-1])
# print(nums[::-2])


# text = '345 1 4 9849 -5 -787 -364 543 23 6 75 234 564'
# num_list = text.split()
# num_list = [int(i) for i in num_list]
#
# print(sorted(num_list))
# print(sorted(num_list, reverse=True))

detachment1 = [7, 75, 76, 77, 76, 73, 57, 67, 176, 52]
print(max(detachment1))
print(min(detachment1))
max(detachment1), min(detachment1) == min(detachment1), max(detachment1)
print(detachment1)
