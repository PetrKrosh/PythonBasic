a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
print('Количество цифр 5 равно ', a.count(5))
for _ in a:
	if 5 in a:
		a.remove(5)
	else:
		continue
print('Список после добавления списка b', a)

a.extend(c)
print('Количество цифр 3 равно ', a.count(3))
print('Итоговый список: ', a)


#
# a.extend(b)
# print('Кол-во цифр 5 при первом объединении:', a.count(5))
# for _ in a:
#     if 5 in a:
#         a.remove(5)
#     else:
#         continue
#
# a.extend(c)
# print('Кол-во цифр 3 при втором объединении:', a.count(3))
# print('Итоговый список:', a)
