first_class = []
second_class = []
# Вариант 1. Как наполнить список
# for i in range(160,178,2):
#     first_class.append(i)
# Вариант 2. Как наполнить список
first_class = list(range(160, 178, 2))
second_class = list(range(162, 183, 3))

print(first_class)
print(second_class)

first_class.extend(second_class)
# first_class.sort()
for _ in range(len(first_class) - 1):
	for sort in range(len(first_class) - 1):
		if first_class[sort] > first_class[sort + 1]:
			first_class[sort], first_class[sort + 1] = first_class[sort + 1], first_class[sort]

print('Итоговый отфоритрованный список список:\n', first_class)


#
# first_class.extend(second_class)
# for _ in range(len(first_class) - 1):
#     for sort in range(len(first_class) - 1):
#         if first_class[sort] > first_class[sort + 1]:
#             first_class[sort], first_class[sort + 1] = first_class[sort + 1], first_class[sort]
# print('Все ученики по росту: ', first_class)
