
list_size_of_sky = []
list_size_of_legs = []

count_of_sky = int(input('Кол-во коньков: '))
count_of_people = int(input('Кол-во людей: '))

for i in range(1, count_of_sky+1):
    print('Размер ', i, '-й пары: ', end=' ')
    list_size_of_sky.append(input())

for i in range(1, count_of_people+1):
    print('Размер ноги', i, '-го человека: ', end=' ')
    list_size_of_legs.append(input())

count = 0
for i_people in list_size_of_legs:
    for i_sky in list_size_of_sky:
        if i_sky == i_people:
            count += 1
            list_size_of_sky.remove(i_sky)
print(list_size_of_sky)
print('Наибольшее кол-во людей, которые могут взять ролики: ', count)