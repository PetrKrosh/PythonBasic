
list_people = []
count_members = int(input('Кол-во человек: '))
list_people = list(range(1, count_members+1))

while len(list_people) > 1:
	print('Текущий круг людей: ', list_people)
	num_for_del = int(input('Номер для выбывания: '))
	print('Значит, выбывает каждый', num_for_del, '-й человек')
	if num_for_del <= len(list_people):
		print('Выбывает человек под номером', num_for_del)
		list_people.remove(num_for_del)
	elif num_for_del > len(list_people):
		num_for_del -= len(list_people)
		print('Выбывает человек под номером', num_for_del)
		list_people.remove(num_for_del)
	# print(list_people)

print('Остался человек под номером ',list_people)
