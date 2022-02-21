# name = 'Tom'
# N_order = 3456
#
# print('Здравствуйте, {name}! Ваш номер заказа: {order}. Приятного дня {name}!'.format(name=name, order=N_order))
# print('Здравствуйте, {0}! Ваш номер заказа: {1}. Приятного дня {0}!'.format(name, N_order))
# # print('Номер заказа: {order}'.format(order = N_order))

# Start--------------------------------------------
# words = ['one', 'two', 'four']
# str = input('Input str: ')
#
# str_list = str.split()
#
# print(str_list)
# print(str_list.count(words[0]))
# print('Word {0} is containes {1}'.format(words[0], str_list.count(words[0])))
# print('Word {0} is containes {1}'.format(words[1], str_list.count(words[1])))
# print('Word {0} is containes {1}'.format(words[2], str_list.count(words[2])))
# End----------------------------------------------

# Start--------------------------------------------
# str = 'У       нас         пошёл                    снег    ! '
# str_list = str.split()
# print(' '.join(str_list))
# End----------------------------------------------

# # Start--------------------------------------------
# while True:
# 	cong_template = input('Введите шаблон поздравления,'
# 						  'в шаблоне можно использовать конструкцию'
# 						  '{name} и {age}:')
# 	if '{name}' in cong_template and '{age}' in cong_template:
# 		break
# 	print('Отсутствует одна из кострукций')
#
# name_list = input('Список людей через запятую: ').split(', ')
# age = input('Возраст людей через пробел: ')
# age_list = [int(i) for i in age.split()]
#
# for i_man in range(len(name_list)):
# 	print(cong_template.format(name=name_list[i_man], age=age_list[i_man]))
#
# people = [
# 	' '.join([name_list[i_man], str(age_list[i_man])])
# 	for i_man in range(len(name_list))
# ]
#
# people_str = ', '.join(people)
#
# print('\nИменинники: ', people_str)
# # End--------------------------------------------

# # Start. Шифр Цезаря-------------------------------
# str = input('Input STR: ').lower()
# str = str.strip()
# alphabet = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# result = ''
# secret_str = ''
# k = 3
#
# secret_list = [(alphabet[(alphabet.index(i) + k) % len(alphabet)] if i != ' ' else ' ')
#                 for i in str]
#
# for i in secret_list:
#     secret_str += i
# print(secret_str)
# # End--------------------------------------------

# # Start. Проверка расширения и диска --------------
# disk = input('На каком диске должен лежать файл: ')
# extention = input('Требуемое расширение файла: ')
# path = input('Путь к файлу: ')
#
# if not path.startswith(disk):
# 	print('Диск не коректен')
# elif not path.endswith(extention):
# 	print('Расширение не корректно')
# else:
# 	print('Путь корректен!')
# # End--------------------------------------------


str = input('Введите строку: ')
elem_upper = 0
elem_lower = 0
for elem in str:
	elem_upper += elem.isupper()
	elem_lower += elem.islower()
if elem_upper > elem_lower:
	print(str.upper())
else:
	print(str.lower())