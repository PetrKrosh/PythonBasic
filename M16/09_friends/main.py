list_notes = [[1, 2, 50], [2, 1, 100], [1, 3, 100]]

sum_got = 0
sum_gave = 0

for i_friend in range(1, count_friends + 1):
    sum_got = 0
    sum_gave = 0
    for i in list_notes:
        if i_friend == i[0]:
            sum_got += i[2]
        elif i_friend == i[1]:
            sum_gave -= i[2]
    # print(i_friend, 'получил', sum_got)
    # print(i_friend, 'отдал', sum_gave)
    print('Баланс ', i_friend, ':', sum_got + sum_gave)


















# friends = int(input('Кол-во друзей: '))
# debt = int(input('Долговых расписок: '))
# ious = [[0, 0]]
# for _ in range(friends - 1):
#     ious.append([0, 0])
#
# for i_debt in range(debt):
#     print(i_debt + 1, 'расписка')
#     who = int(input('Кому: '))
#     from_whom = int(input('От кого: '))
#     how = int(input('Сколько: '))
#     ious[who - 1][0] += 1
#     ious[who - 1][1] += how
#     ious[from_whom - 1][0] -= 1
#     ious[from_whom - 1][1] -= how
#
#
# print('Баланс друзей: ')
# for i in range(len(ious)):
#     print(i + 1, ':', ious[i][1])
